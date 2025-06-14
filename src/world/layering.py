# src/world/layering.py
import os
import pygame

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
STRUCTURE_DIR = os.path.join(BASE_DIR, "assets", "structures")
TILE_SIZE = 32

def load_crop_from_sheet(filename, tile_index, tile_size=(64, 64), columns=3):
    """
    Load a specific crop from a sprite sheet based on its index.
    Index is 0-based, left to right, top to bottom.
    """
    path = os.path.join(BASE_DIR, "assets", "crops_animals", filename)
    sheet = pygame.image.load(path).convert_alpha()

    col = tile_index % columns
    row = tile_index // columns
    rect = pygame.Rect(col * tile_size[0], row * tile_size[1], *tile_size)

    crop_image = pygame.Surface(tile_size, pygame.SRCALPHA)
    crop_image.blit(sheet, (0, 0), rect)
    return pygame.transform.scale(crop_image, (TILE_SIZE, TILE_SIZE))


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

class Crop:
    def __init__(self, name, image, position, size=(1, 1)):
        self.name = name
        self.image = image
        self.position = position  # (tile_x, tile_y)
        self.size = size          # usually (1,1)
        self.harvested = False

    def draw(self, surface):
        if not self.harvested:
            pixel_x = self.position[0] * TILE_SIZE
            pixel_y = self.position[1] * TILE_SIZE
            surface.blit(self.image, (pixel_x, pixel_y))

    def get_rect(self):
        return pygame.Rect(
            self.position[0] * TILE_SIZE,
            self.position[1] * TILE_SIZE,
            self.size[0] * TILE_SIZE,
            self.size[1] * TILE_SIZE
        )

    def on_click(self):
        print(f"🌻 You clicked on a {self.name} at {self.position}")
        self.harvested = True


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

    fence_img = load_structure_image("fence.png", (1, 1))
    fence_positions = [(4, 12), (5, 12), (6, 12), (7, 12), (8, 12), (9, 12), (10, 12), (11, 12), (12, 12), (13, 12), (14, 12), (22, 13), (23, 13)]  
    if fence_img:
        for pos in fence_positions:
            structures.append(Structure("fence", fence_img, pos, (1, 1)))

    sunflower_img = load_crop_from_sheet("farm_crops_transparent.png", tile_index=1)
    if sunflower_img:
        for y in range(3, 8):
            for x in range(2, 8):
                structures.append(Crop("sunflower", sunflower_img, (x, y), (1, 1)))

    tree_img = load_structure_image("tree.png", (3, 3))
    tree_positions = [(15, 10), (5, 6), (12, 14), (20, 8), (25, 16)]  # Add more positions here
    if tree_img:
        for pos in tree_positions:
            structures.append(Structure("tree", tree_img, pos, (3, 3)))


    return structures

def draw_structures(surface, structures):
    for structure in structures:
        structure.draw(surface)