import pygame
from objects.constants import SCREEN_WIDTH, PADDLE_COLOR


class Paddle:
    def __init__(self, game, top, left, width, height) -> None:
        self.game = game
        self.width = width
        self.height = height
        self.top = top
        self.left = left
        self.right = self.left + self.width
        self.speed = 3

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            PADDLE_COLOR,
            pygame.Rect(self.left, self.top, self.width, self.height),
            2,
            3,
        )

    def move_left(self):
        if self.left > 0:
            self.left = self.left - self.speed

    def move_right(self):
        if self.left < SCREEN_WIDTH - self.width:
            self.left = self.left + self.speed
