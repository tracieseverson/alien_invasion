# Importing the libraries
import pygame
import time

# Initializing Pygame
pygame.init()

# Initializing screen
screen = pygame.display.set_mode((400, 300))

# Initialing RGB Color
color = (0, 0, 255)

# Changing surface color
screen.fill(color)
pygame.display.flip()

time.sleep(10)
