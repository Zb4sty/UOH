"""
Bonus: Agregar algún widget no visto en cátedra ni en las ayudantías
Código hecho por Bastián Rubio Moya
"""

import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import QtOpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from NB import *
import random
from PyQt5.QtWidgets import QMessageBox

#Ventana principal
class Ventana(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('cubo.ui')
        self.ui.setWindowTitle('Rubik')
        self.ui.setWindowIcon(QtGui.QIcon('uoh.jpg'))
        self.ui.setWindowFlags(Qt.WindowMinimizeButtonHint)

        self.viewer3D = Viewer3DWidget(self)
        self.ui.OpenGLLayout.addWidget(self.viewer3D)
        self.ui.show()

        #Vars cubo colores
        self.c0 = [0,1,2,3,4,5] # Atras Abajo Izquierda
        self.c1 = [0,1,2,3,4,5] # Atras Arriba Izquierda    
        self.c2 = [0,1,2,3,4,5] # Atras Abajo Derecha
        self.c3 = [0,1,2,3,4,5] # Atras Arriba Derecha  
        self.c4 = [0,1,2,3,4,5] # Adelante Abajo Izquierda
        self.c5 = [0,1,2,3,4,5] # Adelante Arriba Izquierda
        self.c6 = [0,1,2,3,4,5] # Adelante Abajo Derecha
        self.c7 = [0,1,2,3,4,5] # Adelante Arriba Derecha

        #signals
        self.ui.actionCerrar.triggered.connect(self.Cerrar)
        
        self.ui.rotarx.valueChanged.connect(self.rotarx)
        self.ui.rotary.valueChanged.connect(self.rotary)
        self.ui.rotarz.valueChanged.connect(self.rotarz)

        self.ui.ordenar.clicked.connect(self.ordenar)
        self.ui.desordenar.clicked.connect(self.desordenar)

    @pyqtSlot()
    def ordenar(self):
        self.c0 = [0,1,2,3,4,5] # Atras Abajo Izquierda
        self.c1 = [0,1,2,3,4,5] # Atras Arriba Izquierda    
        self.c2 = [0,1,2,3,4,5] # Atras Abajo Derecha
        self.c3 = [0,1,2,3,4,5] # Atras Arriba Derecha  
        self.c4 = [0,1,2,3,4,5] # Adelante Abajo Izquierda
        self.c5 = [0,1,2,3,4,5] # Adelante Arriba Izquierda
        self.c6 = [0,1,2,3,4,5] # Adelante Abajo Derecha
        self.c7 = [0,1,2,3,4,5] # Adelante Arriba Derecha 
        cubos_ord = [self.c0,self.c1,self.c2,self.c3,self.c4,self.c5,self.c6,self.c7]
        self.viewer3D.cubos = cubos_ord
        self.viewer3D.updateGL()
    
    @pyqtSlot()
    def desordenar(self):
        #Aleatoriedad
        random.shuffle(self.c0)
        random.shuffle(self.c1)
        random.shuffle(self.c2)
        random.shuffle(self.c3)
        random.shuffle(self.c4)
        random.shuffle(self.c5)
        random.shuffle(self.c6)
        random.shuffle(self.c7) 
        cubos_desord = [self.c0,self.c1,self.c2,self.c3,self.c4,self.c5,self.c6,self.c7]
        self.viewer3D.cubos = cubos_desord
        self.viewer3D.updateGL()

    @pyqtSlot()
    def rotarx(self):
        ang = int(self.ui.rotarx.value())
        self.viewer3D.angx = ang
        self.ui.lx.setText(str(ang))
        self.viewer3D.updateGL() 

    @pyqtSlot()
    def rotary(self):
        ang = int(self.ui.rotary.value())
        self.viewer3D.angy = ang
        self.ui.ly.setText(str(ang))
        self.viewer3D.updateGL() 

    @pyqtSlot()
    def rotarz(self):
        ang = int(self.ui.rotarz.value())
        self.viewer3D.angz = ang
        self.ui.lz.setText(str(ang))
        self.viewer3D.updateGL() 

    @pyqtSlot()
    def Cerrar(self):
        op = QMessageBox.question(self, "Confirmación", "¿Desea salir?")
        if(op == QMessageBox.Yes):
            sys.exit(app.exec_())
        elif(op == QMessageBox.No):
            pass


class Viewer3DWidget(QtOpenGL.QGLWidget):
    max_xyz = 2.0
    def __init__(self, parent=None):
        QtOpenGL.QGLWidget.__init__(self, parent)
        self.setFocusPolicy(Qt.StrongFocus)
        self.angx = 0
        self.angy = 0
        self.angz = 0
        self.current_cube = 5
        self.flechas = True
        self.primer_mov = True
        self.mov = -1
        self.c0 = [0,1,2,3,4,5] # Atras Abajo Izquierda
        self.c1 = [0,1,2,3,4,5] # Atras Arriba Izquierda    
        self.c2 = [0,1,2,3,4,5] # Atras Abajo Derecha
        self.c3 = [0,1,2,3,4,5] # Atras Arriba Derecha  
        self.c4 = [0,1,2,3,4,5] # Adelante Abajo Izquierda
        self.c5 = [0,1,2,3,4,5] # Adelante Arriba Izquierda
        self.c6 = [0,1,2,3,4,5] # Adelante Abajo Derecha
        self.c7 = [0,1,2,3,4,5] # Adelante Arriba Derecha 
        self.cubos = [self.c0,self.c1,self.c2,self.c3,self.c4,self.c5,self.c6,self.c7]

    #Funciones protegidas OpenGL
    def paintGL(self):
        glMatrixMode( GL_MODELVIEW )
        glLoadIdentity()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glEnable(GL_DEPTH_TEST)
        self.dibujar()
        glFlush()
    def resizeGL(self, widthInPixels, heightInPixels):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-self.max_xyz, self.max_xyz, \
                -self.max_xyz, self.max_xyz, \
                -self.max_xyz, self.max_xyz)
        glViewport(0, 0, widthInPixels, heightInPixels)
    def initializeGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClearDepth(1.0)
    #Metodos-seleccion-figuras
    def dibujar(self):
        glRotatef(self.angx, 0.5, 0.0, 0.0)
        glRotatef(self.angy, 0.0, 0.5, 0.0)
        glRotatef(self.angz, 0.0, 0.0, 0.5)
        cube(self.current_cube, self.mov, self.flechas, self.cubos)
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            self.mover('up')
            self.flechas = True
        elif event.key() == Qt.Key_Down:
            self.mover('dw')
            self.flechas = True
        elif event.key() == Qt.Key_Left:
            self.mover('lf')
            self.flechas = True
        elif event.key() == Qt.Key_Right:
            self.mover('rg')
            self.flechas = True
        elif event.key() == Qt.Key_A:
            self.mover_cubo('A')
            self.flechas = False
        elif event.key() == Qt.Key_S:
            self.mover_cubo('S')
            self.flechas = False
        elif event.key() == Qt.Key_W:
            self.mover_cubo('W')
            self.flechas = False
        elif event.key() == Qt.Key_D:
            self.mover_cubo('D')
            self.flechas = False
        



    def mover(self, pos): #moverse dentro del cubo
        if(pos == 'up'):
            #front
            if(self.current_cube == 4):
                self.current_cube = 5
            elif(self.current_cube == 6):
                self.current_cube = 7
            #back
            elif(self.current_cube == 0):
                self.current_cube = 1
            elif(self.current_cube == 2):
                self.current_cube = 3
        elif(pos == 'dw'):
            if(self.current_cube == 5):
                self.current_cube = 4
            elif(self.current_cube == 7):
                self.current_cube = 6
            #back
            elif(self.current_cube == 1):
                self.current_cube = 0
            elif(self.current_cube == 3):
                self.current_cube = 2
        elif(pos == 'lf'):
            #bottom
            if(self.current_cube == 0):
                self.current_cube = 2
            elif(self.current_cube == 2):
                self.current_cube = 6
            elif(self.current_cube == 4):
                self.current_cube = 0
            elif(self.current_cube == 6):
                self.current_cube = 4
            #top
            elif(self.current_cube == 7):
                self.current_cube = 5
            elif(self.current_cube == 5):
                self.current_cube = 1
            elif(self.current_cube == 1):
                self.current_cube = 3
            elif(self.current_cube == 3):
                self.current_cube = 7
        elif(pos == 'rg'):
            #bottom
            if(self.current_cube == 4):
                self.current_cube = 6
            elif(self.current_cube == 6):
                self.current_cube = 2
            elif(self.current_cube == 2):
                self.current_cube = 0
            elif(self.current_cube == 0):
                self.current_cube = 4
            #top
            elif(self.current_cube == 5):
                self.current_cube = 7
            elif(self.current_cube == 7):
                self.current_cube = 3
            elif(self.current_cube == 3):
                self.current_cube = 1
            elif(self.current_cube == 1):
                self.current_cube = 5
        
        self.update()

    def mover_cubo(self, pos): 
        #mov 1-UP / 2-DN / 3-LF / 4-RG
        if(pos == 'A'): #Izquiereda
            self.mov = 3
        elif(pos == 'S'): #Abajo
            self.mov = 2
        elif(pos == 'D'): #Derecha
            self.mov = 4
        elif(pos == 'W'): #Arriba 1
            self.mov = 1
        self.verificar()
        self.update()
    
    def verificar(self):
        cnt = 0
        if(self.primer_mov != True):
            for i in range(0,6):
                if(self.cubos[0][i] == self.cubos[1][i] == self.cubos[2][i] == self.cubos[3][i] == self.cubos[4][i] == self.cubos[5][i] == self.cubos[6][i] == self.cubos[7][i]):
                    cnt += 1
            
            if(cnt == 6):
                op = QMessageBox.question(self, "Juego Terminado", "Juego Terminado\n ¿Desea salir?")
                if(op == QMessageBox.Yes):
                    sys.exit(app.exec_())
                elif(op == QMessageBox.No):
                    pass
        else:
            self.primer_mov = False
        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = Ventana()
    sys.exit(app.exec_())
    