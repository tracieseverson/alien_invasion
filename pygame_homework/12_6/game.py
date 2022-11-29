import pygame
import rocket
from bullet import Bullet


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        self.screen.fill((230, 230, 230))
        self.rocket = rocket.Rocket(self.screen)
        self.bullets = pygame.sprite.Group()

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
                    if event.key == pygame.K_SPACE:
                        self._fire_bullet()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        self.rocket.moving_down = False
                    if event.key == pygame.K_UP:
                        self.rocket.moving_up = False

            # ====== Update ======
            self.rocket.update()
            self.bullets.update()
            for bullet in self.bullets.copy():
                if bullet.rect.left > self.screen.get_rect().right:
                    self.bullets.remove(bullet)

            # ====== Draw ======
            self.screen.fill((230, 230, 230))
            self.rocket.draw()
            for bullet in self.bullets:
                bullet.draw()
            pygame.display.flip()

    def _fire_bullet(self):
        if len(self.bullets) < 3:
            new_bullet = Bullet(self.screen, self.rocket)
            self.bullets.add(new_bullet)


if __name__ == '__main__':
    game = Game()
    game.run()
