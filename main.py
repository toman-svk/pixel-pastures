import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Pygame Project")

# Set up clock for framerate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    clock.tick(60)  # 60 FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color
    screen.fill((30, 30, 30))  # dark gray background

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()