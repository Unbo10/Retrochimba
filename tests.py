import pygame
import sys
import math

pygame.init()

# Set up the screen
width, height = 400, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Rotating Surface')

# Create a surface
S_t1 = pygame.Surface((100, 100))  # Creating a square surface for demonstration
S_t1.fill((255, 0, 0))  # Fill the surface with red (RGB: 255, 0, 0)
S_t1_rect = S_t1.get_rect(center=(width // 2, height // 2))

angle_in_radians = 0  # Start with 0 radians
rotation_speed = 0.01  # Adjust rotation speed as needed

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Convert radians to degrees
    angle_in_degrees = math.degrees(angle_in_radians)

    # Rotate the surface
    S_rotating_t1 = pygame.transform.rotate(S_t1, angle_in_degrees)
    rotated_rect = S_rotating_t1.get_rect(center=S_t1_rect.center)

    screen.fill((255, 255, 255))  # Fill the screen with white
    screen.blit(S_rotating_t1, rotated_rect.topleft)

    angle_in_radians += rotation_speed  # Increment the angle for continuous rotation

    pygame.display.flip()

pygame.quit()
sys.exit()