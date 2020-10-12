import numpy as np

# matriz de 7 x 2
# 0 3 1 4 2 6 0
# 0 2 3 1 3 5 0
#   1 2 3 4 5

# pedir posicion
# obtenemos el valor de la posicion

# (Jugador abajo) 4 - (2,4) -> (2,5) -> (2,6) -> (1,6) - (1,5)

# (Jugador arriba) 1 - (1,0) -> (2,0) -> (2,1) -> (2,2) 


#   Abajo va sumando en j y cuando llega a posicion 6 resta i y va restando j

#   Arriba va restando en j y cuando llega a posicion 0 suma i y va sumando j

#   Cambio de turno

#   Contador de puntos

#   Revisar que casilla a colocar no esté vacia

#   Para cada turno de la PC se hace el ciclo de n iteraciones para calcular la mejor opcion
#   Para seleccionar el mejor, division de:
#        (exitos de la casilla seleccionada / cantidad de veces de esa casilla)





