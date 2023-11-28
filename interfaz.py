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
pygame.display.set_caption('RetroChimba')
PANTALLA.fill(BLANCO)
#fuente 
fuente=pygame.font.SysFont("aniME Matrix - MB_EN",20)
fuente_titulo=pygame.font.SysFont("Britannic",50)


while True:
    
    #Datos para los botones:

    presionado=pygame.mouse.get_pressed(3)[0] #boolean Si el mouse esta presionado
    mouse_pos=pygame.mouse.get_pos() #Dupla con las cordenadas x y y del mouse
    x=mouse_pos[0]
    y=mouse_pos[1]    


    #Feedback Botones:

    #Conecta 4
    if 125 <= x <= 125+250 and 195 <= y <= 195+50:
        color_conecta=PALETA1_JUGADOR2
    else:
        color_conecta=PALETA1_COLOR1

    #tetris
    if 110 <= x <= 110+290 and 290 <= y <= 290+50:
        color_tetris=PALETA1_JUGADOR2
    else:
        color_tetris=PALETA1_COLOR1

    #galaga
    if 110 <= x <= 110+300 and 355 <= y <= 355+50:
        color_galaga=PALETA1_JUGADOR2
    else:
        color_galaga=PALETA1_COLOR1
    
    #F1
    if 125 <= x <= 125+250 and 435 <= y <= 435+50:
        color_f1=PALETA1_JUGADOR2
    else:
        color_f1=PALETA1_COLOR1

    #Salir
    if 195 <= x <= 195+115 and 515 <= y <= 515+50:
        color_salir=PALETA1_JUGADOR2
    else:
        color_salir=PALETA1_COLOR1

    RetroChimba= fuente_titulo.render("RetroChimba",True,(PALETA2_COLOR3)) 
    PANTALLA.blit(RetroChimba,(110,100)) 
    pygame.display.flip()

    #Botones:
    #Conecta 4
    pygame.draw.rect(PANTALLA,color_conecta,(125,195,250,50),0)
    conecta4= fuente.render("Conecta Chimba",True,(PALETA1_COLOR3)) 
    PANTALLA.blit(conecta4,(135,205)) 
    pygame.display.flip()

    #tetris
    pygame.draw.rect(PANTALLA,color_tetris,(110,275,290,50),0)
    tetris= fuente.render("Retrochimbetris",True,(PALETA1_COLOR3)) 
    PANTALLA.blit(tetris,(130,285)) 
    pygame.display.flip()
    pygame.display.update()

    #Galaga
    pygame.draw.rect(PANTALLA,color_galaga,(110,355,290,50),0)
    galaga= fuente.render("Retrochimbalaga",True,(PALETA1_COLOR3)) 
    PANTALLA.blit(galaga,(125,365)) 
    pygame.display.flip()
    pygame.display.update()

    #F1
    pygame.draw.rect(PANTALLA,color_f1,(125,435,250,50),0)
    f1= fuente.render("Formula Chimba",True,(PALETA1_COLOR3)) 
    PANTALLA.blit(f1,(135,445)) 
    pygame.display.flip()
    pygame.display.update()

    #Salir
    pygame.draw.rect(PANTALLA,color_salir,(195,515,115,50),0)
    salir= fuente.render("Salir",True,(PALETA1_COLOR3)) 
    PANTALLA.blit(salir,(215,525)) 
    pygame.display.flip()
    pygame.display.update()



    #Utilidad de los botones:

    #Conecta 4
    if 125 <= x <= 125+250 and 195 <= y <= 195+50 and presionado:
        pygame.quit() 
        from Conect4_terminado import conecta4

    #salir
    if 195 <= x <= 195+115 and 515 <= y <= 515+50 and presionado:
        pygame.quit() 
        sys.exit
    

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit() 
            sys.exit  
