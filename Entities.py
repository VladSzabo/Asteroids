from Constants import Constants
from Player import Player
from Asteroid import Asteroid
from random import randint


class Entities:
    player = None
    asteroids = []
    spawn_rate = 60
    timer = 0

    def __init__(self):
        Entities.player = Player(
            [(Constants.WIDTH - Constants.player_size) / 2, (Constants.HEIGHT - Constants.player_size) / 2,
             Constants.player_size, Constants.player_size], [5, 5, 95, 95], Constants.images["player"],
            Constants.WIDTH / 120, None)

    @staticmethod
    def render(game_display):
        for a in Entities.asteroids:
            a.render(game_display)
        Entities.player.render(game_display)

    @staticmethod
    def update():
        Entities.player.update()
        for a in Entities.asteroids:
            a.update()

        Entities.timer += 1

        if Entities.timer > 1000:
            Entities.timer = 0

        if Entities.timer % int(Entities.spawn_rate) == 0:
            Entities.generate_asteroid()

    @staticmethod
    def generate_asteroid():
        x = randint(0, Constants.WIDTH)
        y = randint(0, Constants.HEIGHT)
        size = randint(Constants.WIDTH // 25, Constants.WIDTH // 12)
        speed = randint(Constants.WIDTH // 325, Constants.WIDTH // 180)

        Entities.asteroids.append(
            Asteroid([x, y, size, size], [0, 0, 100, 100], Constants.images["asteroid"], speed))

        Entities.spawn_rate -= 0.2