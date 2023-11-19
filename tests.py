import pygame
import sys

pygame.init()

# Set up the display
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Rotating Surface")

# Create a surface and rectangle
surface = pygame.Surface((100, 100), pygame.SRCALPHA)
pygame.draw.rect(surface, (255, 0, 0), (0, 0, 100, 100))  # Red rectangle on transparent surface
rect = surface.get_rect(center=(200, 150))  # Center the rectangle

angle = 0  # Initial angle

clock = pygame.time.Clock()  # For controlling the frame rate

rotation_speed = 2  # Speed of rotation

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((50, 50, 50))  # Fill the screen with a dark gray color

    # Rotate the surface
    rotated_surface = pygame.transform.rotate(surface, angle)
    rotated_rect = rotated_surface.get_rect(center=rect.center)

    # Draw the rotated surface on the screen
    screen.blit(rotated_surface, rotated_rect.topleft)  # Use topleft corner for blitting

    angle += rotation_speed  # Increment the angle for rotation

    pygame.display.flip()
    clock.tick(60)  # Limit frame rate to 60 FPS

pygame.quit()
sys.exit()
