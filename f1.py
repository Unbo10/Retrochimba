import pygame
from sys import exit
import math as m
from moviepy.editor import * 

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((600, 500))
logo = pygame.image.load("images/logo-title-bar-FC.png").convert_alpha()
pygame.display.set_icon(logo)
pygame.display.set_caption("Fórmula Chimba")
clock = pygame.time.Clock()
Minfont = pygame.font.Font('Minecraft.ttf',40)
video = VideoFileClip("images/This-is-Formula-One-Pixelated.mp4")


#Speed = acc + 25m/s
def acceleration(x_increment, y_increment, tires, team, fw, rw, deg):
    acc = list((0, 0))
    if (x_increment != 0):
        acc[0] = x_increment * ((5*(fw + rw)) + deg + (10 * tires) + team) / 500
    if (y_increment > 0):
        acc[1] = y_increment * ((5*(fw + rw)) + deg + (10 * tires) + team) / 500
    if (y_increment < 0):
        acc[1] = y_increment * ((5*(fw + rw)) + deg + (10 * tires) + team) / 100
    return acc
    #Probably we will have to return acceleration on the y-axis and on the x-axis
def reverse(y_increment, aum_y, tires, team, fw, rw, deg):
    if y_increment >= -7:
        return aum_y * ((5*(fw + rw)) + deg + (10 * tires) + team) / 100
    else:
        return 0
    
def menu(video):
    car_size = (128, 326)
    pygame.mixer.music.load('audio/This-is-Formula-One-Pixelated-Audio.mp3')
    pygame.mixer.music.set_volume(0.25)
    pygame.mixer.music.play()
    frame_rate = 25
    current_time = 0
    Minfont_cars = pygame.font.Font('Minecraft.ttf', 16)
    Minfont_title = pygame.font.Font('Minecraft.ttf', 25)

    S_logo = pygame.image.load("images/logo-FC.png").convert_alpha()
    S_logo = pygame.transform.scale(S_logo, (308, 56))
    R_S_logo = S_logo.get_rect(midtop = (300, 13))

    transparent_surface = pygame.Surface((230, 40), pygame.SRCALPHA)
    pygame.draw.rect(transparent_surface, (255, 255, 255, 128), transparent_surface.get_rect())
    R_S_car_text = pygame.Rect(185, 80, 250, 40)
    S_car_text = Minfont_title.render("Choose your car:", None, "Black")

    S_Mercedes = pygame.image.load("images/Mercedes-FC-softs.png").convert_alpha()
    S_Mercedes = pygame.transform.scale(S_Mercedes,car_size)
    R_S_Mercedes = S_Mercedes.get_rect(topleft = (24, 127))
    R_S_text_Mercedes = pygame.Rect(R_S_Mercedes.left, R_S_Mercedes.bottom - 9, car_size[0], 30)
    Mercedes_text = Minfont_cars.render("Mercedes W14", None, "Black")

    S_Ferrari = pygame.image.load("images/Ferrari-FC-softs.png").convert_alpha()
    S_Ferrari = pygame.transform.scale(S_Ferrari, car_size)
    R_S_Ferrari = S_Ferrari.get_rect(midtop = (300, 127))
    R_S_text_Ferrari = pygame.Rect(R_S_Ferrari.left, R_S_Ferrari.bottom - 9, car_size[0], 30)
    Ferrari_text = Minfont_cars.render("Ferrari SF-23", None, "Black")

    S_Mclaren = pygame.image.load("images/McLaren-FC-softs.png").convert_alpha()
    S_Mclaren = pygame.transform.scale(S_Mclaren, car_size)
    R_S_Mclaren = S_Mclaren.get_rect(topright = (577, 127))
    R_S_text_Mclaren = pygame.Rect(R_S_Mclaren.left, R_S_Mclaren.bottom - 9, car_size[0], 30)
    Mclaren_text = Minfont_cars.render("McLaren MCL60", None, "Black")
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.fill((0, 0, 0))
        time_counter = pygame.time.get_ticks()
        print(time_counter)

        if current_time < video.duration:
            video_frame = video.get_frame(current_time)
            pygame_frame = pygame.image.fromstring(video_frame.tobytes(), video.size, "RGB")
            screen.blit(pygame_frame, (0, 0))
            current_time += 1 / frame_rate  # Increment time by 1 frame at the specified frame rate
        else:
            current_time = 0

        if time_counter > 500: #CHANGE TO 5000 WHEN FINISHED
            mouse_pos = pygame.mouse.get_pos()
            if R_S_Mercedes.collidepoint(mouse_pos):
                print(mouse_pos)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print("Y")
                        pygame.mixer.music.stop()
                        video.close()
                        play("mercedes")
                        car_set_up("mercedes")
            if R_S_Ferrari.collidepoint(mouse_pos):
                print(mouse_pos)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print("Y")
                        pygame.mixer.music.stop()
                        video.close()
                        car_set_up("ferrari")  
            if R_S_Mclaren.collidepoint(mouse_pos):
                print(mouse_pos)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print("Y")
                        pygame.mixer.music.stop()
                        video.close()
                        car_set_up("mclaren")  

            screen.blit(S_logo, R_S_logo)
            screen.blit(transparent_surface, (185, 80))        
            screen.blit(S_car_text, (R_S_car_text.left + 10, R_S_car_text.top + 10))
            pygame.draw.rect(screen, (12, 229, 192), R_S_text_Mercedes) #If you have time, design a curved botton
            screen.blit(Mercedes_text, (R_S_text_Mercedes.left + 12, R_S_text_Mercedes.top + 9))
            pygame.draw.rect(screen, (239, 26, 45), R_S_text_Ferrari) #If you have time, design a curved botton
            screen.blit(Ferrari_text, (R_S_text_Ferrari.left + 12, R_S_text_Ferrari.top + 9))
            pygame.draw.rect(screen, (255, 128, 0), R_S_text_Mclaren) #If you have time, design a curved botton
            screen.blit(Mclaren_text, (R_S_text_Mclaren.left + 2, R_S_text_Mclaren.top + 9))
            screen.blit(S_Mercedes, R_S_Mercedes)
            screen.blit(S_Ferrari, R_S_Ferrari)
            screen.blit(S_Mclaren, R_S_Mclaren)
            

        pygame.display.update()
        clock.tick(25)


