import pygame
import random
import sys

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
WIDTH = 1000
HEIGHT = 1000
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 128, 0)
WHITE = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 255)


class Player(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super(Player, self).__init__()
        self.image = pygame.image.load('ship.png').convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 180, 0.1)
        self.width = pygame.Surface.get_width(self.image)
        self.height = pygame.Surface.get_height(self.image)
        self.x = WIDTH / 2
        self.y = HEIGHT - self.height
        self.rect = self.image.get_rect()
        self.angle = 0
        self.angle_change = 1

    def update(self):
        key = pygame.key.get_pressed()
        if key[K_UP]:
            if self.y-HEIGHT/100 >= 0:
                self.y -= HEIGHT/100
        if key[K_DOWN]:
            if self.y+HEIGHT/100 <= HEIGHT-self.height:
                self.y += HEIGHT/100
        if key[K_LEFT]:
            if self.x-WIDTH/100 >= 0:
                self.x -= WIDTH/100
        if key[K_RIGHT]:
            if self.x+WIDTH/100 <= WIDTH-self.width:
                self.x += WIDTH/100

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))


class Enemy(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super(Enemy, self).__init__()
        self.counter = 0
        self.x = 0
        self.y = 0
        self.image = pygame.image.load('pirate ship.png').convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, 0.1)
        self.counter =0
        self.width = pygame.Surface.get_width(self.image)
        self.height = pygame.Surface.get_height(self.image)
        self.rect = self.image.get_rect()

    def update(self):
        if self.x+WIDTH/100 <= WIDTH-self.width:
            self.x += 5

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))


pygame.init()
infoObject = pygame.display.Info()
WIDTH = infoObject.current_w
HEIGHT = infoObject.current_h
screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
player = Player(50, 50)
enemy = Enemy(50, 50)
game_over = False
score = 0
clock = pygame.time.Clock()
myFont = pygame.font.SysFont("monospace", 35)
BG = pygame.image.load("water.png").convert_alpha()

while not game_over:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game_over = True
        elif event.type == QUIT:
            game_over = True

    screen.fill(BACKGROUND_COLOR)
    screen.blit(BG, (0, 0))
    player.draw(screen)
    enemy.draw(screen)
    pressed_keys = pygame.key.get_pressed()
    player.update()
    enemy.update()
    clock.tick(60)
    pygame.display.update()