import numpy as np
import random

class Mancala:
    def __init__(self):
        self.turno = True
        self.puntaje1 = 0
        self.puntaje2 = 0
        self.tablero = np.full((2, 8), 4)
        self.finish = False

    def showTablero(self):
        print(self.tablero)

    def movimiento(self, tablero, tiro, valor):
        tableroNuevo = tablero
        cont = 0
        if(tiro > 0 and tiro < 7):
            while(cont < valor):
                cont +=1
                if(tiro+cont == 7):
                    print("punto")
                    self.puntaje1 += 1
                    tablero[1][tiro+cont] = tablero[1][tiro+cont]+1
                    tablero[0][tiro+cont] = tablero[0][tiro+cont]+1
                    tablero[1][tiro] = 0
                    
                elif(tiro+cont < 7):
                    tablero[1][tiro+cont] = tablero[1][tiro+cont]+1
                    tablero[1][tiro] = 0
                    
                elif(tiro+cont > 7):
                    tablero[0][6-(valor-cont)] = tablero[0][6-(valor-cont)]+1
                    tablero[1][tiro] = 0
                    
                if(cont == valor):
                    if(tiro+cont == 7):
                        print("me toca de nuevo")
                        self.turno = True
                    else:
                        print("no me toca de nuevo :(")
                        self.turno = False
        else:
            print("no puedes escoger ese valor")
            self.turno = True
        
        return tableroNuevo, self.turno

    def Iniciarjuego(self):
        #self.tablero = np.full((2, 8), 4)
        self.tablero = np.random.randint(4, size=(2, 8))
        self.tablero[0][0] = 0
        self.tablero[1][0] = 0
        self.tablero[0][7] = 0
        self.tablero[1][7] = 0
        print("Tablero")
        print(self.tablero)
        print("    1 2 3 4 5 6")

        while(self.finish == False and self.turno):
            
            tiro = int(input("Ingresa tu casilla: "))
            #print("En la posicion",tiro,"esta el valor",self.tablero[1][tiro])
            valor = self.tablero[1][tiro]
            #print("Me movere",valor,"veces")
            self.tablero, self.turno = self.movimiento(self.tablero,tiro,valor)
            print(self.tablero)
            print("    1 2 3 4 5 6")
                

juego = Mancala()
juego.Iniciarjuego()
# juego.showTablero()


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





