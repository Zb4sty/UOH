from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def cube(current_cube,movimiento, flechas, cubos):
    
    #Colores por cubo Fre,Atr, Arr, Aba, Izq, Der 
    #Movimientos de colores
    movs= [] #Guardar cubos que se tienen que mover
    if(movimiento == 1): #Arriba
        if(current_cube == 0 or current_cube == 1 or current_cube == 4 or current_cube == 5):
            movs = [0,1,4,5]
        elif(current_cube == 2 or current_cube == 3 or current_cube == 6 or current_cube == 7):
            movs = [2,3,6,7]
    elif(movimiento == 2): #Abajo
        if(current_cube == 0 or current_cube == 1 or current_cube == 4 or current_cube == 5):
            movs = [0,1,4,5]
        elif(current_cube == 2 or current_cube == 3 or current_cube == 6 or current_cube == 7):
            movs = [2,3,6,7]
    elif(movimiento == 3): #Izquierda
        if(current_cube == 0 or current_cube == 2 or current_cube == 4 or current_cube == 6):
            movs = [0,2,4,6]
        elif(current_cube == 1 or current_cube == 3 or current_cube == 5 or current_cube == 7):
            movs = [1,3,5,7]
    elif(movimiento == 4): #Derecha
        if(current_cube == 0 or current_cube == 2 or current_cube == 4 or current_cube == 6):
            movs = [0,2,4,6]
        elif(current_cube == 1 or current_cube == 3 or current_cube == 5 or current_cube == 7):
            movs = [1,3,5,7]

    #Swap de colores
    if(flechas == False):
        for i in movs:
            if(movimiento == 1): #Arriba
                frente = cubos[i][0]
                atras = cubos[i][1]
                arriba = cubos[i][2]
                abajo = cubos[i][3]

                cubos[i][0] = abajo
                cubos[i][1] = arriba
                cubos[i][2] = frente
                cubos[i][3] = atras
            elif(movimiento == 2):
                frente = cubos[i][0]
                atras = cubos[i][1]
                arriba = cubos[i][2]
                abajo = cubos[i][3]

                cubos[i][0] = arriba
                cubos[i][1] = abajo
                cubos[i][2] = atras
                cubos[i][3] = frente
            elif(movimiento == 3):
                frente = cubos[i][0]
                atras = cubos[i][1]
                izq = cubos[i][4]
                der = cubos[i][5]

                cubos[i][0] = der
                cubos[i][1] = izq
                cubos[i][4] = frente
                cubos[i][5] = atras
            elif(movimiento == 4):
                frente = cubos[i][0]
                atras = cubos[i][1]
                izq = cubos[i][4]
                der = cubos[i][5]

                cubos[i][0] = izq
                cubos[i][1] = der
                cubos[i][4] = atras
                cubos[i][5] = frente

    translates_coords = [
        [0.0,0.0,0.0],
        [0.0,1.0,0.0],
        [1.0,0.0,0.0],
        [1.0,1.0,0.0],
        [0.0,0.0,1.0],
        [0.0,1.0,1.0],
        [1.0,0.0,1.0],
        [1.0,1.0,1.0]
        
    ]

    colors = [
        [1.0, 0.0, 0.0],    # Rojo
        [0.0, 1.0, 0.0],    # Verde
        [0.0, 0.0, 1.0],    # Azul
        [1.0, 1.0, 0.0],    # Amarillo
        [1.0, 0.5, 0.0],    # Naranja
        [1.0, 1.0, 1.0]     # Blanco
    ]
    for i in range(len(translates_coords)):
        r = 0.49
        v = 0.5 #Opacidad
        glPushMatrix()        
        glTranslatef(translates_coords[i][0],translates_coords[i][1],translates_coords[i][2])  # Mover el cubo a una nueva posición

        glBegin(GL_QUADS)
        
        # Dibujar las caras del cubo
        #Frente
        if(i == current_cube): 
            if(cubos[i][0] == 0): #Rojo
                glColor3f(colors[0][0]+v, colors[0][1]+v, colors[0][2]+v)
            elif(cubos[i][0] == 1): #Verde
                glColor3f(colors[1][0]+v, colors[1][1]+v, colors[1][2]+v)
            elif(cubos[i][0] == 2): #Azul
                glColor3f(colors[2][0]+v, colors[2][1]+v, colors[2][2]+v)
            elif(cubos[i][0] == 3): #Amarillo
                glColor3f(colors[3][0]+v, colors[3][1]+v, colors[3][2]+v)
            elif(cubos[i][0] == 4): #Naranja
                glColor3f(colors[4][0]+v, colors[4][1]+v, colors[4][2]+v)
            elif(cubos[i][0] == 5): #Blanco
                glColor3f(colors[5][0]+v, colors[5][1]+v, colors[5][2]+v)
        else:
            if(cubos[i][0] == 0): #Rojo
                glColor3f(colors[0][0], colors[0][1], colors[0][2])
            elif(cubos[i][0] == 1): #Verde
                glColor3f(colors[1][0], colors[1][1], colors[1][2])
            elif(cubos[i][0] == 2): #Azul
                glColor3f(colors[2][0], colors[2][1], colors[2][2])
            elif(cubos[i][0] == 3): #Amarillo
                glColor3f(colors[3][0], colors[3][1], colors[3][2])
            elif(cubos[i][0] == 4): #Naranja
                glColor3f(colors[4][0], colors[4][1], colors[4][2])
            elif(cubos[i][0] == 5): #Blanco
                glColor3f(colors[5][0], colors[5][1], colors[5][2])

        
        #Vertices frente
        glVertex3f(-r, -r, r)
        glVertex3f(r, -r, r)
        glVertex3f(r, r, r)
        glVertex3f(-r, r, r)
        
        #Atras
        if(i == current_cube): 
            if(cubos[i][1] == 0): #Rojo
                glColor3f(colors[0][0]+v, colors[0][1]+v, colors[0][2]+v)
            elif(cubos[i][1] == 1): #Verde
                glColor3f(colors[1][0]+v, colors[1][1]+v, colors[1][2]+v)
            elif(cubos[i][1] == 2): #Azul
                glColor3f(colors[2][0]+v, colors[2][1]+v, colors[2][2]+v)
            elif(cubos[i][1] == 3): #Amarillo
                glColor3f(colors[3][0]+v, colors[3][1]+v, colors[3][2]+v)
            elif(cubos[i][1] == 4): #Naranja
                glColor3f(colors[4][0]+v, colors[4][1]+v, colors[4][2]+v)
            elif(cubos[i][1] == 5): #Blanco
                glColor3f(colors[5][0]+v, colors[5][1]+v, colors[5][2]+v)
        else:
            if(cubos[i][1] == 0): #Rojo
                glColor3f(colors[0][0], colors[0][1], colors[0][2])
            elif(cubos[i][1] == 1): #Verde
                glColor3f(colors[1][0], colors[1][1], colors[1][2])
            elif(cubos[i][1] == 2): #Azul
                glColor3f(colors[2][0], colors[2][1], colors[2][2])
            elif(cubos[i][1] == 3): #Amarillo
                glColor3f(colors[3][0], colors[3][1], colors[3][2])
            elif(cubos[i][1] == 4): #Naranja
                glColor3f(colors[4][0], colors[4][1], colors[4][2])
            elif(cubos[i][1] == 5): #Blanco
                glColor3f(colors[5][0], colors[5][1], colors[5][2])

        #Vertices Atras
        glVertex3f(-r, -r, -r)
        glVertex3f(-r, r, -r)
        glVertex3f(r, r, -r)
        glVertex3f(r, -r, -r)
        
        #Arriba
        if(i == current_cube): 
            if(cubos[i][2] == 0): #Rojo
                glColor3f(colors[0][0]+v, colors[0][1]+v, colors[0][2]+v)
            elif(cubos[i][2] == 1): #Verde
                glColor3f(colors[1][0]+v, colors[1][1]+v, colors[1][2]+v)
            elif(cubos[i][2] == 2): #Azul
                glColor3f(colors[2][0]+v, colors[2][1]+v, colors[2][2]+v)
            elif(cubos[i][2] == 3): #Amarillo
                glColor3f(colors[3][0]+v, colors[3][1]+v, colors[3][2]+v)
            elif(cubos[i][2] == 4): #Naranja
                glColor3f(colors[4][0]+v, colors[4][1]+v, colors[4][2]+v)
            elif(cubos[i][2] == 5): #Blanco
                glColor3f(colors[5][0]+v, colors[5][1]+v, colors[5][2]+v)
        else:
            if(cubos[i][2] == 0): #Rojo
                glColor3f(colors[0][0], colors[0][1], colors[0][2])
            elif(cubos[i][2] == 1): #Verde
                glColor3f(colors[1][0], colors[1][1], colors[1][2])
            elif(cubos[i][2] == 2): #Azul
                glColor3f(colors[2][0], colors[2][1], colors[2][2])
            elif(cubos[i][2] == 3): #Amarillo
                glColor3f(colors[3][0], colors[3][1], colors[3][2])
            elif(cubos[i][2] == 4): #Naranja
                glColor3f(colors[4][0], colors[4][1], colors[4][2])
            elif(cubos[i][2] == 5): #Blanco
                glColor3f(colors[5][0], colors[5][1], colors[5][2])
        glVertex3f(-r, r, -r)
        glVertex3f(-r, r, r)
        glVertex3f(r, r, r)
        glVertex3f(r, r, -r)

        #Abajo
        if(i == current_cube): 
            if(cubos[i][3] == 0): #Rojo
                glColor3f(colors[0][0]+v, colors[0][1]+v, colors[0][2]+v)
            elif(cubos[i][3] == 1): #Verde
                glColor3f(colors[1][0]+v, colors[1][1]+v, colors[1][2]+v)
            elif(cubos[i][3] == 2): #Azul
                glColor3f(colors[2][0]+v, colors[2][1]+v, colors[2][2]+v)
            elif(cubos[i][3] == 3): #Amarillo
                glColor3f(colors[3][0]+v, colors[3][1]+v, colors[3][2]+v)
            elif(cubos[i][3] == 4): #Naranja
                glColor3f(colors[4][0]+v, colors[4][1]+v, colors[4][2]+v)
            elif(cubos[i][3] == 5): #Blanco
                glColor3f(colors[5][0]+v, colors[5][1]+v, colors[5][2]+v)
        else:
            if(cubos[i][3] == 0): #Rojo
                glColor3f(colors[0][0], colors[0][1], colors[0][2])
            elif(cubos[i][3] == 1): #Verde
                glColor3f(colors[1][0], colors[1][1], colors[1][2])
            elif(cubos[i][3] == 2): #Azul
                glColor3f(colors[2][0], colors[2][1], colors[2][2])
            elif(cubos[i][3] == 3): #Amarillo
                glColor3f(colors[3][0], colors[3][1], colors[3][2])
            elif(cubos[i][3] == 4): #Naranja
                glColor3f(colors[4][0], colors[4][1], colors[4][2])
            elif(cubos[i][3] == 5): #Blanco
                glColor3f(colors[5][0], colors[5][1], colors[5][2])
        
        #Vertices Abajo
        glVertex3f(-r, -r, -r)
        glVertex3f(r, -r, -r)
        glVertex3f(r, -r, r)
        glVertex3f(-r, -r, r)
        
        #Izquierda
        if(i == current_cube): 
            if(cubos[i][4] == 0): #Rojo
                glColor3f(colors[0][0]+v, colors[0][1]+v, colors[0][2]+v)
            elif(cubos[i][4] == 1): #Verde
                glColor3f(colors[1][0]+v, colors[1][1]+v, colors[1][2]+v)
            elif(cubos[i][4] == 2): #Azul
                glColor3f(colors[2][0]+v, colors[2][1]+v, colors[2][2]+v)
            elif(cubos[i][4] == 3): #Amarillo
                glColor3f(colors[3][0]+v, colors[3][1]+v, colors[3][2]+v)
            elif(cubos[i][4] == 4): #Naranja
                glColor3f(colors[4][0]+v, colors[4][1]+v, colors[4][2]+v)
            elif(cubos[i][4] == 5): #Blanco
                glColor3f(colors[5][0]+v, colors[5][1]+v, colors[5][2]+v)
        else:
            if(cubos[i][4] == 0): #Rojo
                glColor3f(colors[0][0], colors[0][1], colors[0][2])
            elif(cubos[i][4] == 1): #Verde
                glColor3f(colors[1][0], colors[1][1], colors[1][2])
            elif(cubos[i][4] == 2): #Azul
                glColor3f(colors[2][0], colors[2][1], colors[2][2])
            elif(cubos[i][4] == 3): #Amarillo
                glColor3f(colors[3][0], colors[3][1], colors[3][2])
            elif(cubos[i][4] == 4): #Naranja
                glColor3f(colors[4][0], colors[4][1], colors[4][2])
            elif(cubos[i][4] == 5): #Blanco
                glColor3f(colors[5][0], colors[5][1], colors[5][2])

        #Vertices Izquierda
        glVertex3f(-r, -r, -r)
        glVertex3f(-r, -r, r)
        glVertex3f(-r, r, r)
        glVertex3f(-r, r, -r)
        
        #Derecha
        if(i == current_cube): 
            if(cubos[i][5] == 0): #Rojo
                glColor3f(colors[0][0]+v, colors[0][1]+v, colors[0][2]+v)
            elif(cubos[i][5] == 1): #Verde
                glColor3f(colors[1][0]+v, colors[1][1]+v, colors[1][2]+v)
            elif(cubos[i][5] == 2): #Azul
                glColor3f(colors[2][0]+v, colors[2][1]+v, colors[2][2]+v)
            elif(cubos[i][5] == 3): #Amarillo
                glColor3f(colors[3][0]+v, colors[3][1]+v, colors[3][2]+v)
            elif(cubos[i][5] == 4): #Naranja
                glColor3f(colors[4][0]+v, colors[4][1]+v, colors[4][2]+v)
            elif(cubos[i][5] == 5): #Blanco
                glColor3f(colors[5][0]+v, colors[5][1]+v, colors[5][2]+v)
        else:
            if(cubos[i][5] == 0): #Rojo
                glColor3f(colors[0][0], colors[0][1], colors[0][2])
            elif(cubos[i][5] == 1): #Verde
                glColor3f(colors[1][0], colors[1][1], colors[1][2])
            elif(cubos[i][5] == 2): #Azul
                glColor3f(colors[2][0], colors[2][1], colors[2][2])
            elif(cubos[i][5] == 3): #Amarillo
                glColor3f(colors[3][0], colors[3][1], colors[3][2])
            elif(cubos[i][5] == 4): #Naranja
                glColor3f(colors[4][0], colors[4][1], colors[4][2])
            elif(cubos[i][5] == 5): #Blanco
                glColor3f(colors[5][0], colors[5][1], colors[5][2])

        #Vertices derecha
        glVertex3f(r, -r, r)
        glVertex3f(r, -r, -r)
        glVertex3f(r, r, -r)
        glVertex3f(r, r, r)
        
        glEnd()
        glPopMatrix()

    
