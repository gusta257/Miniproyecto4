import numpy as np
import random

class Mancala:
    def __init__(self,iteraciones):
        self.turno = True
        self.puntaje1 = 0
        self.puntaje2 = 0
        self.tablero = np.full((2, 8), 4)
        self.finish = False
        #Variables para montecarlo
        self.iteraciones = iteraciones
        self.filtro = [] #Opciones disponibles a poder jugar
        self.copia = self.tablero
        self.resultados = [] #Array donde se van a guardar los resultados de victorias
        self.iteraciones = 0 #Cantidad de vueltas para monte carlo

    def showTablero(self):
        print(self.tablero)

    def movimiento(self, tablero, tiro, valor):
        tableroNuevo = tablero
        cont = 0
        if(tiro > 0 and tiro < 7 and valor != 0):
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
                        print("Turno Humano")
                        self.turno = True
                    else:
                        print("Turno IA")
                        self.turno = False
        else:
            print("no puedes escoger ese valor")
            self.turno = True
        print("*"*50)
        return tableroNuevo, self.turno

    def movimientoIA(self, tablero, tiro, valor):
        tableroNuevo = tablero
        cont = 0
        if(tiro > 0 and tiro < 7 and valor != 0):
            # SI EL VALOR - TIRO ES 0 SE SUMA PUNTO
            while(cont < valor):
                cont +=1
                #print("El tiro menos el cont es",(tiro-cont))
                if(tiro-cont == 0):
                    
                    self.puntaje2 += 1
                    tableroNuevo[1][tiro-cont] = tableroNuevo[1][tiro-cont]+1
                    tableroNuevo[0][tiro-cont] = tableroNuevo[0][tiro-cont]+1
                    tableroNuevo[0][tiro] = 0
                    
                elif(tiro-cont > 0):
                    
                    tableroNuevo[0][tiro-cont] = tableroNuevo[0][tiro-cont]+1
                    tableroNuevo[0][tiro] = 0
                    
                elif(tiro-cont < 0):
                    tableroNuevo[1][-(tiro-cont)] = tableroNuevo[1][-(tiro-cont)]+1
                    tableroNuevo[0][tiro] = 0
                    
                if(cont == valor):
                    if(tiro-cont == 0):
                        print("Turno IA")
                        self.turno = False
                    else:
                        print("Turno Jugador")
                        self.turno = True
        else:
            print("no puedes escoger ese valor")
            self.turno = False
        print("*"*50)
        return tableroNuevo, self.turno

    def Iniciarjuego(self):
        self.tablero = np.full((2, 8), 4)
        #self.tablero = np.random.randint(4, size=(2, 8))
        self.tablero[0][0] = 0
        self.tablero[1][0] = 0
        self.tablero[0][7] = 0
        self.tablero[1][7] = 0
        print("Tablero")
        print(self.tablero)
        print("    1 2 3 4 5 6")

        while(self.finish == False):
            while(self.turno):
                
                tiro = int(input("Ingresa tu casilla: "))
                #print("En la posicion",tiro,"esta el valor",self.tablero[1][tiro])
                valor = self.tablero[1][tiro]
                #print("Me movere",valor,"veces")
                self.tablero, self.turno = self.movimiento(self.tablero,tiro,valor)
                print(self.tablero)
                print("    1 2 3 4 5 6")
                
            while(self.turno == False):
                tiro = random.randint(1,6)
                #print("En la posicion",tiro,"esta el valor",self.tablero[1][tiro])
                valor = self.tablero[0][tiro]
                #print("Me movere",valor,"veces")
                print("el tiro de la IA es",tiro)
                self.tablero, self.turno = self.movimientoIA(self.tablero,tiro,valor)
                print(self.tablero)
                print("    1 2 3 4 5 6")
                

                
    #=========================== Montecarlo ==================================================
    # Metodo para filtrar posiciones donde hay fichas disponibles y se pueden realizar jugadas
    def filtrado(self):
        for i in range(1,7):
            if(self.tablero[0][i] > 0):
                self.filtro.append(i)
        self.resultados = [0 for i in range()]
        
    def simularJuego(self):
        if self.iteraciones == 0: #Noob
            return random.randint(0,len(self.filtro))
        else:
            jugadaInicial = self.filtro[random.randint(0,len(self.filtro))]
            #for i in range(0,self.iteraciones):
                ### PONER LOGICA DEL JUEGO AQUI

x = True
iteraciones = 0
while x:
    print(""" 
        Noob        => 1\n
        Avanzado    => 2\n
        Pro         => 3\n 
    """)
    op = int(input('¿Que nivel desea la IA? \n'))
    if(op > 3 or op<1):
        print("Debe ingresar un valor entre 1 y 3")
    else:
        if op == 1:
            iteraciones = 0
        elif op == 2:
            iteraciones = 500
        elif op == 3:
            iteraciones = 10000
        x = False
        


juego = Mancala(iteraciones)
juego.Iniciarjuego()

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





