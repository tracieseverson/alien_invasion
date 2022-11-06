import pygame
import sys
import time


class Picture():
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen.get_rect().center
        #self.rect.center = self.screen_rect().center
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        #self.ship_speed = 1.5
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        screen.fill((0, 0, 255))
        self.screen.blit(self.image, self.rect)
        pygame.display.flip()

    def run_game(self):
        while True:
            ship.check_events()
            ship.updates()
            ship.draw()

    def updates(self):
        #self.x += self.ship_speed
        #self.x -= self.ship_speed
        #self.rect.x = self.x
        if self.moving_right:
            self.x += ship_speed
            #self.rect.x += 1
        if self.moving_left:
            self.x -= ship_speed
            #self.rect.x -= 1
        if self.moving_up:
            self.y -= ship_speed
            #self.rect.x += 1
        if self.moving_down:
            self.y += ship_speed
            #self.rect.x -= 1
        #self.x += self.ship_speed
        #self.x -= self.ship_speed
        self.rect.x = self.x
        self.rect.y = self.y

    def check_events(self):
        #while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.moving_left = True
                elif event.key == pygame.K_UP:
                    #self.moving_right = True
                     self.moving_up = True
                elif event.key == pygame.K_DOWN:
                     self.moving_down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.moving_left = False
                elif event.key == pygame.K_UP:
                    #self.moving_right = False
                    self.moving_up = False
                elif event.key == pygame.K_DOWN:
                    #self.moving_right = False
                    self.moving_down = False


pygame.init()

screen = pygame.display.set_mode((600, 400))
screen.fill((0, 0, 255))
ship = Picture(screen)
ship_speed = 0.5
ship.run_game()
