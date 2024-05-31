import pygame
import spritesheet

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Spritesheets')

sprite_sheet_image = pygame.image.load('sprites/pencilman.png').convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

BG = (50, 50, 50)
BLACK = (0, 0, 0)

animation_list = []
animation_steps = [4,4,4]
action = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 150
frame = 0
raw_sprite_x = 32
raw_sprite_y = 32
sprite_scale = 4
sprite_x = raw_sprite_x * sprite_scale
sprite_y = raw_sprite_y * sprite_scale
step_counter = 0
player_x = 0
player_y = 0
player_speed = 8

for animation in animation_steps:
	temp_img_list = []
	for _ in range(animation):
		temp_img_list.append(sprite_sheet.get_image(step_counter, raw_sprite_x, raw_sprite_y, sprite_scale, BLACK))
		step_counter += 1
	animation_list.append(temp_img_list)


run = True
while run:

	#update background
	screen.fill(BG)

	current_time = pygame.time.get_ticks()
	if current_time - last_update >= animation_cooldown:
		frame += 1
		last_update = current_time
		if frame >= len(animation_list[action]):
			frame = 0
		
		#event handler
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		keys = pygame.key.get_pressed()

		player_x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * player_speed
		if player_x > (SCREEN_WIDTH - sprite_x):
			player_x = (SCREEN_WIDTH - sprite_x)
		if player_x < 0:
			player_x = 0

		player_y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * player_speed
		if player_y > (SCREEN_HEIGHT - sprite_y):
			player_y = (SCREEN_HEIGHT - sprite_y)
		if player_y < 0:
			player_y = 0

		if keys[pygame.K_DOWN]:
			if action != 0:
				action = 0 # Walking down
				frame = 0
		if keys[pygame.K_UP]:
			if action != 1:
				action = 1 # Walking up
				frame = 0
		if keys[pygame.K_RIGHT]:
			if action != 2:
				action = 2 # Walking down
				frame = 0
		if keys[pygame.K_LEFT]:
			if action != 0:
				action = 0 # Walking up
				frame = 0
		
		

	#show frame image
	screen.blit(animation_list[action][frame], (player_x, player_y))

	

	pygame.display.update()

pygame.quit()