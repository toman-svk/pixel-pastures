import pygame
from src.world.tilemap import load_tiles, generate_tile_matrix, draw_map
from src.world.layering import load_structures, draw_structures
from src.ui.popup import PopupManager
from src.entities.player import Player

pygame.init()
screen = pygame.display.set_mode((1024, 768))
clock = pygame.time.Clock()

tiles = load_tiles()
tile_matrix = generate_tile_matrix()
structures = load_structures()
font = pygame.font.SysFont(None, 36)
popup = PopupManager(font=font)
player = Player()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for s in structures:
                if hasattr(s, 'get_rect') and s.get_rect().collidepoint(mouse_x, mouse_y):
                    popup.show_popup("Crop harvested!")
                    structures.remove(s)  # 💥 Remove the clicked structure
                    break # Optional: only remove one at a time

    screen.fill((0, 0, 0))
    draw_map(screen, tile_matrix, tiles)
    draw_structures(screen, structures)
    popup.draw(screen)

    keys = pygame.key.get_pressed()
    player.handle_input(keys)
    player.draw(screen)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()