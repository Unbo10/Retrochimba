
#Recursos graficos (pygames)
import pygame ,sys
from pygame.locals import *                 
#importar random
import random

def conecta4():

    def ida_de_olla(paleta,mapa,modo):
    
        def creadorTablero(): 
            #Crea una matriz con las casillas del juego
            contador=1
            tablero=[]
        
            while contador<=6:
                tablero.append([0,0,0,0,0,0,0])
                contador+=1
            return(tablero)
        
        def ponerFicha(jugada,tablero,jugador,turno):
        
            contador = 0
            
            while True:
            
                if tablero[contador][jugada] == 0 and contador<=5:
                    tablero[contador][jugada] = jugador
                    return([tablero,turno+1])
                elif contador<=4: 
                    contador += 1
                else: #Arreglar la excepcion para que no explote *Gracias Huertas del pasado, ya lo arregle)
                    return([tablero,turno])
        
        
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
        
    
        
        #Colores basicos 
        
        BLANCO=(255,255,255)
        NEGRO=(0,0,0)
        ROJO=(255,0,0)
        AZUL=(0,0,255)
        VERDE=(0,255,0)
        MORADO=(100,40,200)
        
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
        
        
        def cuadricula(tamaño,color=BLANCO):
            tablero=pygame.draw.rect(PANTALLA,color,(0,100,700,600))
            contador=tamaño
            while contador<=600:
                pygame.draw.line(PANTALLA, NEGRO,(contador, 100),(contador, 700),1)
                contador+=tamaño
            contador=tamaño
            while contador<=700:
                pygame.draw.line(PANTALLA, NEGRO,(0, contador),(700,contador),1)
                contador+=tamaño 
        
        def cuadricula2(color,color2):
            tablero=pygame.draw.rect(PANTALLA,color,(0,100,700,600))
            centroCircuferenciaX=50
            centroCircuferenciaY=150
            for j in range(0,7):
                for i in range (0,8):
                    circulo=pygame.draw.circle(PANTALLA,color2,(centroCircuferenciaX,centroCircuferenciaY),45)
                    centroCircuferenciaX+=100
                centroCircuferenciaY+=100
                centroCircuferenciaX=50
        
        if paleta == 1:
            jug_1=PALETA1_JUGADOR1
            jug_2=PALETA1_JUGADOR2
            col_tab=PALETA1_COLOR1
        
        elif paleta == 2:
            jug_1=PALETA2_JUGADOR1
            jug_2=PALETA2_JUGADOR2    
            col_tab=PALETA2_COLOR1
        
        else:
            jug_1=ROJO
            jug_2=AZUL
            col_tab=NEGRO
        
        pygame.init()
        PANTALLA= pygame.display.set_mode((700,700))
        pygame.display.set_caption('Conecta 4')
        
        victoria = False
        tablero = creadorTablero()
        jugador = 0
        ganador = 0
        
        #Modo 2 jugadores
    
        while True:
        
            if modo == 2:
                while not victoria:
                
                    presionado=pygame.mouse.get_pressed(3)[0] #boolean Si el mouse esta presionado
                    mouse_pos=pygame.mouse.get_pos() #Dupla con las cordenadas x y y del mouse 
                    x = mouse_pos[0]//100 #Sector de el tablero en el que esta
                    centroCirculo=((x*100)+50) #Coord x de el centro de la circunferencia 
    
                    #Poner linda la pantalla (Cambiar despues)
                    PANTALLA.fill(BLANCO)
                    if mapa == 1:
                        cuadricula(100)
                        ficha1=50
                        ficha2=15
                    elif mapa == 2:
                        cuadricula2(col_tab,BLANCO)
                        ficha1=45
                        ficha2=0
                    
    
                    #Dibujar circulo en la posicion del mouse (falta completar bien )
                    if jugador % 2 ==0:
                        pygame.draw.circle(PANTALLA,jug_1,(centroCirculo,50),ficha1,ficha2)
                    else:
                        pygame.draw.circle(PANTALLA,jug_2,(centroCirculo,50),ficha1,ficha2)
                    
                    pygame.event.wait()


    
                    #Protoripo:
    
                    if jugador % 2 == 0 and presionado:
                        dupla = ponerFicha(x,tablero,1,jugador) 
                        tablero = dupla[0]
                        jugador = dupla [1]
                        if revisarVictoria(tablero,1):
                            ganador = 1
                            victoria = True
                            print("Ganó jugador 1")
    
                    elif presionado:
                        dupla = ponerFicha(x,tablero,2,jugador) 
                        tablero = dupla[0]
                        jugador = dupla [1]
                        if revisarVictoria(tablero,2):
                            ganador = 2
                            victoria = True
                            print("Ganó jugador 2")
    
                    if jugador>=42: #42
                        victoria = True
                        print('Empate')
    
    
    
                    # Dibujar las circunferencias de la matriz
                    coordX=50
                    coordY=650
                    for fila in tablero:
                        coordX=50
                        for elemento in fila:
                            if elemento!=0:
                                if elemento==1:
                                    pygame.draw.circle(PANTALLA,jug_1,(coordX,coordY),ficha1,ficha2)
                                elif elemento==2:
                                    pygame.draw.circle(PANTALLA,jug_2,(coordX,coordY),ficha1,ficha2)    
                            coordX+=100
                        coordY-=100
    
    
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit() 
                            sys.exit   
    
    #Modo un jugador
    
    
            elif modo==1:
            
                while not victoria:
                
                    presionado=pygame.mouse.get_pressed(3)[0] #boolean Si el mouse esta presionado
                    mouse_pos=pygame.mouse.get_pos() #Dupla con las cordenadas x y y del mouse 
                    x = mouse_pos[0]//100 #Sector de el tablero en el que esta
                    centroCirculo=((x*100)+50) #Coord x de el centro de la circunferencia 
    
                    #Poner linda la pantalla
                    PANTALLA.fill(BLANCO)
                    if mapa == 1:
                        cuadricula(100)
                        ficha1=50
                        ficha2=15
                    elif mapa == 2:
                        cuadricula2(col_tab,BLANCO)
                        ficha1=45
                        ficha2=0
                    
                    #Dibujar circulo en la posicion del mouse (falta completar bien )
                    pygame.draw.circle(PANTALLA,jug_1,(centroCirculo,50),ficha1,ficha2)
                    pygame.event.wait()
    
                    #Prototipo:
                    if presionado:
                        dupla = ponerFicha(x,tablero,1,jugador) 
                        tablero = dupla[0]
                        jugador = dupla [1]            
                        if revisarVictoria(tablero,1):
                            victoria = True
                            ganador = 3
                            print("Gano jugador 1")
    
                        if not victoria:
                            tablero = ponerFicha(random.randint(0, 6),tablero,2,0)[0]
                            jugador += 1
                            if revisarVictoria(tablero,2):
                                victoria = True
                                ganador = 4
                                print("Gano el Bot")
    
                        if jugador>=42: #42
                            victoria = True
                            print('Empate')
    
    
                    # dibujar las circunferencias de la matriz
                    coordX=50
                    coordY=650
                    for fila in tablero:
                        coordX=50
                        for elemento in fila:
                            if elemento!=0:
                                if elemento==1:
                                    pygame.draw.circle(PANTALLA,jug_1,(coordX,coordY),ficha1,ficha2)
                                elif elemento==2:
                                    pygame.draw.circle(PANTALLA,jug_2,(coordX,coordY),ficha1,ficha2)    
                            coordX+=100
                        coordY-=100
    
    
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit() 
                            sys.exit   
    
            pygame.quit() 
            return(ganador)
    
    
    '''Empieza la interfaz Visual'''
    
    def interfaz(tablero=1,jugadores=1,colores=1,primera_vez=-1):
        #Colores basicos 
    
        BLANCO=(255,255,255)
        NEGRO=(0,0,0)
        ROJO=(255,0,0)
        AZUL=(0,0,255)
        VERDE=(0,255,0)
        MORADO=(100,40,200)
    
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
    
    
        pygame.init()
        PANTALLA= pygame.display.set_mode((500,650))
        pygame.display.set_caption('Conecta 4')
        PANTALLA.fill(BLANCO)
        #fuente 
        fuente=pygame.font.SysFont("aniME Matrix - MB_EN",40)
        fuente_titulo=pygame.font.SysFont("Britannic",50)
    
        boton1=(165,195,150,50)
        boton2=(100,295,300,50)
        boton_salir=(175,395,125,50)
        boton_atras=(175,495,125,50)
    
        configuraciones=False
    
        while primera_vez != -1:
        
            presionado=pygame.mouse.get_pressed(3)[0] #boolean Si el mouse esta presionado
            mouse_pos=pygame.mouse.get_pos() #Dupla con las cordenadas x y y del mouse
            x=mouse_pos[0]
            y=mouse_pos[1]
             
            #Colores botones    
    
            if 100 <= x <= 100+300 and 295 <= y <= 295+50:
                color_volver=PALETA1_JUGADOR2
            else:
                color_volver=PALETA1_COLOR1
    
            if 100 <= x <= 100+300 and 393 <= y <= 395+50:
                color_salir=PALETA1_JUGADOR2
            else:
                color_salir=PALETA1_COLOR1
    
    
            conecta4= fuente_titulo.render("Conecta 4",True,(PALETA2_COLOR3)) 
            PANTALLA.blit(conecta4,(135,50)) 
            pygame.display.flip()
    
            if primera_vez == 0:
                titulo_gano= fuente_titulo.render("Empate",True,(MORADO)) 
                pos_victoria=120
            if primera_vez == 1:
                titulo_gano= fuente_titulo.render("Gano Jugador 1",True,(MORADO)) 
                pos_victoria=80
            if primera_vez == 2:
                titulo_gano= fuente_titulo.render("Gano Jugador 2",True,(MORADO))
                pos_victoria=155
            if primera_vez == 3:
                titulo_gano= fuente_titulo.render("Ganaste",True,(MORADO))
                pos_victoria=155
            if primera_vez == 4:
                titulo_gano= fuente_titulo.render("Perdiste",True,(MORADO)) 
                pos_victoria=155
            
            PANTALLA.blit(titulo_gano,(pos_victoria,150))  #130,150
            pygame.display.flip()
    
    
            pygame.draw.rect(PANTALLA,color_volver,(100,295,300,50),0)
            volver_jugar= fuente.render("  Volver a jugar",True,(PALETA1_COLOR3)) #(texto,antialiasing,color)
            PANTALLA.blit(volver_jugar,(125,305)) #Cordenada
            pygame.display.flip()
    
    
            pygame.draw.rect(PANTALLA,color_salir,(100,395,300,50),0)  
            salir_victoria= fuente.render("Salir",True,(PALETA1_COLOR3)) #(texto,antialiasing,color)
            PANTALLA.blit(salir_victoria,(220,405)) #Cordenada
            pygame.display.flip()
    
    
            if 100 <= x <= 100+300 and 295 <= y <= 295+50 and presionado:
                primera_vez = -1
               
    
            if 100 <= x <= 100+300 and 393 <= y <= 395+50 and presionado:
                    pygame.quit() 
                    sys.exit   
    
    
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit() 
                    sys.exit   
    
        PANTALLA.fill(BLANCO)

        while True:
        
            presionado=pygame.mouse.get_pressed(3)[0] #boolean Si el mouse esta presionado
            mouse_pos=pygame.mouse.get_pos() #Dupla con las cordenadas x y y del mouse
            x=mouse_pos[0]
            y=mouse_pos[1]
    
            #menu principal
            if not configuraciones:
            
                if 165 <= x <= 165+150 and 195 <= y <= 195+50:
                    color_boton1=PALETA1_JUGADOR2
                else:
                    color_boton1=PALETA1_COLOR1
    
                if 100 <= x <= 100+300 and 295 <= y <= 295+50:
                    color_boton2=PALETA1_JUGADOR2
                else:
                    color_boton2=PALETA1_COLOR1
    
                if 175 <= x <= 175+125 and 395 <= y <= 395+50:
                    color_boton3=PALETA1_JUGADOR2
                else:
                    color_boton3=PALETA1_COLOR1
    
                #Boton jugar
                pygame.draw.rect(PANTALLA,color_boton1,boton1,0)
                jugar= fuente.render("Jugar",True,(PALETA1_COLOR3)) #(texto,antialiasing,color)
                PANTALLA.blit(jugar,(195,205)) #Cordenadas
                pygame.display.flip()
    
                if 165 <= x <= 165+150 and 195 <= y <= 195+50 and presionado:
                    pygame.quit() 
                    interfaz(tablero,jugadores,colores,ida_de_olla(colores,tablero,jugadores))
      
                #Boton Configuraciones
                pygame.draw.rect(PANTALLA,color_boton2,boton2,0)
                Configuraciones= fuente.render("Configuraciones",True,(PALETA1_COLOR3)) #(texto,antialiasing,color)
                PANTALLA.blit(Configuraciones,(125,305)) #Cordenada
                pygame.display.flip()
    
                #Boton Salir
                pygame.draw.rect(PANTALLA,color_boton3,boton_salir,0)
                salir= fuente.render("Salir",True,(PALETA1_COLOR3)) #(texto,antialiasing,color)
                PANTALLA.blit(salir,(200,405)) #Cordenadas
                pygame.display.flip()
    
                if 175 <= x <= 175+125 and 395 <= y <= 395+50 and presionado:
                    pygame.quit() 
                    sys.exit   
    
    
                if 100 <= x <= 100+300 and 295 <= y <= 295+50 and presionado:
                    configuraciones = True
                    PANTALLA.fill(BLANCO)
    
    
    
            #Menu configuraciones
            if configuraciones:
            
                #boton atras
                if 175 <= x <= 175+125 and 495 <= y <= 495+50:
                    color_boton3=PALETA1_JUGADOR2
                else:
                    color_boton3=PALETA1_COLOR1
    
                #Botones Tablero 
                if 235 <= x <= 235+155 and 190 <= y <= 190+50:
                    color_cuadricula=PALETA1_JUGADOR2
                else:
                    if tablero==1:
                        color_cuadricula=MORADO
                    else:
                        color_cuadricula=PALETA1_COLOR1
    
                if 90 <= x <= 90+125 and 190 <= y <= 190+50:
                    color_clasico=PALETA1_JUGADOR2
                else:
                    if tablero==2:
                        color_clasico=MORADO
                    else:
                        color_clasico=PALETA1_COLOR1
    
    
                #Botones Jugadores
                if 325 <= x <= 325+100 and 290 <= y <= 290+50:
                    color_solo=PALETA1_JUGADOR2
                else:
                    if jugadores==1:
                        color_solo=MORADO
                    else:    
                        color_solo=PALETA1_COLOR1
    
                if 80 <= x <= 80+230 and 290 <= y <= 290+50:
                    color_amigos=PALETA1_JUGADOR2
                else:
                    if jugadores==2:
                        color_amigos=MORADO
                    else:
                        color_amigos=PALETA1_COLOR1
    
                #Botones Colores
                if 125<= x <= 125+50 and 390 <= y <= 390+50:
                    color_1=PALETA1_JUGADOR2
                else:
                    if  colores==1:
                        color_1=MORADO
                    else:
                        color_1=PALETA1_COLOR1
    
                if 225 <= x <= 225+50 and 390 <= y <= 390+50:
                    color_2=PALETA1_JUGADOR2
                else:
                    if colores == 2:
                        color_2=MORADO
                    else:    
                        color_2=PALETA1_COLOR1
    
                if 325 <= x <= 325+50 and 390 <= y <= 390+50:
                    color_3=PALETA1_JUGADOR2
                else:
                    if colores == 3:
                        color_3=MORADO
                    else:    
                        color_3=PALETA1_COLOR1
    
                #Configuracion del tablero 
                conecta4= fuente.render("Tablero",True,(PALETA2_JUGADOR1)) 
                PANTALLA.blit(conecta4,(180,150)) 
                pygame.display.flip()
    
    
                pygame.draw.rect(PANTALLA,color_cuadricula,(235,190,195,50),0)
                Cuadricula= fuente.render("Cuadricula",True,(PALETA1_COLOR3)) 
                PANTALLA.blit(Cuadricula,(250,200)) 
                pygame.display.flip()
    
                pygame.draw.rect(PANTALLA,color_clasico,(90,190,125,50),0)
                Clasico= fuente.render("Clasico",True,(PALETA1_COLOR3)) 
                PANTALLA.blit(Clasico,(100,200)) 
                pygame.display.flip()
    
    
                #Configuracion jugadores
                Jugadores= fuente.render("Jugadores",True,(PALETA2_JUGADOR1)) 
                PANTALLA.blit(Jugadores,(158,250)) 
                pygame.display.flip()
    
                pygame.draw.rect(PANTALLA,color_solo,(325,290,100,50),0)
                Solo= fuente.render("Solo",True,(PALETA1_COLOR3)) 
                PANTALLA.blit(Solo,(340,300)) 
                pygame.display.flip()
    
                pygame.draw.rect(PANTALLA,color_amigos,(80,290,230,50),0) 
                Amigos= fuente.render("Multijugador",True,(PALETA1_COLOR3)) 
                PANTALLA.blit(Amigos ,(90,300)) 
                pygame.display.flip()
    
                #Configuracion colores
    
                Colores= fuente.render("Colores",True,(PALETA2_JUGADOR1)) 
                PANTALLA.blit(Colores,(170,350)) 
                pygame.display.flip()
    
                pygame.draw.rect(PANTALLA,color_1,(125,390,50,50),0)
                color1= fuente.render("1",True,(PALETA1_COLOR3)) 
                PANTALLA.blit(color1,(145,400)) 
                pygame.display.flip()
    
                pygame.draw.rect(PANTALLA,color_2,(225,390,50,50),0)
                color2= fuente.render("2",True,(PALETA1_COLOR3)) 
                PANTALLA.blit(color2,(243,400)) 
                pygame.display.flip()
    
                pygame.draw.rect(PANTALLA,color_3,(325,390,50,50),0)
                color3= fuente.render("3",True,(PALETA1_COLOR3)) 
                PANTALLA.blit(color3,(340,400)) 
                pygame.display.flip()
    
                
    
    
                #Funciones Botones
    
                #Tablero
                if 235 <= x <= 235+155 and 190 <= y <= 190+50 and presionado:
                    tablero=1
                if 90 <= x <= 90+125 and 190 <= y <= 190+50 and presionado:
                    tablero=2
    
                #Jugadores
    
                if 325 <= x <= 325+100 and 290 <= y <= 290+50 and presionado:
                    jugadores=1
                if 80 <= x <= 80+230 and 290 <= y <= 290+50 and presionado:
                    jugadores=2
    
                #Colores    
    
                if 125<= x <= 125+50 and 390 <= y <= 390+50 and presionado:
                    colores=1
                if 225 <= x <= 225+50 and 390 <= y <= 390+50 and presionado:
                    colores =2
                if 325 <= x <= 325+50 and 390 <= y <= 390+50 and presionado:
                    colores=3
    
    
                #Boton Atras
                pygame.draw.rect(PANTALLA,color_boton3,boton_atras,0)
                atras= fuente.render("Atras",True,(PALETA1_COLOR3)) 
                PANTALLA.blit(atras,(192,505)) 
                pygame.display.flip()
    
                if 175 <= x <= 175+125 and 495 <= y <= 495+50 and presionado:
                    configuraciones = False
                    PANTALLA.fill(BLANCO)
    
    
            #titulo
            conecta4= fuente_titulo.render("Conecta 4",True,(PALETA2_COLOR3)) 
            PANTALLA.blit(conecta4,(135,50)) 
            pygame.display.flip()
    
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit() 
                    sys.exit  
    
    interfaz()
conecta4()
