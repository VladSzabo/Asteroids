from pygame import image, transform
from math import atan2, degrees, pi

class Constants:

    WIDTH = 1000
    HEIGHT = 700
    TITLE = "Asteroids"

    player_size = WIDTH / 10
    asteroid_size = WIDTH / 7
    bullet_size = WIDTH / 20

    A, W, S, D = False, False, False, False

    images = {
        "player": image.load("res/player.png"),
        "asteroid": image.load("res/asteroid.png"),
        "bullet": image.load("res/bullet.png")
    }

    @staticmethod
    def get_player_pos():
        from Entities import Entities
        player_pos = [Entities.player.draw_rect[0], Entities.player.draw_rect[1]]
        del Entities

        return player_pos

    @staticmethod
    def get_angle(x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        rads = atan2(-dy, dx)
        rads %= 2 * pi
        return degrees(rads)
