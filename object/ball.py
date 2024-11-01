from common.constants import BALL
from common.utils import load_images

from random import choice

class Ball:
    def __init__(self, dimension, speed, image) -> None:
        self.x, self.y = dimension
        self.speed = speed
        self.image = image

    def draw(self, screen):
        # to do: make it a circle, or mask for collisions?
        screen.blit(self.image, (self.x, self.y))

    def change_speed(self, speed):
        self.speed = speed

    def update(self):
        pass

class Balls:
    def __init__(self):
        self.balls = []
        self.images = []

    def load(self, theme, resolution):
        self.images = load_images(theme, BALL, resolution)
        # to do: randomize default position
        # make sure when changing resolution, if positions are out of bounds, they get adjusted
        self.balls = [Ball((100, 100), 10, choice(self.images)), Ball((80, 80), 10, choice(self.images))]

    def add(self, x, y, speed):
        # check bounds?
        ball = Ball(x, y, speed)
        self.balls.append(ball)

    def remove(self, ball):
        if ball in self.balls:
            self.balls.remove(ball)

    def update(self):
        for ball in self.balls:
            ball.update()

    def draw(self, screen):
        for ball in self.balls:
            ball.draw(screen)

    def change_speed(self, speed):
        for ball in self.balls:
            ball.change_speed(speed)

    def reload(self, theme, resolution):
        self.images = load_images(theme, BALL, resolution)
        for ball in self.balls:
            # adjust position for resolution
            ball.image = choice(self.images)

    def reset(self):
        self.balls.clear()

