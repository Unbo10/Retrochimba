import pygame
from copy import deepcopy
from random import choice, randrange

def RCtetris():
    print("Bienvenido a tetris")
    print("1. Tetris original")
    print("2. Tetris hard mode")
    print("3. Tetris Zen mode")
    a = int(input("Para seleccionar el modo digite el numero que esta relacionado: "))
    def tetrisoriginal():
        FONDO = 750, 640  # pantalla del juego
        X, Y = 10, 20
        TOPE = 32

        FONDO2 = X * TOPE, Y * TOPE  # pantalla del juego
        FPS = 60

        zonaj = [pygame.Rect(x * TOPE, y * TOPE, TOPE, TOPE) for x in range(X) for y in range(Y)]
        pygame.init()
        juego = pygame.display.set_mode(FONDO)
        juego_comprimido = pygame.Surface(FONDO2)
        reloj = pygame.time.Clock()

        origenfig = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],  # la linea
                    [(0, -1), (-1, -1), (-1, 0), (0, 0)],
                    [(-1, 0), (-1, 1), (0, 0), (0, -1)],
                    [(0, 0), (-1, 0), (0, 1), (-1, -1)],
                    [(0, 0), (0, -1), (0, 1), (-1, -1)],
                    [(0, 0), (0, -1), (0, 1), (1, -1)],
                    [(0, 0), (0, -1), (0, 1), (-1, 0)]]

        figuras = [[pygame.Rect(x + X // 2, y + 1, 1, 1) for x, y in origenfig] for origenfig in origenfig]
        figura_rect = pygame.Rect(0, 0, TOPE - 2, TOPE - 2)
        cancha = [[0 for i in range(X)] for j in range(Y)]

        caidac, caidav, caidal = 0, 3, 2000

        fuentep = pygame.font.Font("Minecraft.ttf", 63)
        fuente = pygame.font.Font("Minecraft.ttf", 43)

        Titulo = fuentep.render('OLD TETRIS', True, pygame.Color('Blue'))
        Siguiente_figura = fuente.render('Siguiente', True, pygame.Color('Green'))
        PUNTAJE = fuente.render('Puntuacion', True, pygame.Color('White'))
        Recordt = fuente.render('Record: ', True, pygame.Color('Blue'))

        seleccion_color = lambda: (randrange(30, 256), randrange(30, 256), randrange(30, 256))

        FIGURA, figura_siguiente = deepcopy(choice(figuras)), deepcopy(choice(figuras))  # Cual figura sale primero
        color, proximo_color = seleccion_color(), seleccion_color()

        puntaje, lineas = 0, 0
        puntajesp = {0: 0, 1: 100, 2: 300, 3: 700, 4: 1500}
        icono=pygame.image.load("images/logo-RC-4.png")
        pygame.display.set_icon(icono)

        def bordes():  # limita el borde de movimiento
            if FIGURA[i].x < 0 or FIGURA[i].x > X - 1:
                return False
            elif FIGURA[i].y > Y - 1 or cancha[FIGURA[i].y][FIGURA[i].x]:
                return False
            return True

        def calculo_record():
            try:
                with open('Record') as f:
                    return f.readline()
            except FileNotFoundError:
                with open('Record', 'w') as f:
                    f.write('0')

        def record_visible(Record, puntaje):
            recM = max(int(Record), puntaje)
            with open('Record', 'w') as f:
                f.write(str(recM))

        while True:  # blucle para abrir el juego
            Record = calculo_record()
            ejex = 0
            rotacion = False
            juego.fill(pygame.Color("Black"))
            # pausa por lineas completadas
            for i in range(lineas):
                pygame.time.wait(200)  # nos da una pausa entre que completamos una linea y que se empieza a mover la otra
            for evento in pygame.event.get():  # esto cierra el juego
                if evento.type == pygame.QUIT:
                    exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_LEFT:
                        ejex = -1
                    elif evento.key == pygame.K_RIGHT:
                        ejex = 1
                    elif evento.key == pygame.K_DOWN:
                        caidal = 100
                    elif evento.key == pygame.K_UP:
                        rotacion = True
            # movimiento en el eje x
            figuraorg = deepcopy(FIGURA)
            for i in range(4):
                FIGURA[i].x += ejex
                if not bordes():  # esto limita el movimento en el eje x
                    FIGURA = deepcopy(figuraorg)
                    break
                # caida y moviemineto en el eje y
            caidac += caidav
            if caidac > caidal:
                caidac = 0
                figuraorg = deepcopy(FIGURA)
                for i in range(4):
                    FIGURA[i].y += 1
                    if not bordes():  # esto limita el movimento en el eje x
                        for i in range(4):
                            cancha[figuraorg[i].y][figuraorg[i].x] = color
                        FIGURA, color = figura_siguiente, proximo_color
                        figura_siguiente, proximo_color = deepcopy(choice(figuras)), seleccion_color()
                        caidal = 2000
                        break
                # rotacion de la figuras
            centro = FIGURA[0]
            figuraorg = deepcopy(FIGURA)
            if rotacion:
                for i in range(4):
                    x = FIGURA[i].y - centro.y
                    y = FIGURA[i].x - centro.x
                    FIGURA[i].x = centro.x - x
                    FIGURA[i].y = centro.y + y
                    if not bordes():  # esto limita el movimento en el eje x
                        FIGURA = deepcopy(figuraorg)
                        break
            # Romper la lineas
            linea, lineas = Y - 1, 0
            for row in range(Y - 1, -1, -1):
                cuenta = 0
                for i in range(X):
                    if cancha[row][i]:
                        cuenta += 1
                    cancha[linea][i] = cancha[row][i]
                if cuenta < X:
                    linea -= 1
                else:
                    caidav += 0.5
                    lineas += 1
            # calculo puntaje
            puntaje += puntajesp[lineas]

            # Mostramos la zona de juego
            [pygame.draw.rect(juego, (20, 20, 20), i_rect, 1) for i_rect in zonaj]
            # mostramos la figuras
            for i in range(4):
                figura_rect.x = FIGURA[i].x * TOPE
                figura_rect.y = FIGURA[i].y * TOPE
                pygame.draw.rect(juego, color, figura_rect)
            # dibujamnos la cancha
            for y, raw in enumerate(cancha):
                for x, col in enumerate(raw):
                    if col:
                        figura_rect.x, figura_rect.y = x * TOPE, y * TOPE
                        pygame.draw.rect(juego, col, figura_rect)
            # Mostramos la siguiente figura
            for i in range(4):
                figura_rect.x = figura_siguiente[i].x * TOPE + 250
                figura_rect.y = figura_siguiente[i].y * TOPE + 170
                pygame.draw.rect(juego, proximo_color, figura_rect)
            # mostramos el titulo
            juego.blit(Titulo, (335, 0))
            juego.blit(Siguiente_figura, (340, 90))
            juego.blit(PUNTAJE, (340, 300))
            juego.blit(fuente.render(str(puntaje), True, pygame.Color('white')), (660, 300))
            juego.blit(Recordt, (340, 470))
            juego.blit(fuente.render(Record, True, pygame.Color('gold')), (620, 470))  # final del juego
            for i in range(X):
                if cancha[0][i]:
                    record_visible(Record, puntaje)
                    cancha = [[0 for i in range(X)] for i in range(Y)]
                    caidac, caidav, caidal = 0, 3, 2000
                    puntaje = 0
                    for i_rect in zonaj:
                        pygame.draw.rect(juego_comprimido, seleccion_color(), i_rect)
                        juego.blit(juego_comprimido, (0, 0))
                        pygame.display.flip()
                        reloj.tick(150)

            pygame.display.flip()
            reloj.tick()
    def tetrishardmode():
        FONDO = 750, 640  # pantalla del juego
        X, Y = 10, 20
        TOPE = 32

        FONDO2 = X * TOPE, Y * TOPE  # pantalla del juego
        FPS = 60

        zonaj = [pygame.Rect(x * TOPE, y * TOPE, TOPE, TOPE) for x in range(X) for y in range(Y)]
        pygame.init()
        juego = pygame.display.set_mode(FONDO)
        juego_comprimido = pygame.Surface(FONDO2)
        reloj = pygame.time.Clock()

        origenfig = [[(-1, 0), (-2, 0), (0, 0), (1, 0), (1, 0)],  # la linea
                    [(0, -1), (-1, -1), (-1, 0), (0, 0), (0, 0)],
                    [(-1, 0), (-1, 1), (0, 0), (0, -1), (0, -1)],
                    [(0, 0), (-1, 0), (0, 1), (-1, -1), (-1, -1)],
                    [(0, 0), (0, -1), (0, 1), (-1, -1), (-1, -1)],
                    [(0, 0), (0, -1), (0, 1), (1, -1), (1, -1)],
                    [(0, 0), (0, -1), (0, 1), (-1, 0), (-1, 0)],
                    [(-1, 0), (0, 0), (-1, -1), (0, 0), (0, 0)],
                    [(-1, 1), (-1, 0), (-1, 1), (-1, 0), (-1, 0)],
                    [(-1, 0), (-2, 0), (0, 0), (0, -1), (-2, -1)]]

        figuras = [[pygame.Rect(x + X // 2, y + 1, 1, 1) for x, y in origenfig] for origenfig in origenfig]
        figura_rect = pygame.Rect(0, 0, TOPE - 2, TOPE - 2)
        cancha = [[0 for i in range(X)] for j in range(Y)]

        caidac, caidav, caidal = 0, 3, 2000

        fuentep = pygame.font.Font("Minecraft.ttf", 63)
        fuente = pygame.font.Font("Minecraft.ttf", 43)

        Titulo = fuentep.render('HARD MODE', True, pygame.Color('Red'))
        Siguiente_figura = fuente.render('Siguiente', True, pygame.Color('Orange'))
        PUNTAJE = fuente.render('Puntuacion', True, pygame.Color('White'))
        Recordt = fuente.render('Record: ', True, pygame.Color('orange'))

        seleccion_color = lambda: (randrange(30, 256), randrange(30, 256), randrange(30, 256))

        FIGURA, figura_siguiente = deepcopy(choice(figuras)), deepcopy(choice(figuras))  # Cual figura sale primero
        color, proximo_color = seleccion_color(), seleccion_color()

        puntaje, lineas = 0, 0
        puntajesp = {0: 0, 1: 100, 2: 200, 3: 500, 4: 1000}
        icono = pygame.image.load("images/logo-RC-4.png")
        pygame.display.set_icon(icono)

        def bordes():  # limita el borde de movimiento
            if FIGURA[i].x < 0 or FIGURA[i].x > X - 1:
                return False
            elif FIGURA[i].y > Y - 1 or cancha[FIGURA[i].y][FIGURA[i].x]:
                return False
            return True

        def calculo_record():
            try:
                with open('Record') as f:
                    return f.readline()
            except FileNotFoundError:
                with open('Record', 'w') as f:
                    f.write('0')

        def record_visible(Record, puntaje):
            recM = max(int(Record), puntaje)
            with open('Record', 'w') as f:
                f.write(str(recM))

        while True:  # blucle para abrir el juego
            Record = calculo_record()
            ejex = 0
            rotacion = False
            juego.fill(pygame.Color("Black"))
            # pausa por lineas completadas
            for i in range(lineas):
                pygame.time.wait(200)
            for evento in pygame.event.get():  # esto cierra el juego
                if evento.type == pygame.QUIT:
                    exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_LEFT:
                        ejex = -1
                    elif evento.key == pygame.K_RIGHT:
                        ejex = 1
                    elif evento.key == pygame.K_DOWN:
                        caidal = 100
                    elif evento.key == pygame.K_UP:
                        rotacion = True
                # movimiento en el eje x
            figuraorg = deepcopy(FIGURA)
            for i in range(5):
                FIGURA[i].x += ejex
                if not bordes():  # esto limita el movimento en el eje x
                    FIGURA = deepcopy(figuraorg)
                    break
                # caida y moviemineto en el eje y
            caidac += caidav
            if caidac > caidal:
                caidac = 0
                figuraorg = deepcopy(FIGURA)
                for i in range(5):
                    FIGURA[i].y += 1
                    if not bordes():  # esto limita el movimento en el eje x
                        for i in range(5):
                            cancha[figuraorg[i].y][figuraorg[i].x] = color
                        FIGURA, color = figura_siguiente, proximo_color
                        figura_siguiente, proximo_color = deepcopy(choice(figuras)), seleccion_color()
                        caidal = 2000
                        break
                # rotacion de la figuras
            centro = FIGURA[0]
            figuraorg = deepcopy(FIGURA)
            if rotacion:
                for i in range(5):
                    x = FIGURA[i].y - centro.y
                    y = FIGURA[i].x - centro.x
                    FIGURA[i].x = centro.x - x
                    FIGURA[i].y = centro.y + y
                    if not bordes():  # esto limita el movimento en el eje x
                        FIGURA = deepcopy(figuraorg)
                        break
            # Romper la lineas
            linea, lineas = Y - 1, 0
            for row in range(Y - 1, -1, -1):
                cuenta = 0
                for i in range(X):
                    if cancha[row][i]:
                        cuenta += 1
                    cancha[linea][i] = cancha[row][i]
                if cuenta < X:
                    linea -= 1
                else:
                    caidav += 0.7
                    lineas += 1
            # calculo puntaje
            puntaje += puntajesp[lineas]

            # Mostramos la zona de juego
            [pygame.draw.rect(juego, (30, 30, 30), i_rect, 1) for i_rect in zonaj]
            # mostramos la figuras
            for i in range(5):
                figura_rect.x = FIGURA[i].x * TOPE
                figura_rect.y = FIGURA[i].y * TOPE
                pygame.draw.rect(juego, color, figura_rect)
            # dibujamnos la cancha
            for y, raw in enumerate(cancha):
                for x, col in enumerate(raw):
                    if col:
                        figura_rect.x, figura_rect.y = x * TOPE, y * TOPE
                        pygame.draw.rect(juego, col, figura_rect)
            # Mostramos la siguiente figura
            for i in range(5):
                figura_rect.x = figura_siguiente[i].x * TOPE + 250
                figura_rect.y = figura_siguiente[i].y * TOPE + 170
                pygame.draw.rect(juego, proximo_color, figura_rect)
            # mostramos el titulo
            juego.blit(Titulo, (375, 0))
            juego.blit(Siguiente_figura, (340, 90))
            juego.blit(PUNTAJE, (350, 300))
            juego.blit(fuente.render(str(puntaje), True, pygame.Color('white')), (650, 300))
            juego.blit(Recordt, (350, 500))
            juego.blit(fuente.render(Record, True, pygame.Color('gold')), (600, 500))  # final del juego
            for i in range(X):
                if cancha[0][i]:
                    record_visible(Record, puntaje)
                    cancha = [[0 for i in range(X)] for i in range(Y)]
                    caidac, caidav, caidal = 0, 3, 2000
                    puntaje = 0
                    for i_rect in zonaj:
                        pygame.draw.rect(juego_comprimido, seleccion_color(), i_rect)
                        juego.blit(juego_comprimido, (20, 20))
                        pygame.display.flip()
                        reloj.tick(200)

            pygame.display.flip()
            reloj.tick()
    def tetriszenmode():
        FONDO = 880, 640  # pantalla del juego
        X, Y = 13, 20
        TOPE = 32

        FONDO2 = X * TOPE, Y * TOPE  # pantalla del juego
        FPS = 60

        zonaj = [pygame.Rect(x * TOPE, y * TOPE, TOPE, TOPE) for x in range(X) for y in range(Y)]
        pygame.init()
        juego = pygame.display.set_mode(FONDO)
        juego_comprimido = pygame.Surface(FONDO2)
        reloj = pygame.time.Clock()

        origenfig = [[(-1, 0), (-2, 0), (0, 0), (1, 0), (1, 0)],  # la linea
                    [(0, -1), (-1, -1), (-1, 0), (0, 0), (0, 0)],
                    [(-1, 0), (-1, 1), (0, 0), (0, -1), (0, -1)],
                    [(0, 0), (-1, 0), (0, 1), (-1, -1), (-1, -1)],
                    [(0, 0), (0, -1), (0, 1), (-1, -1), (-1, -1)],
                    [(0, 0), (0, -1), (0, 1), (1, -1), (1, -1)],
                    [(0, 0), (0, -1), (0, 1), (-1, 0), (-1, 0)]]

        figuras = [[pygame.Rect(x + X // 2, y + 1, 1, 1) for x, y in origenfig] for origenfig in origenfig]
        figura_rect = pygame.Rect(0, 0, TOPE - 2, TOPE - 2)
        cancha = [[0 for i in range(X)] for j in range(Y)]

        caidac, caidav, caidal = 0, 3, 2000

        fuentep = pygame.font.Font("Minecraft.ttf", 63)
        fuente = pygame.font.Font("Minecraft.ttf", 43)

        Titulo = fuentep.render('ZEN MODE ', True, pygame.Color('white'))
        Siguiente_figura = fuente.render('Siguiente', True, pygame.Color('pink'))
        PUNTAJE = fuente.render('Puntuacion: ', True, pygame.Color('White'))
        Recordt = fuente.render('Record: ', True, pygame.Color('Blue'))

        seleccion_color = lambda: (randrange(254, 255), randrange(254, 255), randrange(254, 255))

        FIGURA, figura_siguiente = deepcopy(choice(figuras)), deepcopy(choice(figuras))  # Cual figura sale primero
        color, proximo_color = seleccion_color(), seleccion_color()
        icono = pygame.image.load("images/logo-RC-4.png")
        pygame.display.set_icon(icono)

        puntaje, lineas = 0, 0
        puntajesp = {0: 0, 1: 100, 2: 300, 3: 700, 4: 1500}

        def bordes():  # limita el borde de movimiento
            if FIGURA[i].x < 0 or FIGURA[i].x > X - 1:
                return False
            elif FIGURA[i].y > Y - 1 or cancha[FIGURA[i].y][FIGURA[i].x]:
                return False
            return True

        def calculo_record():
            try:
                with open('Record') as f:
                    return f.readline()
            except FileNotFoundError:
                with open('Record', 'w') as f:
                    f.write('0')

        def record_visible(Record, puntaje):
            recM = max(int(Record), puntaje)
            with open('Record', 'w') as f:
                f.write(str(recM))

        while True:  # blucle para abrir el juego
            Record = calculo_record()
            ejex = 0
            rotacion = False
            juego.fill(pygame.Color("Black"))
            # pausa por lineas completadas
            for i in range(lineas):
                pygame.time.wait(200)  # nos da una pausa entre que completamos una linea y que se empieza a mover la otra
            for evento in pygame.event.get():  # esto cierra el juego
                if evento.type == pygame.QUIT:
                    exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_LEFT:
                        ejex = -1
                    elif evento.key == pygame.K_RIGHT:
                        ejex = 1
                    elif evento.key == pygame.K_DOWN:
                        caidal = 100
                    elif evento.key == pygame.K_UP:
                        rotacion = True
            # movimiento en el eje x
            figuraorg = deepcopy(FIGURA)
            for i in range(5):
                FIGURA[i].x += ejex
                if not bordes():  # esto limita el movimento en el eje x
                    FIGURA = deepcopy(figuraorg)
                    break
                # caida y moviemineto en el eje y
            caidac += caidav
            if caidac > caidal:
                caidac = 0
                figuraorg = deepcopy(FIGURA)
                for i in range(5):
                    FIGURA[i].y += 1
                    if not bordes():  # esto limita el movimento en el eje x
                        for i in range(5):
                            cancha[figuraorg[i].y][figuraorg[i].x] = color
                        FIGURA, color = figura_siguiente, proximo_color
                        figura_siguiente, proximo_color = deepcopy(choice(figuras)), seleccion_color()
                        caidal = 2000
                        break
                # rotacion de la figuras
            centro = FIGURA[0]
            figuraorg = deepcopy(FIGURA)
            if rotacion:
                for i in range(5):
                    x = FIGURA[i].y - centro.y
                    y = FIGURA[i].x - centro.x
                    FIGURA[i].x = centro.x - x
                    FIGURA[i].y = centro.y + y
                    if not bordes():  # esto limita el movimento en el eje x
                        FIGURA = deepcopy(figuraorg)
                        break
            # Romper la lineas
            linea, lineas = Y - 1, 0
            for row in range(Y - 1, -1, -1):
                cuenta = 0
                for i in range(X):
                    if cancha[row][i]:
                        cuenta += 1
                    cancha[linea][i] = cancha[row][i]
                if cuenta < X:
                    linea -= 1
                else:
                    lineas += 1
            puntaje += puntajesp[lineas]

            # Mostramos la zona de juego
            [pygame.draw.rect(juego, (20, 20, 20), i_rect, 1) for i_rect in zonaj]
            # mostramos la figuras
            for i in range(5):
                figura_rect.x = FIGURA[i].x * TOPE
                figura_rect.y = FIGURA[i].y * TOPE
                pygame.draw.rect(juego, color, figura_rect)
            # dibujamnos la cancha
            for y, raw in enumerate(cancha):
                for x, col in enumerate(raw):
                    if col:
                        figura_rect.x, figura_rect.y = x * TOPE, y * TOPE
                        pygame.draw.rect(juego, col, figura_rect)
            # Mostramos la siguiente figura
            for i in range(5):
                figura_rect.x = figura_siguiente[i].x * TOPE + 350
                figura_rect.y = figura_siguiente[i].y * TOPE + 170
                pygame.draw.rect(juego, proximo_color, figura_rect)
            # mostramos el titulo

        # final del juego
            juego.blit(Titulo, (475, 0))
            juego.blit(Siguiente_figura, (460, 90))
            juego.blit(PUNTAJE, (470, 300))
            juego.blit(fuente.render(str(puntaje), True, pygame.Color('white')), (780, 300))
            juego.blit(Recordt, (470, 420))
            juego.blit(fuente.render(Record, True, pygame.Color('light blue')), (730, 420))  # final del juego
            for i in range(X):
                if cancha[0][i]:
                    record_visible(Record, puntaje)
                    cancha = [[0 for i in range(X)] for i in range(Y)]
                    caidac, caidav, caidal = 0, 3, 2000
                    puntaje = 0
                    for i_rect in zonaj:
                        pygame.draw.rect(juego_comprimido, seleccion_color(), i_rect)
                        juego.blit(juego_comprimido, (0, 0))
                        pygame.display.flip()
                        reloj.tick(150)

            pygame.display.flip()
            reloj.tick()


    if(a == 1):
        tetrisoriginal()
    if(a==2):
        tetrishardmode()
    if(a==3):
        tetriszenmode()

RCtetris()


