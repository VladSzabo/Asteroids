from pygame import Rect, transform
from Constants import Constants
from math import cos, sin, radians


class Asteroid:

    dir_x, dir_y = 0, 0

    def __init__(self, draw_rect, collision_box, image, speed):
        self.draw_rect = draw_rect
        self.collision_box = collision_box
        self.image = transform.scale(image, (int(draw_rect[2]), int(draw_rect[3])))
        self.speed = speed

        player_pos = Constants.get_player_pos()
        angle = Constants.get_angle(draw_rect[0], draw_rect[1], player_pos[0], player_pos[1])
        self.dir_x, self.dir_y = cos(radians(angle)), sin(radians(angle))
        print(angle)
        print(str(self.dir_x) + "|" + str(self.dir_y))
        print("-------------")

    def render(self, game_display):
        game_display.blit(self.image, self.draw_rect)

    def update(self):
        self.draw_rect[0] += self.dir_x
        self.draw_rect[1] += self.dir_y

