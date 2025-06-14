import pygame
import os
import json

# Dynamically determine path to project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ASSET_DIR = os.path.join(BASE_DIR, "assets", "maps/tiles/")
MAP_FILE = os.path.join(BASE_DIR, "assets", "maps", "map1.json")


TILE_SIZE = 32
MAP_WIDTH = 4
MAP_HEIGHT = 4

TILE_INDEX = {
    1: "grass",
    2: "field_dry",
    3: "field_wet",
    4: "water",
    5: "dirt"
}

TILE_IMAGES = {
    "grass": os.path.join(ASSET_DIR, "grass.png"),
    "field_dry": os.path.join(ASSET_DIR, "dry.png"),
    "field_wet": os.path.join(ASSET_DIR, "wet.png"),
    "water": os.path.join(ASSET_DIR, "water.png"),
    "dirt": os.path.join(ASSET_DIR, "dirt.png")
}



def load_tiles():
    for name, path in TILE_IMAGES.items():
        if not os.path.exists(path):
            print(f"❌ MISSING: {path}")
        else:
            print(f"✅ Loaded: {path}")
    return {
        name: pygame.transform.scale(pygame.image.load(path).convert_alpha(), (TILE_SIZE, TILE_SIZE))
        for name, path in TILE_IMAGES.items()
    }


def generate_tile_matrix():
    """
    32x24 tile map
    """
    try:
        with open(MAP_FILE, 'r') as f:
            matrix = json.load(f)
            print("✅ Loaded map1.json")
            print("Height:", len(matrix))
            print("Width:", len(matrix[0]) if matrix else 0)
            return matrix
    except Exception as e:
        print(f"❌ Failed to load map: {e}")
        return []


def draw_map(screen, tile_matrix, tiles):

    for y, row in enumerate(tile_matrix):
        for x, tile_num in enumerate(row):
            tile_name = TILE_INDEX.get(tile_num)
            screen.blit(tiles[tile_name], (x * TILE_SIZE, y * TILE_SIZE))
