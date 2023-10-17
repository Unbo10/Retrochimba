import pygame
from sys import exit
import math as m

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Retrochimba")
clock = pygame.time.Clock()
Minfont = pygame.font.Font('Minecraft.ttf',40)

track = pygame.image.load("images/ind-r-2.png").convert_alpha()
track.set_alpha(255)
track_curve_rect = track.get_rect(center = (307, 250))

car1 = pygame.image.load("images/mclaren-f1.png").convert_alpha()
cari = pygame.transform.scale(car1, (27, 95))
carR = cari.get_rect(midtop = (250, 385)) #Rectangles are useful for collisions and for getting acurate measurements of where a surface is. Therefore, it will be used in this project
# car_pos_x = 294
# car_pos_y = 385 Can be used with a surface, but is not useful with a rectangle
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

        if carR.y < 100:
            game_active = False

        screen.blit(track, (-56.5, 0))
        # car_pos_y -= 4
        # screen.blit(car, (car_pos_x,car_pos_y))
        carR.y -= car_pos_y_increment
        carR.x += car_pos_x_increment
        screen.blit(cari, carR)
        # pygame.draw.arc(track, (200, 200, 200), track_curve_rect, m.pi * 0.5, m.pi, 50)

        screen.blit(Time, (225,15))
    
    else:
        track.set_alpha(100)
        print(track.get_alpha())

    pygame.display.update()
    clock.tick(60)