import pygame

import lib
import player
import camera

class World():
    def __init__(self) -> None:
        lib.ref_level = self

        self.display_surface = pygame.display.get_surface()

        self.player = player.Player()
        self.camera = camera.Camera("assets/test_image.png")
        self.camera.add(self.player)


    def draw(self) -> None:
        self.camera.draw_camera()

    def update(self) -> None:
        self.player.update()