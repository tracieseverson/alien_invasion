import pygame
import sys
from drop import Drop

WIDTH = 400
HEIGHT = 400

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((0, 0, 0,))

drop = Drop(screen, 0, 0)

drop_width = drop.rect.width
available_space_x = WIDTH - (2 * drop_width)
number_drops_x = available_space_x // (2 * drop_width)

drop_height = drop.rect.height
available_space_y = HEIGHT - (2 * drop_height)
number_drops_y = available_space_y // (2 * drop_height)
drops = pygame.sprite.Group() #container class to hold and manage multiple Sprite objects

#lets add all the raindrop sprites to a sprite group
for i in range(number_drops_x):
    for j in range(number_drops_y):
        drops.add(Drop(screen,
                       drop_width + 2 * drop_width * i,
                       drop_height + 2 * drop_height * j))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    drops.update()

    screen.fill((0, 0, 0,))
    drops.draw(screen)
    pygame.display.flip()
    clock.tick(60)  # slow down the game to 60 frames per second
