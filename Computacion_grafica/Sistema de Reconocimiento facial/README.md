## Instrucciones

Se solicita implementar una interfaz gráfica que permita visualizar y procesar digitalmente imágenes de video para la detección de rostros. La interfaz gráfica debe
realizar lo siguiente:
* Capturar imágenes RGB (Red, Green, Blue) desde una cámara (por ejemplo, webcam).
* Reajustar el tamaño de la imagen a un determinado número de FILAS (F) y COLUMNAS (C).
* Seleccionar el tipo de imagen a visualizar (RGB, escala de grises o binaria) mediante un QComboBox. En el caso de la imagen binaria, deberá utilizar un umbral ajustable mediante un QSlider.
* Aplicar un detector de rostros en la imagen actual utilizando las herramientas disponibles de las bibliotecas de Python.
* Mostrar el histograma actual de la imagen gris o binaria.
* Cerrar el programa desde la barra de menú.
