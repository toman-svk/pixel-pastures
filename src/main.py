import pygame
from src.core.input_handler import InputHandler
from src.world.tilemap import load_tiles, generate_tile_matrix, draw_map
from src.world.layering import load_structures, draw_structures
from src.ui.popup import PopupManager
from src.entities.player import Player
from src.ui.hud import Hud

pygame.init()
screen = pygame.display.set_mode((1024, 768))
clock = pygame.time.Clock()
tiles = load_tiles()
tile_matrix = generate_tile_matrix()
structures = load_structures()
font = pygame.font.SysFont(None, 36)
popup = PopupManager(font=font)
player = Player()
hud = Hud()
inputHandler = InputHandler(player, structures, popup, hud)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    draw_map(screen, tile_matrix, tiles)
    draw_structures(screen, structures)
    popup.draw(screen)

    keys = pygame.key.get_pressed()
    inputHandler.handle_input(keys)
    player.draw(screen)
    hud.draw(screen)

    inputHandler.cooldown()
    for s in structures:
        if hasattr(s, 'growthStage'):
            if s.growthStage < 5:
                s.grow(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()