#################################################################################################################       

# *** SET UP OF THE CAR ***

def car_set_up (team_name):

    screen.fill((0, 0, 0))

    Minfont_cars = pygame.font.Font('Minecraft.ttf', 16)
    Minfont_title = pygame.font.Font('Minecraft.ttf', 25)
    car_size = (128, 316)

    S_logo = pygame.image.load("images/logo-FC.png").convert_alpha()
    S_logo = pygame.transform.scale(S_logo, (308, 56))
    R_S_logo = S_logo.get_rect(midtop = (300, 13))

    transparent_surface = pygame.Surface((230, 40), pygame.SRCALPHA)
    pygame.draw.rect(transparent_surface, (255, 255, 255, 128), transparent_surface.get_rect())
    R_S_title = pygame.Rect(185, 80, 250, 40)
    S_title = Minfont_title.render("Choose your car:", None, "Black")

    if team_name == "mercedes":
        S_car = pygame.image.load("images/Mercedes-FC-softs.png").convert_alpha()
        S_car = pygame.transform.scale(S_car,car_size)
        R_S_car = S_car.get_rect(topleft = (24, 127))
        R_S_car_text = pygame.Rect(R_S_car.left, R_S_car.bottom - 9, car_size[0], 30)
        car_text = Minfont_cars.render("Mercedes W14", None, "Black")
    elif team_name == "ferrari":
        S_car = pygame.image.load("images/Ferrari-FC-softs.png").convert_alpha()
        S_car = pygame.transform.scale(S_car, car_size)
        R_S_car = S_car.get_rect(topleft = (24, 127))
        R_S_car_text = pygame.Rect(R_S_car.left, R_S_car.bottom - 9, car_size[0], 30)
        S_car_text = Minfont_cars.render("Ferrari SF-23", None, "Black")  
        print("F")
    elif team_name == "mclaren":
        S_car = pygame.image.load("images/McLaren-FC-softs.png").convert_alpha()
        S_car = pygame.transform.scale(S_car, car_size)
        R_S_car = S_car.get_rect(topleft = (24, 127))
        R_S_car_text = pygame.Rect(R_S_car.left, R_S_car.bottom - 9, car_size[0], 30)
        car_text = Minfont_cars.render("McLaren MCL60", None, "Black")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.fill((0, 0, 0))
        # print("S")

        screen.blit(S_car, R_S_car)
        screen.blit(S_logo, R_S_logo)
        screen.blit(S_car_text, R_S_car_text)

        pygame.display.update()
        clock.tick(30)



