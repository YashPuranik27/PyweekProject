import sys
import pygame
from pygame.locals import *
from pygame import mixer
pygame.init()

size = width, height = 1000, 1000

white = (255, 255, 255)
black = (0,0,0)
blue = (0,0,255)
green = (0,100,0)
red = (139,0,0)
green_bright = (0,255,0)
red_bright = (255,0,0)

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

BackgroundPNG = pygame.image.load("MainBackground.png")

pygame.display.set_caption("Castaway")

clock = pygame.time.Clock()

mixer.music.load('backgroundMusicLowBitrate.wav')
mixer.music.play(-1)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        screen.blit(BackgroundPNG,(0,0))

        if 150+300 > mouse[0] > 150 and 600+150 > mouse[1] > 600:
            pygame.draw.rect(screen, green_bright,(150,600,300,150))

            if click[0] == 1 and click != None:
                intro = False
                pygame.mixer.music.stop()
                return False
        else:
            pygame.draw.rect(screen, green,(150,600,300,150))

        smallText = pygame.font.Font("freesansbold.ttf",80)
        TextSurf, TextRect = text_objects("PLAY", smallText)
        TextRect.center = ((250+(100/2)),(650+(50/2)))
        screen.blit(TextSurf, TextRect)

        if 1500+300 > mouse[0] > 1500 and 600+150 > mouse[1] > 600:
            pygame.draw.rect(screen, red_bright,(1500,600,300,150))

            if click[0] == 1 and click != None:
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(screen, red,(1500,600,300,150))

        TextSurf, TextRect = text_objects("QUIT", smallText)
        TextRect.center = ((1600+(100/2)),(650+(50/2)))
        screen.blit(TextSurf, TextRect)

        pygame.display.flip()
        pygame.display.update()
        clock.tick(15)

game_intro()