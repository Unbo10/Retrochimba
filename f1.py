import pygame
from sys import exit
import math as m

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Retrochimba")
clock = pygame.time.Clock()
Minfont = pygame.font.Font('Minecraft.ttf',40)

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
S_end = pygame.image.load("images/i-S.png").convert_alpha()
S_end = pygame.transform.scale(S_end, size_S)
R_S_end = S_end.get_rect(midbottom = (R_S_finish_line.midtop))

S_barriers_L = pygame.image.load("images/i-S-Lbarrier.png").convert_alpha()
S_barriers_L = pygame.transform.scale(S_barriers_L, size_S_L)
R_S_barriers_L1 = S_barriers_L.get_rect(midright = (188, 250)) # Problem: images are not loading and they are "waving". Look at the tutorial because that did not happen there
R_S_barriers_L2 = S_barriers_L.get_rect(midright = (188, -250))
R_S_barriers_L3 = S_barriers_L.get_rect(midright = (188, -750))
R_S_barriers_L4 = S_barriers_L.get_rect(midright = (188, -1250))

S_pits = pygame.image.load("images/i-S-pits-NOlogos.png").convert_alpha()
S_pits = pygame.transform.scale(S_pits, size_S_R)
R_S_pits1 = S_pits.get_rect(midleft = (413, 250))
S_pits_logos = pygame.image.load("images/i-S-pits-logos.png").convert_alpha()
S_pits_logos = pygame.transform.scale(S_pits_logos, size_S_R)
R_S_pits_logos = S_pits_logos.get_rect(midleft = (413, -250))
R_S_pits2 = S_pits.get_rect(midleft = (413, -750))
S_pits_exit = pygame.image.load("images/i-S-pits-exit.png").convert_alpha() #Cambiar por salida de pits
S_pits_exit = pygame.transform.scale(S_pits_exit, size_S_R)
R_S_pits_exit = S_pits.get_rect(midleft = (413, -1250))

#CAR AND OTHERS
car = pygame.image.load("images/f1-mclaren.png").convert_alpha()
car = pygame.transform.scale(car, (27, 95))
R_car = car.get_rect(midtop = (300, 385))

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
        # if (event.type == pygame.KEYDOWN):    
        #     if ((event.key == pygame.K_w) or (event.key == pygame.K_UP)):
        #         car_pos_y_increment = 1
        #     if ((event.key == pygame.K_s) or (event.key == pygame.K_DOWN)) and (car_pos_y_increment > 0):
        #         car_pos_y_increment -= 0.25
        # if (event.type != pygame.KEYDOWN) and (car_pos_y_increment > 0):
        #         car_pos_y_increment -= 0.25
    screen.fill((0, 0, 0))

    if game_active == True:
        keys = pygame.key.get_pressed() #Get all the keys getting pressed in every frame
        car_pos_x_increment = 0
        if keys[pygame.K_UP]:
            car_pos_y_increment += 0.10 #Replace for function of acceleration
        elif (car_pos_y_increment > 0):
            car_pos_y_increment -= 0.05
            if keys[pygame.K_LEFT]:
                car_pos_x_increment -= 1
            elif keys[pygame.K_RIGHT]:
                car_pos_x_increment += 1 
            else:
                car_pos_x_increment = 0

        if R_car.y < 100:
            game_active = False

        print(R_S_start.top - R_S_grid.bottom, car_pos_y_increment)

        #SHOW BACKGROUND
        R_S_start.x -= int(car_pos_x_increment)
        R_S_barriers_L1.x -= int(car_pos_x_increment)
        R_S_pits1.x -= int(car_pos_x_increment)
        R_S_grid.x -= int(car_pos_x_increment)
        R_S_barriers_L2.x -= int(car_pos_x_increment)
        R_S_pits_logos.x -= int(car_pos_x_increment)
        R_S_finish_line.x -= int(car_pos_x_increment)
        R_S_barriers_L3.x -= int(car_pos_x_increment)
        R_S_pits2.x -= int(car_pos_x_increment)
        R_S_end.x -= int(car_pos_x_increment)
        R_S_barriers_L4.x -= int(car_pos_x_increment)
        R_S_pits_exit.x -= int(car_pos_x_increment)
        
        R_S_start.y += int(car_pos_y_increment)
        R_S_barriers_L1.y += int(car_pos_y_increment)
        R_S_pits1.y += int(car_pos_y_increment)
        R_S_grid.y += int(car_pos_y_increment)
        R_S_barriers_L2.y += int(car_pos_y_increment)
        R_S_pits_logos.y += int(car_pos_y_increment)
        R_S_finish_line.y += int(car_pos_y_increment)
        R_S_barriers_L3.y += int(car_pos_y_increment)
        R_S_pits2.y += int(car_pos_y_increment)
        R_S_end.y += int(car_pos_y_increment)
        R_S_barriers_L4.y += int(car_pos_y_increment)
        R_S_pits_exit.y += int(car_pos_y_increment)

        screen.blit(S_start, R_S_start)
        screen.blit(S_barriers_L, R_S_barriers_L1)        
        screen.blit(S_pits, R_S_pits1)
        screen.blit(S_grid, R_S_grid)
        screen.blit(S_barriers_L, R_S_barriers_L2)
        screen.blit(S_pits_logos, R_S_pits_logos)
        screen.blit(S_finish_line, R_S_finish_line)
        screen.blit(S_barriers_L, R_S_barriers_L3)
        screen.blit(S_pits, R_S_pits2)
        screen.blit(S_end, R_S_end)
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

    