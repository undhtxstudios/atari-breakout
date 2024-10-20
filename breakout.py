import pygame
import sys
from objects.ball import Ball
from objects.brick import Brick
from objects.paddle import Paddle
from objects.constants import PADDLE_STARTING_POS, SCREEN_WIDTH, SCREEN_HEIGTH


class Game:
    # Initializing game objects
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Atari Breakout")
        pygame.key.set_repeat(1, 10)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
        self.running = True
        self.clock = pygame.time.Clock()
        self.ball = Ball(self, 100, 100, 10)
        self.brick = Brick(self, 10, 10, 10, 10, False)
        self.paddle = Paddle(
            self,
            PADDLE_STARTING_POS[0],
            PADDLE_STARTING_POS[1],
            PADDLE_STARTING_POS[2],
            PADDLE_STARTING_POS[3],
        )

    # Main function for running the game
    def run(self):
        while self.running:
            self.screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.paddle.move_left()
                        # self.paddle.draw()
                        # self.screen.fill((0,0,0))
                    if event.key == pygame.K_RIGHT:
                        self.paddle.move_right()
            self.ball.draw(self.screen)
            self.brick.draw(self.screen)
            self.paddle.draw(self.screen)
            pygame.display.update()


Game().run()
