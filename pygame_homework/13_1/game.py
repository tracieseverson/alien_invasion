import pygame
import sys

WIDTH = 400
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((0, 0, 0,))

star = pygame.image.load('star.png')
star_rect = star.get_rect()

star_width = star.get_width()
available_space_x = WIDTH - (2 * star_width)

number_stars_x = available_space_x // (2 * star_width)

star_height = star.get_height()
available_space_y = HEIGHT - (2 * star_height)
number_stars_y = available_space_y // (2 * star_height)

for i in range(number_stars_x):
    for j in range(number_stars_y):
        screen.blit(star, (star_width + 2 * star_width * i,
                           star_height + 2 * star_height * j))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
