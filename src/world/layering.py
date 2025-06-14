# src/world/layering.py
import os
import pygame

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
STRUCTURE_DIR = os.path.join(BASE_DIR, "assets", "structures")
TILE_SIZE = 32

class Structure:
    def __init__(self, name, image, position, size):
        self.name = name
        self.image = image
        self.position = position  # (tile_x, tile_y)
        self.size = size          # (tiles_wide, tiles_high)

    def draw(self, surface):
        pixel_x = self.position[0] * TILE_SIZE
        pixel_y = self.position[1] * TILE_SIZE
        surface.blit(self.image, (pixel_x, pixel_y))


def load_structure_image(filename, size_tiles):
    path = os.path.join(STRUCTURE_DIR, filename)
    if not os.path.exists(path):
        print(f"❌ Missing: {path}")
        return None
    img = pygame.image.load(path).convert_alpha()
    return pygame.transform.scale(img, (size_tiles[0] * TILE_SIZE, size_tiles[1] * TILE_SIZE))


def load_structures():
    structures = []

    barn_img = load_structure_image("barn.png", (5, 5))
    if barn_img:
        structures.append(Structure("barn", barn_img, (18, 10), (5, 5)))

    # Add more structures here in the future

    tree_img = load_structure_image("tree.png", (3, 3))
    tree_positions = [(15, 10), (5, 6), (12, 14), (20, 8), (25, 16)]  # Add more positions here
    if tree_img:
        for pos in tree_positions:
            structures.append(Structure("tree", tree_img, pos, (3, 3)))

    fence_img = load_structure_image("fence.png", (1, 1))
    fence_positions = [(4, 12), (5, 12), (6, 12), (7, 12), (8, 12), (9, 12), (10, 12), (11, 12), (12, 12), (13, 12), (14, 12), (22, 13), (23, 13)]  
    if fence_img:
        for pos in fence_positions:
            structures.append(Structure("fence", fence_img, pos, (1, 1)))

    return structures

def draw_structures(surface, structures):
    for structure in structures:
        structure.draw(surface)