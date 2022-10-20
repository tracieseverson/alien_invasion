# Importing the libraries
import pygame
import time

class NewImage:
    """A class to draw a new image on the screen"""

    def __init__(self, screen):
        """Initialize the image and set its starting position"""
        self.screen = screen
        self.image = pygame.image.load('dog.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen.get_rect().center

    def draw(self):
        self.screen.blit(self.image, self.rect)


# Initializing Pygame
pygame.init()

# Initializing screen
screen = pygame.display.set_mode((400, 300))

# Initialing RGB Color
color = (0, 0, 255)

# Changing surface color
screen.fill(color)

my_character = NewImage(screen)
my_character.draw()

pygame.display.flip()

time.sleep(10)