##################################################################################################################       

        
def play (team_name):

    tire = 10
    fw = 10
    rw = 10
    deg = 100

    # Default sizes for images to scale them
    size_S = (225, 500)
    size_S_L= (245, 500)
    size_S_R = (246, 500)

    #BACKGROUND

    #Track
    S_start = pygame.image.load("images/i-S.png").convert_alpha()
    S_start = pygame.transform.scale(S_start, size_S)
    R_S_start = S_start.get_rect(center = (300, 250))
    S_grid = pygame.image.load("images/i-S-grid.png").convert_alpha()
    S_grid = pygame.transform.scale(S_grid, size_S)
    R_S_grid = S_grid.get_rect(midbottom = (R_S_start.midtop))
    S_finish_line = pygame.image.load("images/i-S-finish-line.png").convert_alpha()
    S_finish_line = pygame.transform.scale(S_finish_line, size_S)
    R_S_finish_line = S_finish_line.get_rect(midbottom = (R_S_grid.midtop))
    R_S_base2 = S_start.get_rect(midbottom = (R_S_finish_line.midtop))
    R_S_base3 = S_start.get_rect(midbottom = (R_S_base2.midtop))
    R_S_base4 = S_start.get_rect(midbottom = (R_S_base3.midtop))
    R_S_base5 = S_start.get_rect(midbottom = (R_S_base4.midtop))
    S_t1 = pygame.image.load("images/i-S-T1.png").convert()
    R_S_t1 = S_t1.get_rect(bottomleft = (188, -3500))
    R_S_base6 = S_start.get_rect(topleft = (R_S_t1.bottomleft))

    S_barriers_L = pygame.image.load("images/i-S-Lbarrier.png").convert_alpha()
    S_barriers_L = pygame.transform.scale(S_barriers_L, size_S_L)
    R_S_barriers_L1 = S_barriers_L.get_rect(midright = (188, 250))
    R_S_barriers_L2 = S_barriers_L.get_rect(midright = (188, -250))
    R_S_barriers_L3 = S_barriers_L.get_rect(midright = (188, -750))
    R_S_barriers_L4 = S_barriers_L.get_rect(midright = (188, -1250))
    R_S_barriers_L5 = S_barriers_L.get_rect(midright = (188, -1750))
    R_S_barriers_L6 = S_barriers_L.get_rect(midright = (188, -2250))
    R_S_barriers_L7 = S_barriers_L.get_rect(midright = (188, -2750))
    R_S_barriers_L8 = S_barriers_L.get_rect(midright = (188, -3250))

    S_pits = pygame.image.load("images/i-S-pits-NOlogos.png").convert_alpha()
    S_pits = pygame.transform.scale(S_pits, size_S_R)
    R_S_pits1 = S_pits.get_rect(midleft = (413, 250))
    S_pits_logos = pygame.image.load("images/i-S-pits-logos.png").convert_alpha()
    S_pits_logos = pygame.transform.scale(S_pits_logos, size_S_R)
    R_S_pits_logos = S_pits_logos.get_rect(midleft = (413, -250))
    R_S_pits_logos2 = S_pits_logos.get_rect(midleft = (413, -750))
    R_S_pits2 = S_pits.get_rect(midleft = (413, -1250))
    R_S_pits3 = S_pits.get_rect(midleft = (413, -1750))
    R_S_pits4 = S_pits.get_rect(midleft = (413, -2250))
    R_S_pits5 = S_pits.get_rect(midleft = (413, -2750))
    S_pits_exit = pygame.image.load("images/i-S-pits-exit.png").convert_alpha()
    S_pits_exit = pygame.transform.scale(S_pits_exit, size_S_R)
    R_S_pits_exit = S_pits.get_rect(midleft = (413, -3250))


    #CAR AND OTHERS
    if team_name == "mclaren":
        car = pygame.image.load("images/f1-mclaren.png").convert_alpha()
        car = pygame.transform.scale(car, (27, 95))
        R_car = car.get_rect(midtop = (300, 385))
        team = 9
    elif team_name == "ferrari":
        car = pygame.image.load("images/f1-ferrari.png").convert_alpha()
        car = pygame.transform.scale(car, (27, 95))
        R_car = car.get_rect(midtop = (300, 385))
        team = 8
    elif team_name == "mercedes":
        car = pygame.image.load("images/f1-mercedes.png").convert_alpha()
        car = pygame.transform.scale(car, (27, 95))
        R_car = car.get_rect(midtop = (300, 385))
        team = 8

    Time = Minfont.render("1:25.000", False, "Black") #Boolean for capital letters

    #Variables
    car_pos_y_increment = float(0)
    car_pos_x_increment = 0
    game_active = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.fill((0, 0, 0))

        if game_active == True:
            keys = pygame.key.get_pressed() #Get all the keys getting pressed in every frame
            if keys[pygame.K_UP]:
                if keys[pygame.K_LEFT]:
                    aum_x, aum_y = acceleration(-0.10, 0.25, tire, team, fw, rw, deg)
                    car_pos_y_increment += aum_y
                    car_pos_x_increment += aum_x
                elif keys[pygame.K_RIGHT]:
                    aum_x, aum_y = acceleration(0.10, 0.25, tire, team, fw, rw, deg)
                    car_pos_y_increment += aum_y
                    car_pos_x_increment += aum_x 
                else:
                    car_pos_x_increment = 0
                    car_pos_y_increment += acceleration(0, 0.25, tire, team, fw, rw, deg)[1] 
            elif keys[pygame.K_DOWN] and (car_pos_y_increment >= 0):
                if keys[pygame.K_LEFT]:
                    aum_x, aum_y = acceleration(-0.15, -0.10, tire, team, fw, rw, deg)
                    car_pos_x_increment += aum_x
                    car_pos_y_increment += aum_y
                if keys[pygame.K_RIGHT]:
                    aum_x, aum_y = acceleration(0.15, -0.10, tire, team, fw, rw, deg)
                    car_pos_x_increment += aum_x
                    car_pos_y_increment += aum_y
                else:
                    car_pos_x_increment = 0
                    car_pos_y_increment += acceleration(0, -0.15, tire, team, fw, rw, deg)[1]
            elif car_pos_y_increment > 0:
                if keys[pygame.K_LEFT]:
                    aum_x, aum_y = acceleration (-0.15, -0.025, tire, team, fw, rw, deg)
                    car_pos_x_increment += aum_x
                    car_pos_y_increment += aum_y
                elif keys[pygame.K_RIGHT]:
                    aum_x, aum_y = acceleration (0.15, -0.025, tire, team, fw, rw, deg)
                    car_pos_x_increment += aum_x
                    car_pos_y_increment += aum_y
                else:
                    car_pos_x_increment = 0
                    car_pos_y_increment += (0, -0.025, tire, team, fw, rw, deg)[1]
            elif car_pos_y_increment < 0:
                if keys[pygame.K_DOWN] and keys[pygame.K_r]:
                    car_pos_y_increment += reverse(car_pos_y_increment, -0.10, tire, team, fw, rw, deg)
                    if keys[pygame.K_LEFT]:
                        aum_x= acceleration (-0.15, 0, tire, team, fw, rw, deg)[0]
                        car_pos_x_increment += aum_x
                    elif keys[pygame.K_RIGHT]:
                        aum_x= acceleration (0.15, 0, tire, team, fw, rw, deg)[0]
                        car_pos_x_increment += aum_x
                elif car_pos_y_increment >= 0.5 or car_pos_y_increment <= -0.5:
                    if keys[pygame.K_LEFT]:
                        aum_x= acceleration (-0.15, 0, tire, team, fw, rw, deg)[0]
                        car_pos_x_increment += aum_x
                    elif keys[pygame.K_RIGHT]:
                        aum_x= acceleration (0.15, 0, tire, team, fw, rw, deg)[0]
                        car_pos_x_increment += aum_x
                    else:
                        car_pos_x_increment = 0
                        car_pos_y_increment += (0, 0.025, tire, team, fw, rw, deg)[1]
                else:
                    car_pos_x_increment = 0
            else:
                car_pos_x_increment = 0

            # if car_pos_x_increment < 0:
            #     car = pygame.transform.rotate(car, 1)
            # elif car_pos_x_increment > 0:
            #     car = pygame.transform.rotate(car, -1)

            #T1
            if R_S_t1.y + 637 > 0:
                print((m.asin(abs(R_S_t1.y + 637)/1022)))
                S_t1 = pygame.image.load("images/i-S-T1.png").convert()
                S_t1 = pygame.transform.rotate(S_t1, m.degrees(m.asin(abs(R_S_t1.y + 637)/1022)))
                S_start = pygame.image.load("images/i-S.png").convert_alpha()
                S_start = pygame.transform.scale(S_start, size_S)
                S_start = pygame.transform.rotate(S_start, m.degrees(m.asin(abs(R_S_t1.y + 637)/1022)))

            #FOCUS ON THE OTHER STUFF!!!!!!

            print(car_pos_x_increment, car_pos_y_increment)

            #SHOW BACKGROUND
            R_S_start.x -= int(car_pos_x_increment)
            R_S_barriers_L1.x -= int(car_pos_x_increment)
            R_S_pits1.x -= int(car_pos_x_increment)

            R_S_base2.x -= int(car_pos_x_increment)
            R_S_barriers_L2.x -= int(car_pos_x_increment)
            R_S_pits2.x -= int(car_pos_x_increment)
            R_S_grid.x -= int(car_pos_x_increment)
            R_S_barriers_L3.x -= int(car_pos_x_increment)
            R_S_pits_logos.x -= int(car_pos_x_increment)
            R_S_finish_line.x -= int(car_pos_x_increment)
            R_S_barriers_L4.x -= int(car_pos_x_increment)
            R_S_pits_logos2.x -= int(car_pos_x_increment)
            R_S_base3.x -= int(car_pos_x_increment)
            R_S_barriers_L5.x -= int(car_pos_x_increment)
            R_S_pits3.x -= int(car_pos_x_increment)
            R_S_base4.x -= int(car_pos_x_increment)
            R_S_barriers_L6.x -= int(car_pos_x_increment)
            R_S_pits4.x -= int(car_pos_x_increment)
            R_S_base5.x -= int(car_pos_x_increment)
            R_S_barriers_L7.x -= int(car_pos_x_increment)
            R_S_pits5.x -= int(car_pos_x_increment)
            R_S_base6.x -= int(car_pos_x_increment)
            R_S_barriers_L8.x -= int(car_pos_x_increment)
            R_S_pits_exit.x -= int(car_pos_x_increment)

            # R_S_t1.x -= int (car_pos_x_increment)


            
            R_S_start.y += int(car_pos_y_increment)
            R_S_barriers_L1.y += int(car_pos_y_increment)
            R_S_pits1.y += int(car_pos_y_increment)

            R_S_base2.y += int(car_pos_y_increment)
            R_S_barriers_L2.y += int(car_pos_y_increment)
            R_S_pits2.y += int(car_pos_y_increment)
            R_S_grid.y += int(car_pos_y_increment)
            R_S_barriers_L3.y += int(car_pos_y_increment)
            R_S_pits_logos.y += int(car_pos_y_increment)
            R_S_finish_line.y += int(car_pos_y_increment)
            R_S_barriers_L4.y += int(car_pos_y_increment)
            R_S_pits_logos2.y += int(car_pos_y_increment)
            R_S_base3.y += int(car_pos_y_increment)
            R_S_barriers_L5.y += int(car_pos_y_increment)
            R_S_pits3.y += int(car_pos_y_increment)
            R_S_base4.y += int(car_pos_y_increment)
            R_S_barriers_L6.y += int(car_pos_y_increment)
            R_S_pits4.y += int(car_pos_y_increment)
            R_S_base5.y += int(car_pos_y_increment)
            R_S_barriers_L7.y += int(car_pos_y_increment)
            R_S_pits5.y += int(car_pos_y_increment)
            R_S_base6.y += int(car_pos_y_increment)
            R_S_barriers_L8.y += int(car_pos_y_increment)
            R_S_pits_exit.y += int(car_pos_y_increment)

            R_S_t1.y += int(car_pos_y_increment)


            screen.blit(S_t1, R_S_t1)

            screen.blit(S_start, R_S_start)
            screen.blit(S_barriers_L, R_S_barriers_L1)        
            screen.blit(S_pits, R_S_pits1)

            screen.blit(S_start, R_S_base2)
            screen.blit(S_barriers_L, R_S_barriers_L2)
            screen.blit(S_pits_logos, R_S_pits_logos)
            screen.blit(S_grid, R_S_grid)
            screen.blit(S_barriers_L, R_S_barriers_L3)
            screen.blit(S_pits_logos, R_S_pits_logos2)
            screen.blit(S_finish_line, R_S_finish_line)
            screen.blit(S_barriers_L, R_S_barriers_L4)
            screen.blit(S_pits, R_S_pits2)
            screen.blit(S_start, R_S_base3)
            screen.blit(S_barriers_L, R_S_barriers_L5)
            screen.blit(S_pits, R_S_pits3)
            screen.blit(S_start, R_S_base4)
            screen.blit(S_barriers_L, R_S_barriers_L6)
            screen.blit(S_pits, R_S_pits4)
            screen.blit(S_start, R_S_base5)
            screen.blit(S_barriers_L, R_S_barriers_L7)
            screen.blit(S_pits, R_S_pits5)
            screen.blit(S_start, R_S_base6)
            screen.blit(S_barriers_L, R_S_barriers_L8)
            screen.blit(S_pits_exit, R_S_pits_exit)



            screen.blit(S_start, R_S_base2)
            screen.blit(S_barriers_L, R_S_barriers_L4)
            screen.blit(S_pits_exit, R_S_pits_exit)

            #SHOW CAR
            screen.blit(car, R_car)

            screen.blit(Time, (225,15))
            pygame.display.update()
            clock.tick(30)
        else:
            S_finish_line.set_alpha(100)
            print(S_finish_line.get_alpha())

menu(video)      