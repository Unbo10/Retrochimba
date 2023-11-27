import pygame
import sys

pygame.init()

width, height = 400, 300
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Creating a surface to display inside the polygon
surface_to_blit = pygame.Surface((50, 50))
surface_to_blit.fill((0, 255, 0))  # Filling the surface with green color

# Defining a list of vertices for a polygon
polygon_vertices = [(100, 100), (200, 50), (300, 150), (250, 200), (150, 180)]

# Creating a mask for the polygon shape
polygon_mask = pygame.mask.from_surface(surface_to_blit)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # Fill the screen with white color

    # Getting the bounding rectangle for the mask
    bounding_rect = polygon_mask.get_rect()

    # Blitting the surface inside the polygon using the mask
    surface_rect = surface_to_blit.get_rect(center=bounding_rect.center)
    surface_to_blit.set_colorkey((0, 0, 0))  # Set the color key for transparency
    surface_to_blit_mask = pygame.mask.from_surface(surface_to_blit)
    surface_to_blit_mask = surface_to_blit_mask.overlap(polygon_mask, (0, 0))

    if surface_to_blit_mask:
        screen.blit(surface_to_blit, bounding_rect)

    # Drawing the polygon
    pygame.draw.polygon(screen, (255, 0, 0), polygon_vertices, 2)  # Red polygon outline

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
