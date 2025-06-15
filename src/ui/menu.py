import pygame, sys
from .button import Button
from .font import get_font
pygame.init()

SCREEN = pygame.display.set_mode((1024, 730))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/menu/Background.png")
selected_character = "cowgirl"

def play():
    global selected_character
    from src.main import run_game
    run_game(selected_character)

def options():
    global selected_character
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        #SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("Choose your character:", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(512, 200))
        SCREEN.blit(BG, (0, 0))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        # Tlačítka pro výběr postavy
        COWGIRL_BUTTON = Button(
            image=None, pos=(400, 350),
            text_input="COWGIRL", font=get_font(60),
            base_color="Black", hovering_color="Green"
        )
        COWBOY_BUTTON = Button(
            image=None, pos=(650, 350),
            text_input="COWBOY", font=get_font(60),
            base_color="Black", hovering_color="Green"
        )
        OPTIONS_BACK = Button(
            image=None, pos=(512, 500),
            text_input="BACK", font=get_font(75),
            base_color="Black", hovering_color="Green"
        )

        # Zvýraznění vybrané postavy
        if selected_character == "cowgirl":
            pygame.draw.rect(SCREEN, (200,255,200), COWGIRL_BUTTON.rect.inflate(20,20), border_radius=10)
        else:
            pygame.draw.rect(SCREEN, (200,255,200), COWBOY_BUTTON.rect.inflate(20,20), border_radius=10)

        for button in [COWGIRL_BUTTON, COWBOY_BUTTON, OPTIONS_BACK]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if COWGIRL_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    selected_character = "cowgirl"
                if COWBOY_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    selected_character = "cowboy"
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    return

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#d7fcd4")
        MENU_RECT = MENU_TEXT.get_rect(center=(512, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/menu/Play_b.png"), pos=(512,250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/menu/Character_b.png"), pos=(512,400), 
                            text_input="CHARACTER", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/menu/Quit_b.png"), pos=(512,550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

if __name__ == "__main__":
    main_menu() 