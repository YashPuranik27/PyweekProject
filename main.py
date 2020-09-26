import pygame
import random
import math
import menu

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_w,
    K_a,
    K_s,
    K_d,
    KEYDOWN,
    QUIT,
)

WIDTH = 50
HEIGHT = 50
BACKGROUND_COLOR = (0, 0, 255)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load('ship.png').convert_alpha()
        self.angle = 180
        self.image = pygame.transform.rotozoom(self.image, self.angle, 0.1)
        self.width = pygame.Surface.get_width(self.image)
        self.height = pygame.Surface.get_height(self.image)
        self.x = WIDTH / 2
        self.y = HEIGHT - self.height
        self.cannonballs = []
        self.rect = self.image.get_rect()
        self.angle_change = 1

    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.cannonballs.append(FriendlyProjectile(self.x,self.y,mouse_x,mouse_y))
        key = pygame.key.get_pressed()
        if key[K_w]:
            if self.y - HEIGHT / 100 >= 0:
                self.y -= HEIGHT / 100
        if key[K_s]:
            if self.y + HEIGHT / 100 <= HEIGHT - self.height:
                self.y += HEIGHT / 100
        if key[K_a]:
            if self.x - WIDTH / 100 >= 0:
                self.x -= WIDTH / 100
        if key[K_d]:
            if self.x + WIDTH / 100 <= WIDTH - self.width:
                self.x += WIDTH / 100
        for projectiles in self.cannonballs:
            projectiles.draw(screen)

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.direction = random.randint(0,3)  # true is left to right and false is up and down
        self.image = pygame.image.load('pirate ship.png').convert_alpha()
        if self.direction == 0:
            self.x = 0
            self.y = random.randint(0, HEIGHT)
            self.image = pygame.transform.rotozoom(self.image, 90, 0.1)
        elif self.direction == 1:
            self.y = 0
            self.x = random.randint(0, WIDTH)
            self.image = pygame.transform.rotozoom(self.image, 0, 0.1)
        elif self.direction == 2:
            self.x = WIDTH
            self.y = random.randint(0, HEIGHT)
            self.image = pygame.transform.rotozoom(self.image, 270, 0.1)
        elif self.direction == 3:
            self.y = HEIGHT
            self.x = random.randint(0, HEIGHT)
            self.image = pygame.transform.rotozoom(self.image, 180, 0.1)
        self.counter = random.randint(20,40)
        self.speed = random.randint(3, 11)
        self.width = pygame.Surface.get_width(self.image)
        self.height = pygame.Surface.get_height(self.image)
        self.rect = self.image.get_rect()

    def update(self):
        if(self.direction == 0):
            if self.x + WIDTH / 100 <= WIDTH - self.width/2:
                self.x += self.speed
                if self.counter == 0:
                    EnemyProjectile.draw(self.direction,screen)
                    self.counter = random.randint(20,40)
            else:
                self.x = 0
                self.y = random.randint(0, HEIGHT)
                self.counter -= 1
        elif(self.direction == 1):
            if self.y - HEIGHT / 100 <= HEIGHT - self.height/2:
                self.y += self.speed
                if self.counter == 0:
                    EnemyProjectile.draw(self.direction,screen)
                    self.counter = random.randint(20,40)
            else:
                self.x = random.randint(0, WIDTH)
                self.y = 0
                self.counter -= 1
        elif(self.direction == 2):
            if self.x + WIDTH / 100 >= 0 - self.width/2:
                self.x -= self.speed
                if self.counter == 0:
                    EnemyProjectile.draw(self.direction,screen)
                    self.counter = random.randint(20,40)
            else:
                self.x = WIDTH
                self.y = random.randint(0, HEIGHT)
                self.counter -= 1
        elif (self.direction == 3):
            if self.y - HEIGHT / 100 >= 0 - self.height/2:
                self.y -= self.speed
                if self.counter == 0:
                    EnemyProjectile.draw(self.direction,screen)
                    self.counter = random.randint(20,40)
            else:
                self.x = random.randint(0, WIDTH)
                self.y = HEIGHT
                self.counter -= 1
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

