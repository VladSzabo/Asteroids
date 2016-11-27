import pygame
from Constants import Constants
from Entities import Entities


class Game:
    clock = pygame.time.Clock()
    game_exit = False

    def __init__(self, title, width, height, background_color):
        self.title = title
        self.width = width
        self.height = height
        self.background_color = background_color

        Entities()

        self.game_display = pygame.display.set_mode((width, height), pygame.SRCALPHA)
        pygame.display.set_caption(title)
        self.main_loop()

    def main_loop(self):
        while not self.game_exit:

            for event in pygame.event.get():
                self.handle_keys(event)

            self.game_display.fill(self.background_color)
            self.render(self.game_display)
            pygame.display.update()
            self.update()
            self.clock.tick(60)

    @staticmethod
    def render(game_display):
        Entities.render(game_display)

    @staticmethod
    def update():
        Entities.update()

    def handle_keys(self, event):
        if event.type == pygame.QUIT:
            self.game_exit = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                Constants.A = True
            if event.key == pygame.K_w:
                Constants.W = True
            if event.key == pygame.K_s:
                Constants.S = True
            if event.key == pygame.K_d:
                Constants.D = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                Constants.A = False
            if event.key == pygame.K_w:
                Constants.W = False
            if event.key == pygame.K_s:
                Constants.S = False
            if event.key == pygame.K_d:
                Constants.D = False



if __name__ == "__main__":
    pygame.init()
    Game(Constants.TITLE, Constants.WIDTH, Constants.HEIGHT, (0, 0, 0))
