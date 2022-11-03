import pygame

import lib

class Camera(pygame.sprite.Group):
    def __init__(self, ground_surface: str) -> None:
        super().__init__()

        self.display_surface = lib.ref_level.display_surface
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2

        self.ground_surface = pygame.image.load(ground_surface)
        self.ground_rect = self.ground_surface.get_rect(topleft = (0, 0))

    def center_camera(self) -> None:
        lib.global_offset.x = lib.ref_level.player.rect.centerx - self.half_width
        lib.global_offset.y = lib.ref_level.player.rect.centery - self.half_height

    def draw_camera(self) -> None:
        self.center_camera()

        ground_offset = self.ground_rect.topleft - lib.global_offset
        self.display_surface.blit(self.ground_surface, ground_offset)

        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - lib.global_offset
            self.display_surface.blit(sprite.image, offset_pos)