    # Importar las librerias necesarias

import pygame
import sys
import random

def RCGalaga():

    # Inicializar Pygame

    pygame.init()

    # Constantes globales

    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600  # Tamaño de la pantalla
    SHIP_SIZE = (70, 50)  # Tamaño de la nave
    SHIP_SPEED = 5  # Velocidad de la nave
    BULLET_SIZE = (38, 40)  # Tamaño de los proyectiles
    BULLET_SPEED = 10  # Velocidad de los proyectiles
    ENEMY_SIZE = (70, 50)  # Tamaño de los enemigos
    ENEMY_SPEED = 4  # Velocidad de los enemigos vertical
    ENEMY_HORIZONTAL_MOVEMENT_RANGE = 3  # Rango de movimiento horizontal de los enemigos
    ENEMY_SPAWN_RATE = 25  # Frecuencia de aparición de los enemigos
    NEW_ENEMY_IMAGE_PATH = 'images/object_2.png'
    NEW_ENEMY_SIZE = (90, 70)  # Tamaño del enemigo 2
    NEW_ENEMY_SPEED = 4
    ship_image = pygame.image.load('images/spaceship.png')
    ship_image = pygame.transform.scale(ship_image, SHIP_SIZE)
    enemy_image = pygame.image.load('images/enemy_1.png')
    enemy_image = pygame.transform.scale(enemy_image, ENEMY_SIZE)
    background_image = pygame.image.load('images/Space-background.png')
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # Define el color, tamaño de la fuente y posición del puntaje

    puntaje_color = (255, 255, 255)  # Blanco
    puntaje_fuente = pygame.font.Font(None, 70)  # Tamaño y la fuente por defecto de Pygame
    puntaje_posicion = (180, 450)  # Coordenadas x e y en la pantalla

    # Cargar y escalar la imagen del enemigo 2

    new_enemy_image = pygame.image.load(NEW_ENEMY_IMAGE_PATH)
    new_enemy_image = pygame.transform.scale(new_enemy_image, NEW_ENEMY_SIZE)


    # Cargar y escalar la imagen de Game Over

    GAME_OVER_IMAGE_PATH = 'images/gameover.png'
    game_over_image = pygame.image.load(GAME_OVER_IMAGE_PATH)
    game_over_image = pygame.transform.scale(game_over_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # Cargar y escalar la imagen de nave avanzada

    ADVANCED_SHIP_IMAGE_PATH = 'images/sas.png'
    advanced_ship_image = pygame.image.load(ADVANCED_SHIP_IMAGE_PATH)
    advanced_ship_image = pygame.transform.scale(advanced_ship_image, SHIP_SIZE)

    # Cargar y escalar la imagen de la nave 2

    SPACESHIP2 = 'images/spaceship2.png'
    spaceship2 = pygame.image.load(SPACESHIP2)
    spaceship2 = pygame.transform.scale(spaceship2, SHIP_SIZE)

    # Constantes para el control de disparo

    BULLET_SHOOT_INTERVAL = 650  # 0.65 segundos expresados en milisegundos

    # Variable para almacenar el tiempo del último disparo

    last_shoot_time = 0

    # Cargar el sonido de la explosión

    explosion_sound = pygame.mixer.Sound('audio/Explosion.mp3')
    explosion_sound.set_volume(0.3) 

    # Cargar el sonido para cuando la nave muere

    game_over_sound = pygame.mixer.Sound('audio/Lose.mp3')
    game_over_sound.set_volume(0.5)


    # Cargar y escalar la imagen del proyectil

    BULLET_IMAGE_PATH = 'images/bullet_1.png'
    bullet_image = pygame.image.load(BULLET_IMAGE_PATH)
    bullet_image = pygame.transform.scale(bullet_image, BULLET_SIZE)

    # Cargar el sonido del disparo

    bullet_sound = pygame.mixer.Sound('audio/disparo.wav')
    bullet_sound.set_volume(0.2)
    score = 0  # Inicializar puntaje

    # Fuente para el puntaje

    font = pygame.font.Font(None, 50)

    # Inicializar Pygame y el mixer

    pygame.init()
    pygame.mixer.init()

    # Cargar la música de fondo

    pygame.mixer.music.load('audio/musica.mp3')

    # Establecer el volumen de la música

    pygame.mixer.music.set_volume(0.4)

    ship_position = [SCREEN_WIDTH//2, SCREEN_HEIGHT - SHIP_SIZE[1] * 2]
    bullets = []  # Lista para almacenar los proyectiles
    enemies = []  # Lista para almacenar los enemigos

    # Inicializar la pantalla

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('RETROCHIMBALAGA')

    # Funciones para la nave

    def draw_ship(screen, position, image=None):
        if image:
            screen.blit(image, position)
        else:
            screen.blit(ship_image, position)


    # Funciones para los proyectiles

    def shoot_bullet(bullets, position):
        bullet_position = [position[0] + SHIP_SIZE[0]//2 - BULLET_SIZE[0]//2, position[1]]
        bullets.append({"position": bullet_position, "active": True, "image": bullet_image})
        bullet_sound.play()


    def update_bullets(bullets):
        for bullet in bullets[:]:
            bullet["position"][1] -= BULLET_SPEED
            if bullet["position"][1] < 0:
                bullets.remove(bullet)

    def draw_bullets(screen, bullets):
        for bullet in bullets:
            screen.blit(bullet["image"], bullet["position"])

    # Funciones para los enemigos

    def add_enemy(enemies):
        x_pos = random.randint(0, SCREEN_WIDTH - ENEMY_SIZE[0])
        y_pos = -ENEMY_SIZE[1]
        x_move = random.randint(-ENEMY_HORIZONTAL_MOVEMENT_RANGE, ENEMY_HORIZONTAL_MOVEMENT_RANGE)
        enemies.append({"position": [x_pos, y_pos], "movement": [x_move, ENEMY_SPEED], "active": True, "health": 1})

    def add_new_enemy(enemies):
        x_pos = random.randint(0, SCREEN_WIDTH - NEW_ENEMY_SIZE[0])
        y_pos = -NEW_ENEMY_SIZE[1]
        x_move = random.randint(-ENEMY_HORIZONTAL_MOVEMENT_RANGE, ENEMY_HORIZONTAL_MOVEMENT_RANGE)
        enemies.append({"position": [x_pos, y_pos], "movement": [x_move, NEW_ENEMY_SPEED], "active": True, "type": "new", "health": 2})

    def update_enemies(enemies):
        for enemy in enemies[:]:
            enemy["position"][0] += enemy["movement"][0]
            enemy["position"][1] += enemy["movement"][1]

            # Revertir el movimiento horizontal si el enemigo alcanza el borde de la pantalla

            if enemy["position"][0] < 0 or enemy["position"][0] > SCREEN_WIDTH - ENEMY_SIZE[0]:
                enemy["movement"][0] = -enemy["movement"][0]

            if enemy["position"][1] > SCREEN_HEIGHT:
                enemies.remove(enemy)

    def draw_enemies(screen, enemies):
        for enemy in enemies:
            if enemy.get("type") == "new":
                screen.blit(new_enemy_image, enemy["position"])
            else:
                screen.blit(enemy_image, enemy["position"])

    # Funciones para la detección de colisiones

    def check_bullet_enemy_collisions(bullets, enemies, score):
        for bullet in bullets[:]:
            bullet_rect = pygame.Rect(*bullet["position"], *BULLET_SIZE)
            for enemy in enemies[:]:
                enemy_rect = pygame.Rect(*enemy["position"], *ENEMY_SIZE)
                if bullet_rect.colliderect(enemy_rect):
                    # Reducir la salud del enemigo

                    enemy["health"] -= 1
                    bullets.remove(bullet)
                    if enemy["health"] <= 0:
                        enemies.remove(enemy)
                        explosion_sound.play() 
                        score += 10  # Incrementar puntaje
                        return score
                    break  # Salir del bucle ya que la bala ya ha colisionado
        return score

    def check_ship_enemy_collisions(ship_position, enemies):
        ship_rect = pygame.Rect(*ship_position, *SHIP_SIZE)
        for enemy in enemies[:]:
            enemy_rect = pygame.Rect(*enemy["position"], *ENEMY_SIZE)
            if ship_rect.colliderect(enemy_rect):
                return True  # Colisión detectada
        return False  # No se detectó colisión

    def reset_game():
        score, bullets, enemies, ship_position, last_shoot_time, player_alive, enemy_spawn_timer, elapsed_time, ENEMY_SPEED
        score = 0
        ENEMY_SPEED = 4
        bullets = []
        enemies = []
        ship_position = [SCREEN_WIDTH//2, SCREEN_HEIGHT - SHIP_SIZE[1] * 2]
        last_shoot_time = 0
        player_alive = True
        enemy_spawn_timer = 0
        elapsed_time = 0
        pygame.mixer.music.play(-1)  # Reiniciar la música de fondo

    # Cargar y reproducir la música del menú

    menu_music = pygame.mixer.Sound('audio/Nave_espacial.mp3')  # Reemplaza 'menu_music.mp3' con el nombre de tu archivo de música del menú
    menu_music.set_volume(0.4)
    menu_music.play(-1)  # Reproducir en un bucle infinito


    def show_menu():
        menu_background = pygame.image.load('images/ad.png')  # Reemplaza con tu imagen de fondo del menú
        menu_background = pygame.transform.scale(menu_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

        # Escalar las imágenes para hacerlas más grandes

        ship_image = pygame.image.load('images/spaceship.png')
        ship_image = pygame.transform.scale(ship_image, (int(SHIP_SIZE[0] * 2), int(SHIP_SIZE[1] * 2)))

        spaceship2 = pygame.image.load('images/spaceship2.png')
        spaceship2 = pygame.transform.scale(spaceship2, (int(SHIP_SIZE[0] * 2), int(SHIP_SIZE[1] * 2)))

        # Mostrar las opciones de nave junto a las teclas correspondientes

        option1_position = (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 3.5 + 30)
        option2_position = (2.7 * SCREEN_WIDTH // 4, SCREEN_HEIGHT // 3.5 + 30)
        
        selected_ship = None
        running_menu = True

        while running_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        selected_ship = "nave1"
                        pygame.mixer.music.play(-1)
                        pygame.mixer.music.set_volume(0.4)
                        running_menu = False
                    elif event.key == pygame.K_2:
                        selected_ship = "nave2"
                        pygame.mixer.music.play(-1)
                        pygame.mixer.music.set_volume(0.4)
                        running_menu = False

            screen.blit(menu_background, (0, 0))    

            # Mostrar las opciones de nave junto a las teclas correspondientes

            screen.blit(ship_image, option1_position)
            screen.blit(spaceship2, option2_position)
            
            pygame.display.flip()
            pygame.time.Clock().tick(30)

        return selected_ship

    selected_ship = show_menu()

    if selected_ship == "nave2":
        ship_image = spaceship2
    else:
        ship_image = pygame.image.load('images/spaceship.png')
        ship_image = pygame.transform.scale(ship_image, SHIP_SIZE)#

    # Bucle principal del juego

    running = True
    player_alive = True
    enemy_spawn_timer = 0
    elapsed_time = 0  # Variable para llevar el registro del tiempo transcurrido
    menu_music.stop()

    while running and player_alive:
        # Capturar el tiempo actual

        current_time = pygame.time.get_ticks()

        # Manejar eventos

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not player_alive:
                        # Reiniciar el juego si el jugador está muerto y presiona espacio

                        reset_game()  
                        game_over_sound.play()  # Reproducir el sonido de Game Over
                    else:
                        if current_time - last_shoot_time >= BULLET_SHOOT_INTERVAL:
                            shoot_bullet(bullets, ship_position)
                            last_shoot_time = current_time

        # Manejar teclas

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            ship_position[0] -= SHIP_SPEED
        if keys[pygame.K_RIGHT]:
            ship_position[0] += SHIP_SPEED

        # Incrementar el tiempo transcurrido

        elapsed_time += 1

        # Aumentar la cantidad y velocidad de los enemigos basado en el tiempo transcurrido

        if elapsed_time % 100 == 0:
            ENEMY_SPAWN_RATE -= 1
            ENEMY_SPEED += 1

        # Actualizar la posición de los proyectiles

        update_bullets(bullets)

        # Actualizar la posición de los enemigos

        update_enemies(enemies)
        enemy_spawn_timer += 1

        if enemy_spawn_timer >= ENEMY_SPAWN_RATE:
            if score >= 100:
                add_new_enemy(enemies)
            add_enemy(enemies)
            enemy_spawn_timer = 0

        # Comprobar colisiones

        score = check_bullet_enemy_collisions(bullets, enemies, score)
        player_alive = not check_ship_enemy_collisions(ship_position, enemies)

        # Actualizar la pantalla

        screen.blit(background_image, (0, 0))

        if player_alive:
            draw_ship(screen, ship_position, advanced_ship_image if score >= 200 else None)
        else:

            pygame.mixer.music.stop()
            screen.blit(game_over_image, (0, 0))
            game_over_sound.play()
            score_text = puntaje_fuente.render(f'TU PUNTAJE FUE: {score}', True, puntaje_color)
            screen.blit(score_text, puntaje_posicion)
            pygame.display.flip()
            waiting_for_input = True

            while waiting_for_input:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        waiting_for_input = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            reset_game()
                            waiting_for_input = False

        draw_bullets(screen, bullets)
        draw_enemies(screen, enemies)
        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        pygame.display.flip()

        # Controlar los FPS

        pygame.time.Clock().tick(30)

    # Finalizar Pygame

    pygame.quit()
    sys.exit()
