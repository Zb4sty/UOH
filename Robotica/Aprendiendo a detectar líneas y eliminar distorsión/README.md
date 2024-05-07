**Objetivos:**

1. **Detección de Líneas usando Transformada de Hough:**
   - Implementar un sistema de detección de bordes, preferiblemente utilizando el detector de Canny de OpenCV o alternativas como el detector de Sobel.
   - Desarrollar un sistema de detección de líneas rectas utilizando la Transformada de Hough para validar la pertenencia de los candidatos encontrados en el paso anterior.
   - Realizar la cuantización adecuada de los parámetros para garantizar el correcto funcionamiento de la Transformada de Hough.
   - Visualizar las líneas detectadas por la Transformada de Hough sobre la imagen original para su posterior análisis.

2. **Calibración de Cámara utilizando Tablero de Ajedrez:**
   - Definir las coordenadas del mundo real de los puntos 3D utilizando un patrón de tablero de ajedrez conocido, como el patrón de 9x6.
   - Cargar las imágenes proporcionadas con diferentes puntos de vista del tablero de control.
   - Utilizar métodos disponibles en OpenCV para encontrar las coordenadas de píxeles (u, v) para cada punto 3D en las imágenes proporcionadas.
   - Aplicar métodos disponibles en OpenCV para calcular los parámetros intrínsecos y extrínsecos de la cámara, incluyendo la Camera Matrix, coeficiente de distorsión, vector de rotación y vector de traslación.
   - Reportar los resultados obtenidos de la calibración de la cámara.

3. **Detectando las vías de la ciudad:**
   - Generar un detector de líneas de carril utilizando exclusivamente técnicas de procesamiento de imágenes.
   - Filtrar los colores de interés en la imagen utilizando un espacio de color arbitrario.
   - Aplicar operaciones morfológicas, como erosión y dilatación, sobre la imagen binarizada.
   - Detectar los bordes de la imagen utilizando un método de detección preferido.
   - Detectar las líneas de las vías utilizando los bordes de la imagen.
   - Dibujar las vías resultantes sobre la imagen original para su posterior análisis y visualización.
