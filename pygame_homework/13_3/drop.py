import pygame


class Drop(pygame.sprite.Sprite): #simple class for visible game objects
#class Drop():
    def __init__(self, screen, x, y):
        super().__init__()
        self.screen = screen
        self.moving_up = False
        self.moving_down = False
        self.image = pygame.image.load('rain_drop.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y += 1
