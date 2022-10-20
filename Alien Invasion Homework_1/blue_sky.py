# Importing the libraries
import pygame
import time

# Initializing Pygame
pygame.init()

# Initializing surface
surface = pygame.display.set_mode((400, 300))

# Initialing RGB Color
color = (66, 87, 245)

# Changing surface color
surface.fill(color)
pygame.display.flip()

time.sleep(4)
