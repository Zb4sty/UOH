#!/usr/bin/env python
# manual

"""
This script allows you to manually control the simulator or Duckiebot
using the keyboard arrows.
"""

import sys
import argparse
import pyglet
import cv2
from pyglet.window import key
import numpy as np
import gym
import gym_duckietown
from gym_duckietown.envs import DuckietownEnv
from gym_duckietown.wrappers import UndistortWrapper

# from experiments.utils import save_img

parser = argparse.ArgumentParser()
parser.add_argument('--env-name', default='Duckietown-udem1-v0')
parser.add_argument('--map-name', default='udem1')
parser.add_argument('--distortion', default=False, action='store_true')
parser.add_argument('--draw-curve', action='store_true', help='draw the lane following curve')
parser.add_argument('--draw-bbox', action='store_true', help='draw collision detection bounding boxes')
parser.add_argument('--domain-rand', action='store_true', help='enable domain randomization')
parser.add_argument('--frame-skip', default=1, type=int, help='number of frames to skip')
parser.add_argument('--seed', default=1, type=int, help='seed')
args = parser.parse_args()

if args.env_name and args.env_name.find('Duckietown') != -1:
    env = DuckietownEnv(
        seed = args.seed,
        map_name = args.map_name,
        draw_curve = args.draw_curve,
        draw_bbox = args.draw_bbox,
        domain_rand = args.domain_rand,
        frame_skip = args.frame_skip,
        distortion = args.distortion,
    )
else:
    env = gym.make(args.env_name)

env.reset()
env.render()

@env.unwrapped.window.event
def on_key_press(symbol, modifiers):
    """
    This handler processes keyboard commands that
    control the simulation
    """

    if symbol == key.BACKSPACE or symbol == key.SLASH:
        print('RESET')
        env.reset()
        env.render()
    elif symbol == key.PAGEUP:
        env.unwrapped.cam_angle[0] = 0
    elif symbol == key.ESCAPE:
        env.close()
        sys.exit(0)

    # Take a screenshot
    # UNCOMMENT IF NEEDED - Skimage dependency
    # elif symbol == key.RETURN:
    #     print('saving screenshot')
    #     img = env.render('rgb_array')
    #     save_img('screenshot.png', img)


# Register a keyboard handler
key_handler = key.KeyStateHandler()
env.unwrapped.window.push_handlers(key_handler)

def update(dt):
    """
    This function is called at every frame to handle
    movement/stepping and redrawing
    """

    action = np.array([0.0, 0.0])

    if key_handler[key.UP]:
        action = np.array([0.44, 0.0])
    if key_handler[key.DOWN]:
        action = np.array([-0.44, 0])
    if key_handler[key.LEFT]:
        action = np.array([0.35, +1])
    if key_handler[key.RIGHT]:
        action = np.array([0.35, -1])
    if key_handler[key.SPACE]:
        action = np.array([0, 0])

    # Speed boost
    if key_handler[key.LSHIFT]:
        action *= 1.5

    obs, reward, done, info = env.step(action)
    obs = cv2.cvtColor(obs, cv2.COLOR_BGR2RGB)
    print('step_count = %s, reward=%.3f' % (env.unwrapped.step_count, reward))

    if key_handler[key.RETURN]:
        from PIL import Image
        im = Image.fromarray(obs)

        im.save('screen.png')

    if done:
        print('done!')
        env.reset()
        env.render()

    hsv = cv2.cvtColor(obs, cv2.COLOR_RGB2HSV)

    # Primer filtro (Linea continua)
    lower_medio = np.array([86, 66, 161])
    upper_medio = np.array([94, 255, 226])

    # Ops morfologicas
    mask_m = cv2.inRange(hsv, lower_medio, upper_medio)
    kernel_m = np.ones((5, 5), np.uint8)
    op_morf_medio = cv2.erode(mask_m, kernel_m, iterations=2)
    op_morf_medio = cv2.dilate(mask_m, kernel_m, iterations=2)

    # Canny 
    dst_m = cv2.Canny(op_morf_medio, 50, 200, None, 3)
    cdst_m = cv2.cvtColor(dst_m, cv2.COLOR_GRAY2BGR)
    contours, _ = cv2.findContours(mask_m, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Obtener lineas 
    lines = cv2.HoughLinesP(dst_m, 1, np.pi / 180, 50, None, 50, 10)
    if lines is not None:
        for i in range(0, len(lines)):
            l = lines[i][0]
            cv2.line(cdst_m, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv2.LINE_AA)
            cv2.drawContours(cdst_m, contours, -1, (128,128,128), 3)
    
    # Segundo Filtro (baldosas)
    lower_lateral = np.array([27, 0, 130])
    upper_lateral = np.array([126, 63, 209])

    # Ops morfologicas 
    mask_l = cv2.inRange(hsv, lower_lateral, upper_lateral)
    kernel_l = np.ones((5, 5), np.uint8)
    op_morf_lateral = cv2.erode(mask_l, kernel_l, iterations=2)
    op_morf_lateral = cv2.dilate(mask_l, kernel_l, iterations=2)

    # Canny 
    dst_l = cv2.Canny(op_morf_lateral, 50, 200, None, 3)
    cdst_l = cv2.cvtColor(dst_l, cv2.COLOR_GRAY2BGR)

    # Sobreescribir lineas
    lines = cv2.HoughLinesP(dst_l, 1, np.pi / 180, 50, None, 50, 10)
    if lines is not None:
        for i in range(0, len(lines)):
            l = lines[i][0]
            cv2.line(cdst_l, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv2.LINE_AA)
            cv2.drawContours(cdst_l, contours, -1, (0, 255, 255), 3)


    # Display output image
    cv2.imshow('Imagen',cdst_l)
    cv2.waitKey(1)

    env.render()

pyglet.clock.schedule_interval(update, 1.0 / env.unwrapped.frame_rate)

# Enter main event loop
pyglet.app.run()

env.close()
