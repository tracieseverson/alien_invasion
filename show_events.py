import pygame
import time

pygame.init()

screen = pygame.display.set_mode((500, 500))

while True:
    new_event = pygame.event.get()
    print(new_event)
    time.sleep(1)