def creadorTablero(): 
    #Crea una matriz con las casillas del juego
    contador=1
    tablero=[]

    while contador<=6:
        tablero.append([0,0,0,0,0,0,0])
        contador+=1
    return(tablero)



'''def escogerTurno():

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
    
    return(int(posicion)-1)     '''

'''def escoger_turno_graficos():

    while True:
        
        mouse_pos=pygame.mouse.get_pos() #Dupla con las cordenadas x y y del mouse 
        x = mouse_pos[0]//100 #Sector de el tablero en el que 
        if pygame.mouse.get_pressed(3)[0]: #boolean Si el mouse esta presionado
            
            return(x)'''
        
'''def ponerFichaPreBETA(turno,tablero,jugador):

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
            contador = 0'''

def ponerFicha(turno,tablero,jugador):

    contador = 0
    
    while True:

        if tablero[contador][turno] == 0 and contador<=5:
            tablero[contador][turno] = jugador
            return(tablero)
        elif contador<=4: 
            contador += 1
        else: #Arreglar la excepcion para que no explote
            return(tablero)


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

'''def Juego ():
    
    tablero = creadorTablero()
    jugador = 0
    victoria = False

    while not victoria:

        if jugador % 2 == 0:
            tablero = ponerFicha(escoger_turno_graficos(),tablero,1) 
            
            if revisarVictoria(tablero,1):
                victoria = True
                print("Gano jugador 1")

        else:
            tablero = ponerFicha(escoger_turno_graficos(),tablero,2) 
            
            if revisarVictoria(tablero,2):
                victoria = True
                print("Gano jugador 2")

        jugador += 1

        for element in tablero:
            print (element)'''

#Recursos graficos (pygames)
import pygame ,sys
from pygame.locals import *                 


#Colores basicos 

BLANCO=(255,255,255)
NEGRO=(0,0,0)
ROJO=(255,0,0)
AZUL=(0,0,255)
VERDE=(0,255,0)

#colores Paleta 1

PALETA1_COLOR1=(151,137,184)
PALETA1_JUGADOR1=(240,166,202)
PALETA1_COLOR3=(139,195,230)
PALETA1_COLOR4=(240,230,239)
PALETA1_JUGADOR2=(184,190,221)

#colores Paleta 2

PALETA2_COLOR1=(255,172,129)
PALETA2_JUGADOR1=(255,146,139)
PALETA2_COLOR3=(254,195,166)
PALETA2_COLOR4=(239,233,174)
PALETA2_JUGADOR2=(205,239,192)


def cuadricula(tamaño):
    contador=tamaño
    while contador<=600:
        pygame.draw.line(PANTALLA, NEGRO,(contador, 100),(contador, 700),1)
        contador+=tamaño
    contador=tamaño
    while contador<=700:
        pygame.draw.line(PANTALLA, NEGRO,(0, contador),(700,contador),1)
        contador+=tamaño 



#Elegir color jugador
def escogerColor():

    primeravez=True
    turno = True
    paleta = ""

    while turno:

        if primeravez:
            paleta = input("Escoja una paleta de colores: ")
            primeravez = False
        else:
            paleta = input("Escoja una paleta valida: ")
        if paleta in ["1","2","3"]:
            turno = False
    
    return(int(paleta)) 

paleta=escogerColor()

if paleta == 1:
    jug_1=PALETA1_JUGADOR1
    jug_2=PALETA1_JUGADOR2

elif paleta == 2:
    jug_1=PALETA2_JUGADOR1
    jug_2=PALETA2_JUGADOR2    

else:
    jug_1=ROJO
    jug_2=AZUL

pygame.init()
PANTALLA= pygame.display.set_mode((700,700))
pygame.display.set_caption('Conecta 4')

victoria = False
tablero = creadorTablero()
jugador = 0
while not victoria:

    presionado=pygame.mouse.get_pressed(3)[0] #boolean Si el mouse esta presionado
    mouse_pos=pygame.mouse.get_pos() #Dupla con las cordenadas x y y del mouse 
    x = mouse_pos[0]//100 #Sector de el tablero en el que esta
    centroCirculo=((x*100)+50) #Coord x de el centro de la circunferencia 
    
    #Poner linda la pantalla (Cambiar despues)
    PANTALLA.fill(BLANCO)
    cuadricula(100)
    pygame.event.wait()

    #Dibujar circulo en la posicion del mouse (falta completar bien )
    if jugador % 2 ==0:
        pygame.draw.circle(PANTALLA,jug_1,(centroCirculo,50),50,15)
    else:
        pygame.draw.circle(PANTALLA,jug_2,(centroCirculo,50),50,15)

    #Protoripo:

    if jugador % 2 == 0 and presionado:
        tablero = ponerFicha(x,tablero,1) 
        jugador += 1
        if revisarVictoria(tablero,1):
            victoria = True
            print("Gano jugador 1")
            
    elif presionado:
        tablero = ponerFicha(x,tablero,2) 
        jugador += 1
        if revisarVictoria(tablero,2):
            victoria = True
            print("Gano jugador 2")
    
    # dibujar las circunferencias de la matriz
    coordX=50
    coordY=650
    for fila in tablero:
        coordX=50
        for elemento in fila:
            if elemento!=0:
                if elemento==1:
                    pygame.draw.circle(PANTALLA,jug_1,(coordX,coordY),50,15)
                elif elemento==2:
                    pygame.draw.circle(PANTALLA,jug_2,(coordX,coordY),50,15)    
            coordX+=100
        coordY-=100

    for element in tablero:
        print (element)

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit() 
            sys.exit   
