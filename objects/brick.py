import pygame


class Brick:
    def __init__(self, game, top, left, width, height, is_broken) -> None:
        self.game = game
        self.width = width
        self.height = height
        self.top = top
        self.left = left
        self.is_broken = is_broken

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            (0, 255, 0),
            pygame.Rect(self.left, self.top, self.width, self.height),
        )
