import pygame


class Paddle:
    def __init__(self, game, top, left, width, height) -> None:
        self.game = game
        self.width = width
        self.height = height
        self.top = top
        self.left = left
        self.speed = 5

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            (255, 0, 0),
            pygame.Rect(self.left, self.top, self.width, self.height),
            2,
            3,
        )

    def move_left(self):
        if self.left > 0 and self.left < 640:
            self.left = self.left - self.speed
