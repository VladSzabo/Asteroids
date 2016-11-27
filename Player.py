from pygame import Rect, transform
from Constants import Constants


class Player:

    acceleration = 1
    dir_x, dir_y = 0, 0
    bullets = []

    def __init__(self, draw_rect, collision_box, image, speed, template_bullet):
        self.draw_rect = draw_rect
        self.collision_box = collision_box
        self.image = transform.scale(image, (int(draw_rect[2]), int(draw_rect[3])))
        self.speed = speed
        self.template_bullet = template_bullet

    def render(self, game_display):
        game_display.blit(self.image, self.draw_rect)

    def update(self):

        before = False

        if Constants.A:
            self.dir_x, self.dir_y = -1, 0
            before = True
            self.acceleration = 1
        if Constants.W:
            self.dir_y = -1

            if not before:
                self.dir_x = 0
                before = True

            self.acceleration = 1
        if Constants.D:
            self.dir_x = 1

            if not before:
                self.dir_y = 0
                before = True

            self.acceleration = 1
        if Constants.S:
            self.dir_y = 1

            if not before:
                self.dir_x = 0

            self.acceleration = 1

        self.move()

    def move(self):
        self.draw_rect[0] += self.dir_x * self.speed * self.acceleration
        self.draw_rect[1] += self.dir_y * self.speed * self.acceleration

        self.acceleration -= 0.03
        if self.acceleration <= 0:
            self.acceleration = 1
            self.dir_x, self.dir_y = 0, 0

        if self.draw_rect[0] > Constants.WIDTH:
            self.draw_rect[0] = 0
        elif self.draw_rect[0] + self.draw_rect[2] < 0:
            self.draw_rect[0] = Constants.WIDTH - self.draw_rect[2] / 2

        if self.draw_rect[1] > Constants.HEIGHT:
            self.draw_rect[1] = 0
        elif self.draw_rect[1] + self.draw_rect[3] < 0:
            self.draw_rect[1] = Constants.HEIGHT - self.draw_rect[3] / 2

