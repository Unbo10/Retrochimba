import pygame
from sys import exit
import math as m

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Retrochimba")
clock = pygame.time.Clock()
Minfont = pygame.font.Font('Minecraft.ttf',40)

# Default sizes for images to scale them
def_size_S = (225, 500)
def_size_S_L= (245, 500)
def_size_S_R = (246, 500)

#BACKGROUND
S_base = pygame.image.load("images/i-S.png").convert_alpha()
S_base = pygame.transform.scale(S_base, def_size_S)
R_S_base = S_base.get_rect(center = (300, 250))

S_barriers_L = pygame.image.load("images/i-S-Lbarrier.png").convert_alpha()
S_barriers_L = pygame.transform.scale(S_barriers_L, def_size_S_L)
R_S_barriers_L1 = S_barriers_L.get_rect(midright = (188, 250)) # Problem: images are not loading and they are "waving". Look at the tutorial because that did not happen there
R_S_barriers_L2 = S_barriers_L.get_rect(midright = (188, -250))
R_S_barriers_L3 = S_barriers_L.get_rect(midright = (188, -750))
R_S_barriers_L4 = S_barriers_L.get_rect(midright = (188, -1250))

S_pits = pygame.image.load("images/i-S-pits-NOlogos.png").convert_alpha()
S_pits = pygame.transform.scale(S_pits, def_size_S_R)
R_S_pits1 = S_pits.get_rect(midleft = (413, 250))
S_pits_logos = pygame.image.load("images/i-S-pits-logos.png").convert_alpha()
S_pits_logos = pygame.transform.scale(S_pits_logos, def_size_S_R)
R_S_pits_logos = S_pits_logos.get_rect(midleft = (413, -250))
R_S_pits2 = S_pits.get_rect(midleft = (413, -750))
S_pits_salida = pygame.image.load("images/i-S-pits-NOlogos.png").convert_alpha() #Cambiar por salida de pits
S_pits_salida = pygame.transform.scale(S_pits_salida, def_size_S_R)
R_S_pits_salida = S_pits.get_rect(midleft = (413, -1250))

#CAR AND OTHERS
car = pygame.image.load("images/f1-mclaren.png").convert_alpha()
car = pygame.transform.scale(car, (27, 95))
R_car = car.get_rect(midtop = (300, 385))

Time = Minfont.render("1:25.000", False, "Black") #Boolean for capital letters

#Variables
car_pos_y_increment = 0
car_pos_x_increment = 0
game_active = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if (event.type == pygame.KEYDOWN):    
        #     if ((event.key == pygame.K_w) or (event.key == pygame.K_UP)):
        #         car_pos_y_increment = 1
        #     if ((event.key == pygame.K_s) or (event.key == pygame.K_DOWN)) and (car_pos_y_increment > 0):
        #         car_pos_y_increment -= 0.25
        # if (event.type != pygame.KEYDOWN) and (car_pos_y_increment > 0):
        #         car_pos_y_increment -= 0.25

    if game_active == True:
        keys = pygame.key.get_pressed() #Get all the keys getting pressed in every frame
        car_pos_x_increment = 0
        if keys[pygame.K_UP]:
            car_pos_y_increment += 0.05 #Replace for function of acceleration
        elif (car_pos_y_increment > 0):
            car_pos_y_increment -= 0.10
            if keys[pygame.K_LEFT]:
                    car_pos_x_increment -= 1
            elif keys[pygame.K_RIGHT]:
                car_pos_x_increment += 1 
            else:
                car_pos_x_increment = 0

        if R_car.y < 100:
            game_active = False

        #SHOW BACKGROUND
        R_S_base.x -= car_pos_x_increment
        R_S_barriers_L1.x -= car_pos_x_increment
        R_S_barriers_L2.x -= car_pos_x_increment
        R_S_barriers_L3.x -= car_pos_x_increment
        R_S_barriers_L4.x -= car_pos_x_increment
        R_S_pits1.x -= car_pos_x_increment
        R_S_pits_logos.x -= car_pos_x_increment
        R_S_pits2.x -= car_pos_x_increment
        R_S_pits_salida.x -= car_pos_x_increment

        R_S_base.y += car_pos_y_increment
        R_S_barriers_L1.y += car_pos_y_increment
        R_S_barriers_L2.y += car_pos_y_increment
        R_S_barriers_L3.y += car_pos_y_increment
        R_S_barriers_L4.y += car_pos_y_increment
        R_S_pits1.y += car_pos_y_increment
        R_S_pits_logos.y += car_pos_y_increment
        R_S_pits2.y += car_pos_y_increment
        R_S_pits_salida.y += car_pos_y_increment

        screen.blit(S_base, R_S_base)
        screen.blit(S_barriers_L, R_S_barriers_L1)
        screen.blit(S_barriers_L, R_S_barriers_L2)
        screen.blit(S_barriers_L, R_S_barriers_L3)
        screen.blit(S_barriers_L, R_S_barriers_L4)
        screen.blit(S_pits, R_S_pits1)
        screen.blit(S_pits_logos, R_S_pits_logos)
        screen.blit(S_pits, R_S_pits2)
        screen.blit(S_pits_salida, R_S_pits_salida)

        #SHOW CAR
        screen.blit(car, R_car)

        # pygame.draw.arc(track, (200, 200, 200), track_curve_rect, m.pi * 0.5, m.pi, 50)

        screen.blit(Time, (225,15))
    
    else:
        S_base.set_alpha(100)
        print(S_base.get_alpha())

    pygame.display.update()
    clock.tick(60)