import pygame

pygame.init()

# Set up the display without a title bar
width, height = 600, 500
flags = pygame.NOFRAME  # Create a window without a title bar
screen = pygame.display.set_mode((width, height), flags)

background_color = (100, 100, 255)  # Define your desired background color

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_color)
    # Other game logic/rendering

    pygame.display.flip()

pygame.quit()