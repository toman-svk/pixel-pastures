import pygame
from pygame import mixer

pygame.mixer.init()

def music():
    mixer.music.load("assets/music/background_country.mp3")
    mixer.music.play(-1)  # Loop the music indefinitely
    mixer.music.set_volume(0.3)  # Set volume to 30%
