# Importing the libraries
import pygame
import time


class NewImage:
    """A class to draw a new image on the screen"""

    def __init__(self, screen):
        """Initialize the image and set its starting position"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

    def check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)

    def check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.moving_right = True
            print("moving right")
        elif event.key == pygame.K_LEFT:
            self.moving_left = True
            print("moving left")
        elif event.key == pygame.K_UP:
            self.moving_up = True
            print("moving up")
        elif event.key == pygame.K_DOWN:
            self.moving_down = True
            print("moving down")
        elif event.key == pygame.K_q:
            exit()

    def check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.moving_left = False
        elif event.key == pygame.K_UP:
            self.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.moving_down = False



    def draw(self):
        screen.fill(color)
        pygame.display.flip()


# Initializing Pygame
pygame.init()

# Initializing screen
screen = pygame.display.set_mode((400, 300))

# Initialing RGB Color
color = (0, 0, 255)

# Changing surface color
screen.fill(color)

my_character = NewImage(screen)

ship_speed = 0.5

while True:
    my_character.check_events()
    my_character.draw()