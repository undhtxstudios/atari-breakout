import pygame
from objects.constants import BRICK_WIDTH, BRICK_HEIGHT, BRICK_SPACE


class Brick:
    def __init__(self, top, left, width, height, is_broken) -> None:
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


class Bricks:
    def __init__(self, count_x=4, count_y=4) -> None:
        self.bricks = []
        top = 0

        for i in range(0, count_y):
            for j in range(0, count_x):
                left = (BRICK_WIDTH * j) + (BRICK_SPACE * j)
                self.bricks.append(
                    Brick(top + 5, left + 5, BRICK_WIDTH, BRICK_HEIGHT, False)
                )
            top = (BRICK_HEIGHT * i) + (BRICK_SPACE * i)

    def draw(self, screen):
        for brick in self.bricks:
            brick.draw(screen=screen)
