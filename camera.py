import pygame

import lib

class Camera(pygame.sprite.Group):
    def __init__(self) -> None:
        super().__init__()

        self.display_surface = lib.ref_level.display_surface
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2

    def center_camera(self) -> None:
        lib.global_offset.x = lib.ref_level.player.rect.centerx - self.half_width
        lib.global_offset.y = lib.ref_level.player.rect.centery - self.half_height

    def draw_camera(self) -> None:
        self.center_camera()

        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - lib.global_offset
            self.display_surface.blit(sprite.image, offset_pos)