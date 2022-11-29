import pygame


class Drop(pygame.sprite.Sprite):
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
        #print(self.rect.top)
        #print(self.screen.get_rect().bottom)
        if self.rect.top > self.screen.get_rect().bottom: #remember y gets bigger in the down direction
            self.rect.bottom = 0
