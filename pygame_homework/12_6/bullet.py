import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, screen, rocket):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 15, 3)
        # start the bullet at the tip of the rocket
        self.rect.centery = rocket.rect.centery
        self.rect.left = rocket.rect.right
        self.x = float(self.rect.x)

    def update(self):
        self.x += 1
        self.rect.x = self.x

    def draw(self):
        pygame.draw.rect(self.screen, (60, 60, 60), self.rect)
