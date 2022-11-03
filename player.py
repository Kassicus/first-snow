import pygame

import lib

class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()

        self.pos = pygame.math.Vector2(500, 400)
        self.dir = pygame.math.Vector2()
        self.speed = 200

        self.image = pygame.Surface([32, 32])
        self.image.fill(lib.color.WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self) -> None:
        self.pos += self.dir * lib.delta_time
        self.rect.center = self.pos

        self.move()

    def move(self) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.dir.x = -self.speed
        elif keys[pygame.K_d]:
            self.dir.x = self.speed
        else:
            self.dir.x = 0

        if keys[pygame.K_w]:
            self.dir.y = -self.speed
        elif keys[pygame.K_s]:
            self.dir.y = self.speed
        else:
            self.dir.y = 0