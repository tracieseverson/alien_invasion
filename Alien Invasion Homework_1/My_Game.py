# Importing the libraries
import pygame
import time


class NewImage:
    """A class to draw a new image on the screen"""

    def __init__(self, screen):
        """Initialize the image and set its starting position"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load('rocket.png')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen.get_rect().center

        # Store a decimal value for the rocket's horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= ship_speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += ship_speed

        # Update rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y

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
        elif event.key == pygame.K_LEFT:
            self.moving_left = True
        elif event.key == pygame.K_UP:
            self.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.moving_down = True
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
        self.screen.blit(self.image, self.rect)
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
    my_character.update()
    my_character.draw()

# time.sleep(10)
