import pygame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SCREEN_TITLE = "The First Snow"
GAME_VERSION = "V 0.0.1"

class ColorLibrary():
    def __init__(self) -> None:
        self.BLACK = pygame.Color(0, 0, 0)
        self.WHITE = pygame.Color(255, 255, 255)


color = ColorLibrary()

delta_time = 0
global_offset = pygame.math.Vector2()
ref_level = None