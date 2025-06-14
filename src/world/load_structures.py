# src/world/load_structures.py
import os
import pygame

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
STRUCTURE_DIR = os.path.join(BASE_DIR, "assets", "structures")
TILE_SIZE = 32

def load_barn():
    barn_path = os.path.join(STRUCTURE_DIR, "barn.png")
    if not os.path.exists(barn_path):
        print(f"❌ Barn not found at {barn_path}")
        return None
    barn_img = pygame.image.load(barn_path).convert_alpha()
    return pygame.transform.scale(barn_img, (TILE_SIZE * 5, TILE_SIZE * 5))