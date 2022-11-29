import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((200, 200))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()  # quit the game
        if event.type == pygame.KEYDOWN:
            print(f"event.key = {event.key}")
