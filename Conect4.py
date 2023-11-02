import pygame ,sys
from pygame.locals import *

pygame.init()
PANTALLA= pygame.display.set_mode((700,700))
pygame.display.set_caption('Conecta 4')


BLANCO=(255,255,255)
NEGRO=(0,0,0)
ROJO=(255,0,0)
AZUL=(0,0,255)
VERDE=(0,255,0)

def creadorTablero():
    contador=1
    tablero=[]

    while contador<=6:
        tablero.append([0,0,0,0,0,0,0])
        contador+=1
    return(tablero)

def cuadricula(tamaño):
    contador=tamaño
    while contador<=600:
        pygame.draw.line(PANTALLA, NEGRO,(contador, 100),(contador, 700),1)
        contador+=tamaño
    contador=tamaño
    while contador<=700:
        pygame.draw.line(PANTALLA, NEGRO,(0, contador),(700,contador),1)
        contador+=tamaño 

def revisarVictoria(matriz,jugador):
    contador=0
    for fila in matriz:
        contador=0
        for element in fila:  
            if element==jugador:
                contador+=1
            elif contador<4:
                contador=0
        if contador>=4:
            return(int(jugador))
    return(0)

def voltearMatriz(matriz):
    contador=0
    nuevaMatriz=[]
    while(contador<len(matriz[1])):
        output=[]
        for element in matriz:
            output+=[element[contador]]
        contador+=1
        nuevaMatriz.append(output)
    return(nuevaMatriz)

def revisarVictoriaHorizontal(matriz,jugador):
    matriz=voltearMatriz(matriz)
    return(revisarVictoria(matriz,jugador))

def diagonalesMatrices1(matriz):
    nuevaMatriz=[]
    lista=[matriz[0][6],3,3,3,3,3]
    nuevaMatriz.append(lista)
    lista=[matriz[0][5],matriz[1][6],3,3,3,3]
    nuevaMatriz.append(lista)
    lista=[matriz[0][4],matriz[1][5],matriz[2][6],3,3,3]
    nuevaMatriz.append(lista)
    lista=[matriz[0][3],matriz[1][4],matriz[2][5],matriz[3][6],3,3]
    nuevaMatriz.append(lista)
    lista=[matriz[0][2],matriz[1][3],matriz[2][4],matriz[3][5],matriz[4][6],3]
    nuevaMatriz.append(lista)
    lista=[matriz[0][1],matriz[1][2],matriz[2][3],matriz[3][4],matriz[4][5],matriz[5][6]]
    nuevaMatriz.append(lista)
    lista=[matriz[0][0],matriz[1][1],matriz[2][2],matriz[3][3],matriz[4][4],matriz[5][5]]
    nuevaMatriz.append(lista)
    lista=[matriz[1][0],matriz[2][1],matriz[3][2],matriz[4][3],matriz[5][4],3]
    nuevaMatriz.append(lista)
    lista=[matriz[2][0],matriz[3][1],matriz[4][2],matriz[5][3],3,3]
    nuevaMatriz.append(lista)
    lista=[matriz[3][0],matriz[4][1],matriz[5][2],3,3,3]
    nuevaMatriz.append(lista)
    lista=[matriz[4][0],matriz[5][1],3,3,3,3]
    nuevaMatriz.append(lista)
    lista=[matriz[5][0],3,3,3,3,3]
    return(nuevaMatriz)


def diagonalesMatrices2(matriz):
    nuevaMatriz=[]
    lista=[matriz[5][6],3,3,3,3,3]
    nuevaMatriz.append(lista)
    lista=[matriz[5][5],matriz[4][6],3,3,3,3]
    nuevaMatriz.append(lista)
    lista=[matriz[5][4],matriz[4][5],matriz[3][6],3,3,3]
    nuevaMatriz.append(lista)
    lista=[matriz[5][3],matriz[4][4],matriz[3][5],matriz[2][6],3,3]
    nuevaMatriz.append(lista)
    lista=[matriz[5][2],matriz[4][3],matriz[3][4],matriz[2][5],matriz[1][6],3]
    nuevaMatriz.append(lista)
    lista=[matriz[5][1],matriz[4][2],matriz[3][3],matriz[2][4],matriz[1][5],matriz[0][6]]
    nuevaMatriz.append(lista)
    lista=[matriz[5][0],matriz[4][1],matriz[3][2],matriz[2][3],matriz[1][4],matriz[0][5]]
    nuevaMatriz.append(lista)
    lista=[matriz[4][0],matriz[3][1],matriz[2][2],matriz[1][3],matriz[0][4],3]
    nuevaMatriz.append(lista)
    lista=[matriz[3][0],matriz[2][1],matriz[1][2],matriz[0][3],3,3]
    nuevaMatriz.append(lista)
    lista=[matriz[2][0],matriz[1][1],matriz[0][2],3,3,3]
    nuevaMatriz.append(lista)
    lista=[matriz[1][0],matriz[0][1],3,3,3,3]
    nuevaMatriz.append(lista)
    lista=[matriz[1][0],3,3,3,3,3]
    return(nuevaMatriz)


def revisarVictoriaDiagonal1(matriz,jugador):
    matriz=diagonalesMatrices1(matriz)
    return(revisarVictoria(matriz,jugador))

def revisarVictoriaDiagonal2(matriz,jugador):
    matriz=diagonalesMatrices2(matriz)
    return(revisarVictoria(matriz,jugador))

contador=0
turno=0
tablero=creadorTablero()
victoria=False

while True:
    while victoria==False:  
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit    

        presionado=pygame.mouse.get_pressed(3)[0]
        mouse_pos=pygame.mouse.get_pos()
        x = mouse_pos[0]//100
        centroCirculo=((x*100)+50)

        PANTALLA.fill(BLANCO)
        cuadricula(100)
        pygame.event.wait()
        if presionado==True:
            turno+=1

        if presionado==True:
            flag=False
            contador=0
            while flag==False:
                if tablero[contador][x]==0:
                    tablero[contador][x]=(turno%2)+1
                    flag=True
                    print(tablero)

                elif contador<6: 
                    contador+=1
                    
        if turno%2==0:
            color=ROJO
        else:
            color=AZUL    

        pygame.draw.circle(PANTALLA,color,(centroCirculo,50),50,15)
        
        coordX=50
        coordY=650
        for fila in tablero:
            coordX=50
            for elemento in fila:
                if elemento!=0:
                    if elemento==2:
                        pygame.draw.circle(PANTALLA,ROJO,(coordX,coordY),50,15)
                    elif elemento==1:
                        pygame.draw.circle(PANTALLA,AZUL,(coordX,coordY),50,15)    
                coordX+=100
            coordY-=100

            if revisarVictoria(tablero,2)==2:
                print("gano jugador 1")
                victoria=True
            if revisarVictoria(tablero,1)==1:
                print("gano jugador 2")
                victoria=True
            if revisarVictoriaHorizontal(tablero,2)==2:
                print("gano jugador 1")
                victoria=True
            if revisarVictoriaHorizontal(tablero,1)==1:
                print("gano jugador 2")
                victoria=True
            if revisarVictoriaDiagonal1(tablero,2)==2:
                print("gano jugador 1")
                victoria=True
            if revisarVictoriaDiagonal1(tablero,1)==1:
                print("gano jugador 2")
                victoria=True
            if revisarVictoriaDiagonal2(tablero,2)==2:
                print("gano jugador 1")
                victoria=True
            if revisarVictoriaDiagonal2(tablero,1)==1:
                print("gano jugador 2")
                victoria=True



        pygame.display.update()
    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit   

