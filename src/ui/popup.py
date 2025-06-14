import pygame
import time

class PopupManager:
    def __init__(self, font, duration=500):
        self.font = font
        self.duration = duration  # in milliseconds
        self.active_message = None
        self.start_time = 0

    def show_popup(self, message):
        self.active_message = message
        self.start_time = pygame.time.get_ticks()

    def draw(self, screen):
        if self.active_message:
            current_time = pygame.time.get_ticks()
            if current_time - self.start_time < self.duration:
                text_surface = self.font.render(self.active_message, True, (255, 255, 255))
                text_rect = text_surface.get_rect(center=(screen.get_width() // 2, 30))
                background_rect = text_rect.inflate(20, 10)
                pygame.draw.rect(screen, (0, 0, 0), background_rect)
                screen.blit(text_surface, text_rect)
            else:
                self.active_message = None