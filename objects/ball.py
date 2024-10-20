import pygame


class Ball:
    def __init__(self, game, x_pos, y_pos, speed) -> None:
        self.game = game
        self.x = x_pos
        self.y = y_pos
        self.speed = speed

        # self.game.draw.circle(game, (0, 0, 255), (self.x, self.y), 10)

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 255), (self.x, self.y), 10)
