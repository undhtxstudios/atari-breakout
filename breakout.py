import pygame
from objects.ball import Ball
from objects.brick import Brick
from objects.paddle import Paddle
from objects.constants import PADDLE_STARTING_POS


class Game:
    # Initializing game objects
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Atari Breakout")
        self.screen = pygame.display.set_mode((640, 480))
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

    def handle_events(self):
        for event in pygame.event.get():
            if event == pygame.QUIT:
                self.running = False
                pygame.quit()

    # Main function for running the game
    def run(self):
        while self.running:
            self.screen.fill((0, 0, 0))
            self.ball.draw(self.screen)
            self.brick.draw(self.screen)
            self.paddle.draw(self.screen)
            pygame.display.update()
            self.handle_events()
        return


Game().run()
