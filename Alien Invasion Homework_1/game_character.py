import pygame

class NewImage:
    """A class to draw a new image on the screen"""

    def __init__(self):
        """Initialize the image and set its starting position"""
        #self.screen = ai_game.screen
        #self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('close-portrait-gorgeous-maremma-sheepdog-260nw-1015627555.bmp')
        self.rect = self.image.get_rect()

        #self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)