class FriendlyProjectile(pygame.sprite.Sprite):
    def __init__(self, x, y, mouse_x, mouse_y):
        super(FriendlyProjectile, self).__init__()
        self.image = pygame.image.load('ball1.png').convert_alpha()
        self.x = x
        self.y = y
        self.speed = 5
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.angle = math.atan2(self.mouse_y - self.y, self.mouse_x - self.x)
        self.x_vel = math.cos(self.angle) + self.speed
        self.y_vel = math.sin(self.angle) + self.speed
        self.counter = 0
        self.image = pygame.transform.rotozoom(self.image, self.angle, 0.05)
        self.width = pygame.Surface.get_width(self.image)
        self.height = pygame.Surface.get_height(self.image)
        self.rect = self.image.get_rect

    def collision(self, sprite):
        return self.rect.colliderect(sprite.rect)

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def update(self):
        self.x += int(self.x_vel)
        self.y += int(self.y_vel)
        if self.collision(Enemy):
            Enemy.kill()
            self.kill()
        if self.x + WIDTH / 100 >= WIDTH - self.width/2:
            self.kill()
        if self.x + WIDTH / 100 <= 0 - self.width/2:
            self.kill()
        if self.y - HEIGHT / 100 >= HEIGHT - self.height/2:
            self.kill()
        if self.y - HEIGHT / 100 >= 0 - self.height/2:
            self.kill()


class EnemyProjectile(pygame.sprite.Sprite):
    def __init__(self):
        super(EnemyProjectile, self).__init__()
        self.x = 0
        self.y = 0
        self.direction = 0
        self.speed = 5
        self.image = pygame.image.load('ball1.png').convert_alpha()
        self.width = pygame.Surface.get_width(self.image)
        self.height = pygame.Surface.get_height(self.image)
        self.rect = self.image.get_rect

    def collision(self, sprite):
        return self.rect.colliderect(sprite.rect)

    def update(self):
        if self.collision(Player):
            Player.kill()
            self.kill()
        if self.direction == 0:
            if self.x + WIDTH / 100 <= WIDTH - self.width / 2:
                self.x += self.speed
            else:
                self.kill()
        elif self.direction == 1:
            if self.y - HEIGHT / 100 <= HEIGHT - self.height / 2:
                self.y += self.speed
            else:
                self.kill()
        elif self.direction == 2:
            if self.x + WIDTH / 100 >= 0 - self.width / 2:
                self.x -= self.speed
            else:
                self.kill()
        elif self.direction == 3:
            if self.y - HEIGHT / 100 >= 0 - self.height / 2:
                self.y -= self.speed
            else:
                self.kill()

    def draw(self, direction, surface):
        self.direction = direction
        surface.blit(self.image, (self.x, self.y))


pygame.init()
infoObject = pygame.display.Info()
WIDTH = infoObject.current_w
HEIGHT = infoObject.current_h
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
player = Player()
game_over = False
game_win = False
end = False
score = 0
clock = pygame.time.Clock()
ticks = pygame.time.get_ticks()
e_proj_group = pygame.sprite.GroupSingle()
f_proj_group = pygame.sprite.GroupSingle()
enemy_group = [Enemy()]
enemy_group.append(Enemy())
game = False
main_menu = True
myFont = pygame.font.SysFont("monospace", 35)
BG = pygame.image.load("water.png").convert_alpha()

while not end:
    if main_menu:
        main_menu = exec('menu')

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                end = True
        elif event.type == QUIT:
            end = True

    seconds=(pygame.time.get_ticks()-ticks)/60  #calculate how many seconds
    if seconds > 10000:
        game_win = True
        end = True
    if(seconds < 100):
        if seconds % 3 == 0:
            enemy_group.append(Enemy())
    if(seconds > 100 and seconds < 200):
        if seconds % 2 == 0:
            enemy_group.append(Enemy())
    if (seconds > 200 and seconds < 300):
        if seconds % 1 == 0:
            enemy_group.append(Enemy())


    screen.fill(BACKGROUND_COLOR)
    screen.blit(BG, (0, 0))
    player.draw(screen)

    pressed_keys = pygame.key.get_pressed()
    for bad in enemy_group:
        bad.draw(screen)
        bad.update()
    player.update()
    clock.tick(60)
    pygame.display.update()
