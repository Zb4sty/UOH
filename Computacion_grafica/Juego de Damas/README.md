## Instrucciones

Se solicita implementar una GUI que permita visualizar e implementar parcialmente el juego “damas”. La interfaz gráfica debe realizar lo siguiente:

* Dibujar líneas horizontales y verticales que dividan la escena en 8x8 cuadrículas, coloreando el tablero con el patrón correspondiente al juego.
* Dibujar círculos con colores diferenciados para cada jugador (usuario y oponente).
* Permitir el desplazamiento por teclado por cada una de las cuadrículas del tablero (tecla arriba, abajo, izquierda, derecha) para seleccionar la pieza y hacia donde se moverá (barra espaciadora). Esta jugada representa al usuario para lo cual deberá:
  1. Posicionarse en la pieza del usuario a mover
  2. Confirmar con la barra espaciadora
  3. Posicionarse en el lugar donde se moverá la pieza del usuario
  4. Confirmar con la barra espaciadora. En esta jugada, se debe actualizar el tablero
  Los posicionamientos en el tablero en la forma de cuadrícula deben indicarse con algún color distintivo.
* Una vez realizada la jugada del usuario, se da paso al jugador oponente mediante un botón. Para esto, el programa automáticamente debe mover al azar una de las piezas del jugador oponente.
* Indicar con un mensaje emergente si el ganador fue el jugador usuario o el oponente. El juego termina si una de las piezas llega a la primera fila del otro jugador.
* Reiniciar el juego con un botón.

## Reglas
Todos los movimientos de piezas deben cumplir las siguientes reglas:
* Solo se permiten movimientos hacia adelante (respecto del jugador) y hacia una diagonal derecha o izquierda.
* Los movimientos solo se permiten, dentro de los límites del tablero, si no hay una pieza del mismo jugador en la nueva posición. Si hay una pieza del otro jugador en la nueva posición, se podrá saltar sobre ella para llegar a la posición siguiente a ésta. Este proceso se puede repetir tantas veces como piezas hayan en el camino (diagonales), eliminando en este proceso las piezas del otro jugador.


