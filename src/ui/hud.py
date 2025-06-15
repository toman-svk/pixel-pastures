import pygame
import os

FONT_SIZE = 42

class Hud:
    def __init__(self):
        font_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
            "assets", "fonts", "PixelifySans-Regular.ttf"
        )
        pygame.font.init()
        self.score = 0
        self.font = pygame.font.Font(font_path, FONT_SIZE)

    def draw(self, screen):
        text_surface = self.font.render(str(self.score), False, (255, 255, 255))
        screen.blit(text_surface, (10, 0))
        controls_surface1 = self.font.render("E - Harvest", False, (255, 255, 255))
        controls_surface2 = self.font.render("W, A, S, D (Arrows) - Move", False, (255, 255, 255))
        screen.blit(controls_surface1, (10, 768 - 90 - FONT_SIZE))
        screen.blit(controls_surface2, (10, 768 - 90))

    def add_score(self, amount):
        if self.score + amount < 0:
            self.score = 0
        else:
            self.score += amount
        return self.score