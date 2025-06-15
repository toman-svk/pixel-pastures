import pygame
import os

TILE_SIZE = 32

class Player:
    def __init__(self, selected_character="cowgirl"):
        character_file = "cowgirl_transparent.png" if selected_character == "cowgirl" else "cowboy_transparent.png"
        sheet_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
            "assets", "characters", character_file
        )
        self.sheet = pygame.image.load(sheet_path).convert_alpha()

        self.animations = self.load_frames()
        self.direction = 'down'  # default
        self.frame_index = 0
        self.image = self.animations[self.direction][self.frame_index]
        self.rect = self.image.get_rect(topleft=(5 * TILE_SIZE, 5 * TILE_SIZE))

        self.speed = 2
        self.frame_timer = 0

    def load_frames(self):
        # Mapping of directions to sprite positions (row, col)
        frame_map = {
            'down': [(0, 0), (0, 1)],
            'left': [(0, 2), (1, 2)],
            'right': [(1, 0), (1, 1)],
            'up': [(2, 0), (2, 1)]
        }

        frames = {}
        for direction, positions in frame_map.items():
            frames[direction] = []
            for row, col in positions:
                frame = self.sheet.subsurface(pygame.Rect(col * 64, row * 64, 64, 64))
                frames[direction].append(pygame.transform.scale(frame, (TILE_SIZE, TILE_SIZE)))
        return frames
    
    def move(self, directions):
        dx, dy = 0, 0
        for direction in directions:
            if direction == 'up':
                dy = -self.speed
                self.direction = 'up'
            if direction == 'down':
                dy = self.speed
                self.direction = 'down'
            if direction == 'left':
                dx = -self.speed
                self.direction = 'left'
            if direction == 'right':
                dx = self.speed
                self.direction = 'right'

        self.rect.x += dx
        self.rect.y += dy

        # Animate only when moving
        if dx != 0 or dy != 0:
            self.frame_timer += 1
            if self.frame_timer % 10 == 0:
                self.frame_index = (self.frame_index + 1) % len(self.animations[self.direction])
        else:
            self.frame_index = 0  # idle

    def draw(self, screen):
        self.image = self.animations[self.direction][self.frame_index]
        screen.blit(self.image, self.rect.topleft)