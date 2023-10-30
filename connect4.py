def creadorTablero():

    contador=1
    tablero=[]

    while contador<=6:
        tablero.append([0,0,0,0,0,0,0])
        contador+=1
    return(tablero)

def escogerTurno():

    primeravez=True
    turno = True
    posicion = ""

    while turno:

        if primeravez:
            posicion = input("Escoja una posicion del tablero: ")
            primeravez = False
        else:
            posicion = input("Escoja una posicion valida: ")
        if posicion in ["1","2","3","4","5","6","7"]:
            turno = False
    
    return(int(posicion)-1)
        
def ponerFicha(turno,tablero,jugador):

    contador = 0

    while True:
        if tablero[contador][turno] == 0 and contador<=5:
            tablero[contador][turno] = jugador
            return(tablero)
        elif contador<=4: 
            contador += 1
        else: 
            print("Escoge una posicion valida la posicion esta llena")
            turno = escogerTurno()
            contador = 0

def revisarVictoria(tablero,jugador):
    
    def hacerFila(tablero):

        TableroHorizontal = []
        
        for element in tablero:
            for elemento in element:
                TableroHorizontal.append(elemento)
        
        def vertical(TableroHorizontal):
            
            TableroVertical = []

            contador1 = 0

            while contador1<=6:
                contador2 = 0

                while contador2<=5:

                    TableroVertical.append(TableroHorizontal[contador1+(7*contador2)])
                    contador2 += 1
                
                contador1 += 1
            
            return(TableroVertical)
        
        return([TableroHorizontal,vertical(TableroHorizontal)])

    
    def victoria(filaTablero,modulo):

        contadorVictoria = 0
        indice = 0

        for element in filaTablero:

            if indice % modulo == 0:
                contadorVictoria = 0

            if int(element) == jugador:
            
                contadorVictoria += 1

                if contadorVictoria == 4:
                    print("Ganaste")
                    return(True)

            else:
                contadorVictoria = 0
            indice += 1
    
        return(False)
    
    def victoriaDiagonal(tablero):
        
        for i in range(0,21):

            if i % 7 > 2:
                if tablero[i] == tablero[i+6] == tablero [i+12] == tablero[i+18]  == jugador:
                    return(True)
                
            if i % 7 < 3:
                if tablero[i] == tablero[i+8] == tablero [i+16] == tablero[i+24]  == jugador:
                    return(True)







    tablero=hacerFila(tablero)
    tableroHorizontal=tablero[0]
    tableroVertical=tablero[1]

    if victoria(tableroHorizontal,7):
        return(True)

    if victoria(tableroVertical,6):
        return(True)
    
    if victoriaDiagonal(tableroHorizontal):
        return(True)



    return(False)
    

def main ():
    
    tablero = creadorTablero()
    jugador = 0
    victoria = False

    while not victoria:

        if jugador % 2 == 0:
            tablero = ponerFicha(escogerTurno(),tablero,1) 
            
            if revisarVictoria(tablero,1):
                victoria = True
                print("Gano jugador 1")

        else:
            tablero = ponerFicha(escogerTurno(),tablero,2) 
            
            if revisarVictoria(tablero,2):
                victoria = True
                print("Gano jugador 2")

        jugador += 1

        for element in tablero:
            print (element)





main()