import pygame
# Intialize pygame
pygame.init()

screen = pygame.display.set_mode((1000, 500))

#title and icon
pygame.display.set_caption("Tester game")

#icon should be 32 by 32 pixels
#icon = pygame.image.load("icon.ext")
#pygame.display.set_icon(icon)

#player starting values
#playerImg = pygame.image.load("player.png")
playerX= 360
playerY= 360

#How the game runs
running = True
while running:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False

    screen.fill((255, 0, 0))
    pygame.display.update()