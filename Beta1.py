import pygame
import random
import sys

pygame.init()

WIDTH = 1000
HEIGHT = 1000

RED = (255,0,0)
ORANGE = (255,165,0)
YELLOW = (255,255,0)
GREEN = (0,128,0)
BACKGROUND_COLOR = (0,0,255)

player_size = 50
player_pos = [WIDTH/2, HEIGHT-2*player_size]

enemy_size = 50
enemy_pos = [random.randint(0,WIDTH-enemy_size), 0]
enemy_list = [enemy_pos]

tower_size = 50
tower_pos = (400,300)


SPEED = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = False

score = 0

clock = pygame.time.Clock()

myFont = pygame.font.SysFont("monospace", 35)

def set_level(score, SPEED):
	if score < 20:
		SPEED = 5
	elif score < 40:
		SPEED = 8
	elif score < 60:
		SPEED = 12
	else:
		SPEED = 15
	return SPEED
	# SPEED = score/5 + 1

def draw_tower():
	pygame.draw.rect(tower_pos)


def draw_enemies(enemy_list):
	for enemy_pos in enemy_list:
		pygame.draw.rect(screen, ORANGE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

def collision_check(enemy_list, player_pos):
	for enemy_pos in enemy_list:
		if detect_collision(enemy_pos, player_pos):
			return True
	return False

def detect_collision(player_pos, enemy_pos):
	p_x = player_pos[0]
	p_y = player_pos[1]

	e_x = enemy_pos[0]
	e_y = enemy_pos[1]

	if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x+enemy_size)):
		if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y+enemy_size)):
			return True
	return False

while not game_over:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:

			x = player_pos[0]
			y = player_pos[1]

			if event.key == pygame.K_LEFT:
				x -= player_size
			elif event.key == pygame.K_RIGHT:
				x += player_size
			elif event.key == pygame.K_UP:
				y -= player_size
			elif event.key == pygame.K_DOWN:
				y += player_size
			player_pos = [x,y]

	screen.fill(BACKGROUND_COLOR)


	text = "Score:" + str(score)
	label = myFont.render(text, 1, YELLOW)
	screen.blit(label, (WIDTH-500, HEIGHT-40))

	if collision_check(enemy_list, player_pos):
		game_over = True
		break

	draw_enemies(enemy_list)

	pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

	clock.tick(30)

	pygame.display.update()