import pygame
from sys import exit
import math as m

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

tire = 10
team = 100
fw = 10
rw = 10
deg = 100

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
R_S_base2 = S_start.get_rect(midbottom = (R_S_finish_line.midtop))
R_S_base3 = S_start.get_rect(midbottom = (R_S_base2.midtop))
R_S_base4 = S_start.get_rect(midbottom = (R_S_base3.midtop))
R_S_base5 = S_start.get_rect(midbottom = (R_S_base4.midtop))
R_S_base6 = S_start.get_rect(midbottom = (R_S_base5.midtop))
S_t1 = pygame.image.load("images/i-S-T1.png").convert()
R_S_t1 = S_t1.get_rect(bottomleft  = (188, -3500))

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
car = pygame.image.load("images/f1-mclaren.png").convert_alpha()
car = pygame.transform.scale(car, (27, 95))
R_car = car.get_rect(midtop = (300, 385))

Time = Minfont.render("1:25.000", False, "Black") #Boolean for capital letters

#Variables
car_pos_y_increment = float(0)
car_pos_x_increment = 0
game_active = True
angle_T1 = 0

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

        #T1
        if R_S_t1.y + 637 >= 0:
            angle_T1 = m.degrees((m.asin(abs(R_S_t1.y + 637)/1022)))
            S_t1 = pygame.transform.rotate(S_t1, angle_T1)

        print(car_pos_x_increment, car_pos_y_increment, R_S_t1.y, angle_T1)

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

        R_S_t1.x -= int (car_pos_x_increment)


        
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

        screen.blit(S_t1, R_S_t1)

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

    