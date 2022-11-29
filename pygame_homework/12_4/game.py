import pygame
import rocket


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((200, 200))
        self.screen.fill((230, 230, 230))
        self.rocket = rocket.Rocket(self.screen)

    def run(self):
        # ====== Main Loop ======
        while True:
            # ====== Event Handling ======
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.rocket.moving_down = True
                    if event.key == pygame.K_UP:
                        self.rocket.moving_up = True
                    if event.key == pygame.K_LEFT:
                        self.rocket.moving_left = True
                    if event.key == pygame.K_RIGHT:
                        self.rocket.moving_right = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        self.rocket.moving_down = False
                    if event.key == pygame.K_UP:
                        self.rocket.moving_up = False
                    if event.key == pygame.K_LEFT:
                        self.rocket.moving_left = False
                    if event.key == pygame.K_RIGHT:
                        self.rocket.moving_right = False
            # ====== Update ======
            self.rocket.update()

            # ====== Draw ======
            self.screen.fill((230, 230, 230))
            self.rocket.draw()
            pygame.display.flip()


if __name__ == '__main__':
    game = Game()
    game.run()
