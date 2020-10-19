import numpy as np
import random

class Mancala:
    def __init__(self,iteraciones):
        self.turno = True
        self.puntaje1 = 0
        self.puntaje2 = 0
        self.pseudopuntaje = 0
        self.pseudopuntaje2 = 0
        self.tablero = np.full((2, 8), 4)
        self.finish = False
        #Variables para montecarlo
        self.iteraciones = iteraciones
        self.filtro = [] #Opciones disponibles a poder jugar
        self.filtro2 = []
        self.copia = self.tablero
        self.resultados = [] #Array donde se van a guardar los resultados de victorias
        self.totales = []
        # self.iteraciones = 0 #Cantidad de vueltas para monte carlo

    def showTablero(self):
        print(self.tablero)

    def movimiento(self, tablero, tiro, valor):
        tableroNuevo = tablero
        cont = 0
        contV = 0
        if(tiro > 0 and tiro < 7 and valor != 0):
            while(cont < valor):
                cont +=1
                #print("EL CONTADOR LLEVA",cont)
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
                    #print("QUE VALORES LLEVA ESTO",6-(valor-cont))
                    if(6-(valor-cont) > 0):
                        tablero[0][6-(valor-cont)] = tablero[0][6-(valor-cont)]+1
                        tablero[1][tiro] = 0
                    else:
                        tablero[1][contV+1] = tablero[1][contV+1]+1
                        contV +=1
                    
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
        contV = 0
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
                    #print(-(tiro-cont))
                    if(-(tiro-cont)<7):
                        tableroNuevo[1][-(tiro-cont)] = tableroNuevo[1][-(tiro-cont)]+1
                        tableroNuevo[0][tiro] = 0
                    else:
                        tableroNuevo[0][6-contV] = tableroNuevo[0][6-contV]+1
                        contV +=1
                    
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


    def pseudomovimiento(self, tablero, tiro, valor):
        tableroNuevo = tablero
        cont = 0
        contV = 0
        if(tiro > 0 and tiro < 7 and valor != 0):
            #print("Tablero: ",tablero," tiro ",tiro," valor: ",valor)
            while(cont < valor):
                cont +=1
                #print("EL CONTADOR LLEVA",cont)
                if(tiro+cont == 7):
                    self.pseudopuntaje1 += 1
                    tablero[1][tiro+cont] = tablero[1][tiro+cont]+1
                    tablero[0][tiro+cont] = tablero[0][tiro+cont]+1
                    tablero[1][tiro] = 0
                    
                elif(tiro+cont < 7):
                    tablero[1][tiro+cont] = tablero[1][tiro+cont]+1
                    tablero[1][tiro] = 0
                    
                elif(tiro+cont > 7):
                    #print("QUE VALORES LLEVA ESTO",6-(valor-cont))
                    if(6-(valor-cont) > 0):
                        tablero[0][6-(valor-cont)] = tablero[0][6-(valor-cont)]+1
                        tablero[1][tiro] = 0
                    else:
                        tablero[1][contV+1] = tablero[1][contV+1]+1
                        contV +=1
                    
                if(cont == valor):
                    if(tiro+cont == 7):
                        self.turno = True
                    else:
                        self.turno = False
        else:
            self.turno = True
        #print("finalizo pseudohumano")
        #print("Tablero",tablero)
        return tableroNuevo, self.turno

    def pseudomovimientoIA(self, tablero, tiro, valor):
        tableroNuevo = tablero
        cont = 0
        contV = 0
        if(tiro > 0 and tiro < 7 and valor != 0):
            #print("Entro el if al metodo pseudo")
            #print("Tablero: ",tablero," tiro ",tiro," valor: ",valor)
            # SI EL VALOR - TIRO ES 0 SE SUMA PUNTO
            while(cont < valor):
                cont +=1
                #print("El tiro menos el cont es",(tiro-cont))
                if(tiro-cont == 0):
                    
                    self.pseudopuntaje2 += 1
                    tableroNuevo[1][tiro-cont] = tableroNuevo[1][tiro-cont]+1
                    tableroNuevo[0][tiro-cont] = tableroNuevo[0][tiro-cont]+1
                    tableroNuevo[0][tiro] = 0
                    
                elif(tiro-cont > 0):
                    
                    tableroNuevo[0][tiro-cont] = tableroNuevo[0][tiro-cont]+1
                    tableroNuevo[0][tiro] = 0
                    
                elif(tiro-cont < 0):
                    #print(-(tiro-cont))
                    if(-(tiro-cont)<7):
                        tableroNuevo[1][-(tiro-cont)] = tableroNuevo[1][-(tiro-cont)]+1
                        tableroNuevo[0][tiro] = 0
                    else:
                        tableroNuevo[0][6-contV] = tableroNuevo[0][6-contV]+1
                        contV +=1
                    
                if(cont == valor):
                    if(tiro-cont == 0):
                        self.turno = False
                    else:
                        self.turno = True
                #print("Continua en el while del pseudo")
        else:
            self.turno = False
        #print("Finalizo IA")
        #print("Tablero",tablero)
        return tableroNuevo, self.turno

    def Iniciarjuego(self):
        self.tablero = np.full((2, 8), 4)
        #self.tablero = np.random.randint(4, size=(2, 8))
        self.tablero[0][0] = 0
        self.tablero[1][0] = 0
        self.tablero[0][7] = 0
        self.tablero[1][7] = 0
        #print("Tablero")
        #print(self.tablero)
        #print("    1 2 3 4 5 6")

        while(self.finish == False):
            self.finish = self.finalizar(self.tablero)
            if(self.finish):
                print("ENTRO AL BREAK GENERAL")
                break
            
            while(self.turno and self.finish == False):
                print(self.tablero)
                print("    1 2 3 4 5 6")
                tiro = int(input("Ingresa tu casilla: "))
                #print("En la posicion",tiro,"esta el valor",self.tablero[1][tiro])
                valor = self.tablero[1][tiro]
                #print("Me movere",valor,"veces")
                self.tablero, self.turno = self.movimiento(self.tablero,tiro,valor)
                
                self.finish = self.finalizar(self.tablero)
                if(self.finish):
                    print("ENTRO AL BREAK DEL HUMANO")
                    break
                
            while(self.turno == False and self.finish == False):
                print(self.tablero)
                print("    1 2 3 4 5 6")
                self.filtrado() #Obtener valor de casillas con valor
                
                tiro = self.simularJuego()
                print("-"*50)
                print(self.tablero)
                print("    1 2 3 4 5 6")
                print("-"*50)
                self.copia = self.tablero
                # tiro = random.randint(1,6)
                #print("En la posicion",tiro,"esta el valor",self.tablero[1][tiro])
                valor = self.tablero[0][tiro]
                
                #print("Me movere",valor,"veces")
                print("el tiro de la IA es",tiro)
                self.tablero, self.turno = self.movimientoIA(self.tablero,tiro,valor)
                
                self.finish = self.finalizar(self.tablero)
                print("/"*50)
                print(self.tablero)
                print("    1 2 3 4 5 6")
                print("/"*50)
                if(self.finish):
                    print("ENTRO AL BREAK DEL IA")
                    break
            
            
                

                
    def finalizar(self, tablero):
        bandera = False
        cerosH = np.count_nonzero(tablero[1,1:7])
        
        cerosIA = np.count_nonzero(tablero[0,1:7])
        #print("CEROSIA",cerosIA)
        #print("CEROSH",cerosH)
        if cerosH == 0 or cerosIA == 0:
            bandera = True
        #print(bandera)
        return bandera

    def pseudofinalizar(self):
        bandera = False
        cerosH = np.count_nonzero(self.copia[1,1:7])
        
        cerosIA = np.count_nonzero(self.copia[0,1:7])
        #print("CEROSIA",cerosIA)
        #print("CEROSH",cerosH)
        if cerosH == 0 or cerosIA == 0:
            bandera = True
        #print(bandera)
        return bandera
            
    #=========================== Montecarlo ==================================================
    # Metodo para filtrar posiciones donde hay fichas disponibles y se pueden realizar jugadas
    def filtrado(self):
        self.filtro = []
        for i in range(1,7):
            if(self.tablero[0][i] > 0):
                self.filtro.append(i)
        self.resultados = [0 for i in range(0,len(self.filtro))]
        self.totales = [0 for i in range(0,len(self.filtro))]
    
    def filtrado2(self):
        self.filtro2 = []
        for i in range(1,7):
            if(self.copia[1][i] > 0):
                self.filtro2.append(i)
    

    def simularJuego(self):
        if self.iteraciones == 0: #Noob
            noob = random.randint(0,len(self.filtro)-1)
            print(len(self.filtro),"largo")
            print (noob)
            print(self.filtro)
            return self.filtro[noob]
        else:
            for i in range(0,self.iteraciones):
                #print("Entro al For y es la vuelta ",i)
                indice = random.randint(0,len(self.filtro)-1)
                #print("Indice ",indice)
                self.totales[indice] = self.totales[indice] + 1
                jugadaInicial = self.filtro[indice]
                tiro = jugadaInicial
                valor = self.copia[0][jugadaInicial]
                self.pseudopuntaje1 = self.puntaje1
                self.pseudopuntaje2 = self.puntaje2
                pseudofinish = False
                
                while(pseudofinish == False):
                    ### PONER LOGICA DEL JUEGO AQUI
                    pseudofinish = self.pseudofinalizar()
                    if(pseudofinish):
                        #print("ENTRO AL BREAK GENERAL")
                        break
            
                    while(self.turno == False and pseudofinish == False):
                        self.copia, self.turno = self.pseudomovimientoIA(self.copia,tiro,self.copia[0][tiro])
                        tiro = random.randint(1,6)
                        pseudofinish = self.pseudofinalizar()
                        if(pseudofinish):
                            #print("ENTRO AL BREAK DEL IA")
                            break

                    while(self.turno and pseudofinish == False):
                        tiro = random.randint(1,6)
                        self.copia, self.turno =  self.pseudomovimiento(self.copia,tiro,self.copia[1][tiro])
                        pseudofinish = self.pseudofinalizar()
                        if(pseudofinish):
                            #print("ENTRO AL BREAK DEL HUMANO")
                            break


                    #Condicion de cuando termine la partida
                    #pseudofinish = self.pseudofinalizar()
                    tiro = random.randint(1,6)
                #Validar quien gano o no
                #Si gana la maquina le suma un punto al array de resultados
                if(self.pseudopuntaje2 > self.pseudopuntaje1):
                    self.resultados[indice] += 1
                else:
                    self.resultados[indice] += 0
                #print("aun no finaliza")
            #Se compara quien fue el mejor resultado entre todos
            print("Filtros: "+str(self.filtro))
            print("Resultados: "+str(self.resultados))
            valorelegir = []
            for j in range(0,len(self.resultados)):
                promedio =  self.resultados[j]/self.totales[j]
                valorelegir.append(promedio)
            print("Valor a elegir"+str(valorelegir))
            #Obtener cual fue el mejor promedio para elegir jugada
            tironuevo = valorelegir.index(max(valorelegir))
            self.turno = False
            return self.filtro[tironuevo]
                    
                


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
            iteraciones = 100
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





