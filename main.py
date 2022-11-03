import pygame

import lib
import world

pygame.init()

class Game():
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode([lib.SCREEN_WIDTH, lib.SCREEN_HEIGHT])
        pygame.display.set_caption(str(lib.SCREEN_TITLE + lib.GAME_VERSION))

        self.running = True
        self.clock = pygame.time.Clock()
        self.events = pygame.event.get()

        self.world = world.World()

    def run(self) -> None:
        while self.running:
            self.event_loop()
            self.draw()
            self.update()

    def event_loop(self) -> None:
        self.events = pygame.event.get()

        for event in self.events:
            if event.type == pygame.QUIT:
                self.running = False

    def draw(self) -> None:
        self.screen.fill(lib.color.BLACK)

        self.world.draw()

    def update(self) -> None:
        self.world.update()

        pygame.display.update()
        lib.delta_time = self.clock.tick(120) / 1000

if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()