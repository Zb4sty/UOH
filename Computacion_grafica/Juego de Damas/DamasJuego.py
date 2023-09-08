"""
Mini Read-Me: Hay veces que se pega, pero es por la cantidad de procesos que realiza, adjuntaré un video con el funcionamiento del programa
para que vean que si funciona y cumple con lo solicitado.
Código creado por : Bastián Rubio
Bonus: Incorporar alguna mejora o nueva funcionalidad al juego actual

La Funcionalidad que incorporé fueron el total de jugadas que se realizaron

"""

import sys
from PyQt5 import  QtWidgets, uic
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import QtOpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PyQt5.QtWidgets import QMessageBox
import numpy as np
import random

class Ventana(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('Damas.ui')
        self.ui.setWindowFlags(Qt.WindowMinimizeButtonHint)
        self.ui.show()
        self.viewer3D = Viewer3DWidget(self)
        self.ui.OpenGLLayout.addWidget(self.viewer3D)
        self.ui.actionJugadas.triggered.connect(self.mostrar_Jugadas)
        self.ui.actionCerrar.triggered.connect(self.Cerrar)
        self.ui.Finish.clicked.connect(self.Reiniciar)
        self.ui.Random.clicked.connect(self.Oponente)

        self.tablero = [ #1 Son las piezas rojas, 2 son las piezas negras y 5 son los cuadrados negros
            [1, 5, 1, 5, 0, 5, 2, 5],
            [5, 1, 5, 0, 5, 2, 5, 2],
            [1, 5, 1, 5, 0, 5, 2, 5],
            [5, 1, 5, 0, 5, 2, 5, 2],
            [1, 5, 1, 5, 0, 5, 2, 5],
            [5, 1, 5, 0, 5, 2, 5, 2],
            [1, 5, 1, 5, 0, 5, 2, 5],
            [5, 1, 5, 0, 5, 2, 5, 2]
        ]



    @pyqtSlot()
    def Reiniciar(self):
        print("Reiniciar")
        self.viewer3D.board = self.tablero #El mandamos el tablero original
        self.viewer3D.posx = 0
        self.viewer3D.posy = 0
        self.viewer3D.mover(0,0)
        self.viewer3D.updateGL()
    
    #Función Bonus
    @pyqtSlot()
    def mostrar_Jugadas(self):
        total_jugadas = self.viewer3D.contador
        message = "El total de jugadas fue: {}".format(total_jugadas)
        QMessageBox.information(self, "Jugadas", message)

    @pyqtSlot()
    def Oponente(self):
        self.viewer3D.oponente()
        self.viewer3D.updateGL()

    
    @pyqtSlot()
    def Cerrar(self):
        sys.exit(app.exec_())
    
class Viewer3DWidget(QtOpenGL.QGLWidget):
    def __init__(self, parent=None):
        QtOpenGL.QGLWidget.__init__(self, parent)
        self.setFocusPolicy(Qt.StrongFocus)
        self.board = [ #1 Son las piezas rojas, 2 son las piezas negras y 5 son los cuadrados negros
            [1, 5, 1, 5, 0, 5, 2, 5],
            [5, 1, 5, 0, 5, 2, 5, 2],
            [1, 5, 1, 5, 0, 5, 2, 5],
            [5, 1, 5, 0, 5, 2, 5, 2],
            [1, 5, 1, 5, 0, 5, 2, 5],
            [5, 1, 5, 0, 5, 2, 5, 2],
            [1, 5, 1, 5, 0, 5, 2, 5],
            [5, 1, 5, 0, 5, 2, 5, 2]
        ]

        #Movimiento de jugador
        self.pieza_seleccionada = False
        self.posx = 0
        self.posy = 0

        self.posiciones = []
        self.lcuadrado = 1
        self.contador = 0


    #funciones por defecto
    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.dibujar()
        glFlush()
    
    def resizeGL(self, widthInPixels, heightInPixels):
        glViewport(0, 0, widthInPixels, heightInPixels)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, 8, 0, 8, -1, 1)
        glMatrixMode(GL_MODELVIEW)

    def initializeGL(self):
       glClearColor(0.0,0.0,0.0,1.0)
    
    def dibujar(self):
        self.grid()

    
    #Se pinta el tablero
    def grid(self):
        for x in range(8):
            for y in range(8):
                # Calcular la posición del cuadrado actual

                # Determinar el color del cuadrado
                if (x + y) % 2 == 0:
                    glColor3f(1.0, 1.0, 1.0)  # Blanco
                else:
                    glColor3f(0.0, 0.0, 0.0)  # Negro

                # Dibujar el cuadrado
                glBegin(GL_QUADS)
                glVertex2f(x, y)
                glVertex2f(x + self.lcuadrado, y)
                glVertex2f(x + self.lcuadrado, y + self.lcuadrado)
                glVertex2f(x, y + self.lcuadrado)
                glEnd()

                if ((x + y) % 2 == 0):
                    if(self.board[x][y] == 1):
                        glColor3f(1.0, 0.0, 0.0) #Rojo
                    elif(self.board[x][y] == 2):
                        glColor3f(0.0, 0.0, 0.0) #Negro
                    glBegin(GL_POLYGON)
                    num_segments = 100
                    for k in range(num_segments):
                        theta = 2.0 * 3.1415926 * k / num_segments
                        cx = x + self.lcuadrado / 2.0 + self.lcuadrado / 4.0 * np.cos(theta)
                        cy = y + self.lcuadrado / 2.0 + self.lcuadrado / 4.0 * np.sin(theta)
                        glVertex2f(cx, cy)
                    glEnd()
        self.mover(0,0)

    def mover(self, x, y):
        self.posx += x
        self.posy += y
        #Mantener margenes
        #inferior
        if(self.posx < 0):
            self.posx = 0
        elif(self.posy < 0):
            self.posy = 0
        #superior
        if(self.posx > 7):
            self.posx = 7
        elif(self.posy > 7):
            self.posy = 7
        #Mover
        glColor3f(1.0, 1.0, 0.0)
        glBegin(GL_QUADS)
        glVertex2f(self.posx, self.posy)
        glVertex2f(self.posx + self.lcuadrado, self.posy)
        glVertex2f(self.posx + self.lcuadrado, self.posy + self.lcuadrado)
        glVertex2f(self.posx, self.posy + self.lcuadrado)
        glEnd()

    #Mover con el teclado
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            self.mover(0, 1)
        elif event.key() == Qt.Key_Down:
            self.mover(0, -1)
        elif event.key() == Qt.Key_Left:
            self.mover(-1, 0)
        elif event.key() == Qt.Key_Right:
            self.mover(1, 0)
        elif event.key() == Qt.Key_Space:
            self.confirmar(self.posx, self.posy)            
        
        self.update()

    def confirmar(self, posx, posy):
        if(self.pieza_seleccionada == False):
            #Aqui es el primer espacio
            self.pieza_seleccionada = True
            #Agregamos las posiciones
            self.posiciones.append(posx)
            self.posiciones.append(posy)
        elif(self.pieza_seleccionada == True):
            #Aqui es el segundo true y tenemos que mover la pieza en la matriz
            #Usuario siempre tendra el número 1
            if(self.board[posx][posy] == 0):
                #Movimiento a casilla vacía
                if(abs(posx - self.posiciones[0]) == 1 and (posy-self.posiciones[1] == 1)):
                    #Actualizamos
                    self.board[posx][posy] = 1
                    self.board[self.posiciones[0]][self.posiciones[1]] = 0
                
            elif(self.board[posx][posy] == 2):
                #Movimiento a la casilla de otro jugador
                ay = posy+1
                #izq
                axi = posx-1
                #der
                axd = posx+1
                if(self.board[axi][ay] == 0):
                    self.board[axi][ay] = 1 #Actualiza nueva posicion
                    self.board[posx][posy] = 0 #Quita la pieza
                    self.board[self.posiciones[0]][self.posiciones[1]] = 0 #Mueve la ficha
                elif(self.board[axd][ay] == 0):
                    self.board[axd][ay] = 1 #Actualiza nueva posicion
                    self.board[posx][posy] = 0 #Quita la pieza
                    self.board[self.posiciones[0]][self.posiciones[1]] = 0 #Mueve la ficha
            
            self.contador += 1 #Jugadas
            #Reiniciar
            self.posiciones.pop()
            self.posiciones.pop()
            self.pieza_seleccionada = False
            self.verificar()

    def oponente(self):
        # Mueve una pieza del oponente aleatoriamente
        piezas_oponente = []
        piezas_movibles = []
        for x in range(8):
            for y in range(8):
                if (self.board[x][y] == 2):
                    piezas_oponente.append((x,y))
        
        for i in range(len(piezas_oponente)):
            pos = piezas_oponente[i]
            posy = pos[1]-1
            if(pos[0]-1 >= 0 and self.board[pos[0]-1][posy] == 0):
                piezas_movibles.append((pos[0],pos[1]))
            elif(pos[0]-1 >= 0 and self.board[pos[0]-1][posy] == 1):
                if(pos[0]-2 >= 0 and self.board[pos[0]-2][posy-1] == 0):
                    piezas_movibles.append((pos[0],pos[1]))
        
        lado = random.choice([-1,1])
        movimiento = random.choice(piezas_movibles)
        #Verificador de movimiento
        if(self.board[movimiento[0] + lado][movimiento[1]-1] == 0 and self.mov_valido(movimiento[0] + lado, movimiento[1]-1)):
            self.board[movimiento[0]][movimiento[1]] = 0
            self.board[movimiento[0] + lado][movimiento[1]-1] = 2
        elif(self.board[movimiento[0] + lado][movimiento[1]-1] == 1 and self.mov_valido(movimiento[0] + lado, movimiento[1]-1)):
            if(self.board[movimiento[0] + lado * 2][movimiento[1]-2] == 0 and self.mov_valido(movimiento[0] + lado * 2, movimiento[1]-2)):
                self.board[movimiento[0]][movimiento[1]] = 0
                self.board[movimiento[0] + lado][movimiento[1]-1] = 0
                self.board[movimiento[0] + lado * 2][movimiento[1]-2] = 2
        self.contador += 1
        self.verificar()

    def mov_valido(self,x,y): #Verificar que este dentro del tablero
        if(x>= 8 or x<0 or y>=8 or y <0):
            return False
        return True
    
    #Verificación de ganador
    def verificar(self):
        for i in range(8):
            if(self.board[i][7] == 1):
                QMessageBox.information(self, "Damas", "Ganaste!")#Titulo, Mensaje
            elif(self.board[i][0] == 2):
                QMessageBox.information(self, "Damas", "Gano el oponente!")



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ventana = Ventana()
    sys.exit(app.exec_())