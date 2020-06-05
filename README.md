# bingo [![Build Status](https://travis-ci.com/UberSquid/bingo.svg?branch=master)](https://travis-ci.com/UberSquid/bingo)
Este es un proyecto escolar y esta programado en python 
Genera cartones validos de bingo pero no esta capacitado para generar una tira completa para 6 cartones
Si bien genera cartones, no lo hace de la manera mas eficiente, ya que utilizamos un algoritmo de otro proyecto pero en php.
El carton es generado aleatoriamente por lo que puede que al algoritmo le lleve 50 intentos generar un carton o 2000 
El proyecto cuenta con travis para realizar tests automatizados y validar los cartones generados
Donde las reglas del carton son: 
- Los números del carton se encuentran en el rango 1 a 90.
- Cada columna de un carton (contando de izquierda a derecha) contiene numeros que van del 1 al 9, 10 al 19, 20 al 29 ..., 70 al 79 y 80 al 90.
- No hay números repetidos en el carton.
- Cada fila de un carton tiene exactamente 5 celdas ocupadas.
- Cada carton es una matrix de 3 x 9.
- Cada carton tiene 15 celdas ocupadas.
- Los números de las columnas izquierdas son menores que los de las columnas a la derecha.
- Para una misma columna, sus números están ordenados de menor a mayor de arriba hacia abajo.
- No pueden existir columnas vacias.
- No pueden existir columnas con sus tres celdas ocupadas.
- Cada carton debe tener 3 y solo 3 columas con solo una celda ocupada.
- En una fila no existen más de dos celdas vacías consecutivas.
- En una fila no existen más de dos celdas ocupadas consecutivas.

