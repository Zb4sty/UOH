# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz.ui'
# Creditos a quien corresponda por el archivo de 'haarcascade_frontalface_default.xml'
# Created by: PyQt5 UI code generator 5.15.9

"""
Mini Readme:
Importe el Qt con pyuic5 -x interfaz.ui -o main.py

Al momento de comenzar se demora entre 1-5 segundos en comenzar.
Cuando se coloca en la escala de grises, se demora debido a que, toma fotograma a fotograma.

Para el bonus, elegimos  -> Habilitar/Deshabilitar widgets de acuerdo al funcionamiento del programa.

"""

from pyqtgraph import GraphicsLayoutWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import numpy as np
import cv2, imutils

#VARIABLES GLOBALES PARA QUE FUNCIONE EL RECONOCIMIENTO
cascPath = 'haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascPath)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #Función por defecto de la importación, usada para asignar los valores de la inferfaz
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1131, 673)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 0, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Century")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 520, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Century")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.comenzar = QtWidgets.QPushButton(self.centralwidget)
        self.comenzar.setGeometry(QtCore.QRect(20, 560, 131, 28))
        font = QtGui.QFont()
        font.setFamily("Century")
        font.setPointSize(11)
        self.comenzar.setFont(font)
        self.comenzar.setStyleSheet("QPushButton{\n"
        "background-color: rgb(255, 255, 255);\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(85, 85, 255);\n"
        "};\n"
        "")
        self.comenzar.setObjectName("comenzar")
        self.histo = GraphicsLayoutWidget(self.centralwidget)
        self.histo.setGeometry(QtCore.QRect(590, 30, 531, 461))
        self.histo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.histo.setObjectName("histo")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(970, 560, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Century")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.FeedLabel = QtWidgets.QLabel(self.centralwidget)
        self.FeedLabel.setGeometry(QtCore.QRect(20, 30, 551, 461))
        self.FeedLabel.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.FeedLabel.setText("")
        self.FeedLabel.setObjectName("FeedLabel")
        self.barra = QtWidgets.QSlider(self.centralwidget)
        self.barra.setGeometry(QtCore.QRect(790, 560, 160, 22))
        self.barra.setOrientation(QtCore.Qt.Horizontal)
        self.barra.setObjectName("barra")
        #Min y Max de la barra
        self.barra.setMinimum(-1) 
        self.barra.setMaximum(255)
        self.color = QtWidgets.QComboBox(self.centralwidget)
        self.color.setGeometry(QtCore.QRect(460, 560, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Century")
        font.setPointSize(11)
        self.color.setFont(font)
        self.color.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.color.setObjectName("color")
        self.color.addItem("")
        self.color.addItem("")
        self.color.addItem("")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(510, 510, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Century")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(790, 0, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Century")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.detener = QtWidgets.QPushButton(self.centralwidget)
        self.detener.setGeometry(QtCore.QRect(190, 560, 131, 28))
        font = QtGui.QFont()
        font.setFamily("Century")
        font.setPointSize(11)
        self.detener.setFont(font)
        self.detener.setStyleSheet("QPushButton{\n"
        "background-color: rgb(255, 255, 255);\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "    background-color: rgb(85, 85, 255);\n"
        "};\n"
        "")
        self.detener.setObjectName("detener")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(820, 520, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Century")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1131, 26))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCerrar = QtWidgets.QAction(MainWindow)
        self.actionCerrar.setObjectName("actionCerrar")
        self.menuArchivo.addAction(self.actionCerrar)
        self.menubar.addAction(self.menuArchivo.menuAction())

        #Definir histograma
        self.ejex = np.arange(0,256) #Creamos el eje x
        self.hcolor = [20, 127, 50] #Definimos el color
        self.widget_plot = self.histo.addPlot() #Definimos en que parte del Qt va el histo
        self.widget_plot.setXRange(0, 255) #Asignamos el eje x
        self.ejey = np.zeros(256) #Creamos el eje y
        self.widget_plot.setYRange(0.2, 1, 0.2) #Rango
        #Label de los histo
        self.widget_plot.setLabel(axis = 'bottom', text= 'Valor pixel')
        self.widget_plot.setLabel(axis = 'left', text= 'Frecuencia')
        self.curve = self.widget_plot.plot([], pen=self.hcolor) #Ploteamos

        #Conectar botones
        self.actionCerrar.triggered.connect(self.Detener)
        self.comenzar.clicked.connect(self.loadImage)
        self.detener.clicked.connect(self.Detener)
        self.color.currentIndexChanged.connect(self.Color)
        self.barra.valueChanged.connect(self.Umbral)   

        #Esconder hasta presionar el botón comenzar
        self.detener.hide()
        self.label_4.hide()
        self.color.hide()
        self.label_5.hide()
        self.barra.hide()
        self.label_6.hide()

        #Definimos el inicio del video en falso
        self.started = False

        #Función por defecto
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    #Cargar imagenes
    def loadImage(self):
        #Mostramos los botones y el Qbox
        self.detener.show()
        self.label_4.show()
        self.color.show()
        if self.started:
            self.started = False
        else:
            self.started = True

        #Capturamos video con cv2
        vid = cv2.VideoCapture(0)

        #Es una especie de While True pero con la cámara
        while(vid.isOpened()):
            QtWidgets.QApplication.processEvents()
            img, self.image = vid.read() #Leemos el frame y lo ajustamos más abajo
            self.image = imutils.resize(self.image, height=480) 
            gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            #Tome esta parte del git que dejo el profesor
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
            )

            for (x,y,w,h) in faces:
                cv2.rectangle(self.image, (x,y), (x+w, y+h), (10,228,220), 5)
            
            #Update es la función donde vamos actualizando paso a paso la imagen
            self.update()
            key = cv2.waitKey(1) & 0xFF #Esperamos key pero la deje sin uso, debido a que, necesita funcionar con botones del QT
            if (self.started == False or key == ord('q')):
                break
    
    #Función para colocar la imagen en el QT
    def setPhoto(self, image, opc):
        self.tmp = image
        image = imutils.resize(image, width=640)   
        if(opc == 1): #Opción --> RGB
            image = QImage(self.rgb.data, self.width, self.height, 3*self.width, QtGui.QImage.Format_RGB888)
        elif(opc == 2): #Opción --> Grises
            image = QImage(self.gray.data, self.width, self.height, 1*self.width, QtGui.QImage.Format_Indexed8)
        else: #Opción --> Binario
            image = QImage(self.bw.data, self.width, self.height, 1*self.width, QtGui.QImage.Format_Indexed8) 
        self.FeedLabel.setPixmap(QtGui.QPixmap.fromImage(image)) #Mostramos en el QT

    #Función para elegir como se mostrará
    def Color(self):
        self.Plot_hist() #Ploteamos la opción
        #Creamos una condición donde se asigna una opción según el input del botón, está mostrará cuál widget se muestra según corresponde
        if (self.color.currentText() == 'RGB'):
            opc = 1
            self.label_5.hide()
            self.barra.hide()
            self.label_6.hide()
        elif(self.color.currentText() == 'Gris'):
            opc = 2
            self.label_5.hide()
            self.barra.hide()
            self.label_6.hide()
        elif(self.color.currentText() == 'Binario'):
            opc = 3
            self.label_5.show()
            self.barra.show()
            self.label_6.show()
        return opc

    #Función "Central" donde vamos asignando la mayoría de las variables
    def update(self):
        self.rgb = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB) #RGB
        self.gray = cv2.cvtColor(self.rgb, cv2.COLOR_RGB2GRAY) #Gris
        th = self.barra.value()
        ret, self.bw = cv2.threshold(self.gray, th, 255, cv2.THRESH_BINARY) #Binario
        self.height, self.width, self.channel = self.rgb.shape
        opcion = self.Color() #Tomamos la opción
        self.setPhoto(self.image, opcion) #Con todos los datos recolectados, la mandamos al setPhoto que posterior lo colocará en el QT
    
    #Actualizar umbral y label
    def Umbral(self):
        valorumbral= self.barra.value()
        self.label_6.setText(str(valorumbral))
    
    #Ploteamos el histograma para gris y Binario
    def Plot_hist(self):
        if(self.color.currentText() == 'Gris'): 
            for i in range(0,256):
                self.ejey[i] = (self.gray.ravel().tolist().count(i)/118491)
            self.curve.setData(self.ejex, self.ejey, pen=self.hcolor)
        elif(self.color.currentText() == 'Binario'):
            self.ejey= np.zeros(256)
            for p in [0,255]:
                self.ejey[p] = (self.bw.ravel().tolist().count(p)/118491)
            self.curve.setData(self.ejex, self.ejey, pen = self.hcolor)
        else:
            self.curve.setData([], []) 
    
    #Para Salir o cerrar el programa
    def Detener(self):
        sys.exit(app.exec_())

    

    #Función por defecto de la importación 
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Imagen"))
        self.label_3.setText(_translate("MainWindow", "Detección"))
        self.comenzar.setText(_translate("MainWindow", "Comenzar"))
        self.label_6.setText(_translate("MainWindow", "0"))
        self.color.setItemText(0, _translate("MainWindow", "RGB"))
        self.color.setItemText(1, _translate("MainWindow", "Gris"))
        self.color.setItemText(2, _translate("MainWindow", "Binario"))
        self.label_4.setText(_translate("MainWindow", "Color"))
        self.label_2.setText(_translate("MainWindow", "Histograma"))
        self.detener.setText(_translate("MainWindow", "Detener"))
        self.label_5.setText(_translate("MainWindow", "Umbral"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.actionCerrar.setText(_translate("MainWindow", "Cerrar"))


#Inicializar la ventana
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
