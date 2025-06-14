import pygame
from src.world.tilemap import load_tiles, generate_tile_matrix, draw_map
from src.world.layering import load_structures, draw_structures

pygame.init()
screen = pygame.display.set_mode((1024, 768))
clock = pygame.time.Clock()

tiles = load_tiles()
tile_matrix = generate_tile_matrix()
structures = load_structures()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    draw_map(screen, tile_matrix, tiles)

    draw_structures(screen, structures)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()