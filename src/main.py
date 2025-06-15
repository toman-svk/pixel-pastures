import re
import pygame, sys
from src.core.input_handler import InputHandler
from src.world.tilemap import load_tiles, generate_tile_matrix, draw_map
from src.world.layering import load_structures, draw_structures
from src.ui.popup import PopupManager
from src.entities.player import Player
from src.ui.hud import Hud
from src.ui.button import Button
from src.ui.font import get_font
from src.music.background_music import music

def run_game(selected_character):
    from src.ui.menu import main_menu
    pygame.init()
    screen = pygame.display.set_mode((1024, 730))
    clock = pygame.time.Clock()
    tiles = load_tiles()
    tile_matrix = generate_tile_matrix()
    structures = load_structures()
    font = get_font(36)
    popup = PopupManager(font=font)
    player = Player(selected_character)
    hud = Hud()
    inputHandler = InputHandler(player, structures, popup, hud)

    #Menu button
    BACK_BUTTON = Button(
        image=None,
        pos=(950, 40),  
        text_input="MENU",
        font=get_font(40),
        base_color="Black",
        hovering_color="Green"
    )
    #Music button
    
    MUTE_BUTTON = Button(
        image=None,
        pos=(944, 690),  
        text_input="MUTE",
        font=get_font(30),
        base_color="Black",
        hovering_color="Green"
    )
    is_muted = False

    music()

    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(mouse_pos):
                    running = False
                    main_menu()
                    return
                if MUTE_BUTTON.checkForInput(mouse_pos):
                    is_muted = not is_muted
                    if is_muted:
                        pygame.mixer.music.set_volume(0)
                        
                        MUTE_BUTTON.set_text("MUTE")
                    else:
                        pygame.mixer.music.set_volume(0.3)
                        
                        MUTE_BUTTON.set_text("MUTE")

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
        
        
        BACK_BUTTON.changeColor(mouse_pos)
        BACK_BUTTON.update(screen)

        MUTE_BUTTON.changeColor(mouse_pos)
        MUTE_BUTTON.update(screen)

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
        


if __name__ == "__main__":
    from src.ui.menu import main_menu
    main_menu()    