import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Retrochimba")
clock = pygame.time.Clock()
Minfont = pygame.font.Font('Minecraft.ttf',40)

track = pygame.image.load("images/ind-r-2.png").convert()
Time = Minfont.render("1:25.000", False, "Black") #Boolean for capital letters

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(track, (-56.5, 0))
    screen.blit(Time, (225,15))

    pygame.display.update()
    clock.tick(60)