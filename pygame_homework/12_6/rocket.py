import pygame


class Rocket:
    def __init__(self, screen):
        self.screen = screen
        self.moving_up = False
        self.moving_down = False
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen.get_rect().midleft

    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= 1
        if self.moving_down and self.rect.bottom < self.screen.get_rect().bottom:
            self.rect.y += 1

    def draw(self):
        self.screen.blit(self.image, self.rect)
