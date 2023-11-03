import pygame
import random
import time
import os


#Create the screen
window_width = 1200
window_height = 600

screen = pygame.display.set_mode((window_width,window_height))

#Title And Icon
pygame.init()
pygame.display.set_caption("Snake")
fps = pygame.time.Clock()


background=pygame.image.load('background.jpg')

#Snake Properties
snake_color = (0,0,255)
snake_position = [100,50]
snake_body = [[100, 50],[90, 50],[80, 50],[70,50]]

# snake=pygame.image.load('snake.png')
# snake_body = [snake,snake,snake]

direction = 'RIGHT'
changeTo = direction
snake_speed = 20


#Food Properties
food_position = [random.randrange(1, (window_width//10)) * 10,random.randrange(1, (window_height//10)) * 10]
# food_color = (255,0,0)
food_color=pygame.image.load('food.png')

food_spawn = True

score = 0


def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_text = score_font.render('Score : ' + str(score), True, color)
    score_position = (window_width-200, 10)
    
    screen.blit(score_text, score_position)


def game_over():
    myfont = pygame.font.SysFont('times new roman bold', 50)
    game_over_text = myfont.render('Your Score is : ' + str(score), True, (0,0,0))
    game_over_position_text = game_over_text.get_rect()
    game_over_position_text.midtop = (window_width/2, window_height/4)
    screen.blit(game_over_text, game_over_position_text)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    os.system("options.py")
    


running = True
while running:
	screen.blit(background,(0,0))
	# screen.fill((0,255,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN :
			if event.key == pygame.K_RIGHT:
				changeTo = 'RIGHT'
				
			if event.key==pygame.K_LEFT:
				changeTo = 'LEFT'
				
			if event.key==pygame.K_UP:
				changeTo = 'UP'
				
			if event.key==pygame.K_DOWN:
				changeTo = 'DOWN'




	if changeTo == 'UP' and direction != 'DOWN':
		direction = 'UP'
	if changeTo == 'DOWN' and direction != 'UP':
		direction = 'DOWN'
	if changeTo == 'LEFT' and direction != 'RIGHT':
		direction = 'LEFT'
	if changeTo == 'RIGHT' and direction != 'LEFT':
		direction = 'RIGHT'			

	if direction == 'UP':
		snake_position[1] -= 10
	if direction == 'DOWN':
		snake_position[1] += 10
	if direction == 'LEFT':
		snake_position[0] -= 10
	if direction == 'RIGHT':
		snake_position[0] += 10

	snake_body.insert(0, list(snake_position))
	
	#Checking if the snake position and food position is same.
	if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
		score += 5
		food_spawn = False
	else:
		snake_body.pop()

	#if the food is eaten by the snake then new position of the snake	
	if not food_spawn:
		food_position = [random.randrange(1, (window_width//10)) * 10,random.randrange(1, (window_height//10)) * 10]
	food_spawn = True

	# screen.fill((0,255,0))

	#Display of snake body and food.
	for i in snake_body:
		pygame.draw.rect(screen, snake_color,pygame.Rect(i[0], i[1], 10, 10))

	# screen.blit(snake,pygame.Rect(snake_position[0],snake_position[1],10,10))
	# for i in snake_body:
	# 	screen.blit(snake,pygame.Rect(snake_position[0],snake_position[1],10,10))
	

	

	# pygame.draw.rect(screen,food_color, pygame.Rect(food_position[0], food_position[1], 10, 10))
	screen.blit(food_color,pygame.Rect(food_position[0],food_position[1],10,10))

	#game over:conditions if the snake touches the wall, then the game is over.
	# if snake_position[0] < 0 or snake_position[0] > window_width-10:
	# 	game_over()
	# if snake_position[1] < 0 or snake_position[1] > window_height-10:
	# 	game_over()

	#to go through walls and come out
	if snake_position[0] < 0 :
		snake_position[0] = window_width
	if snake_position[0] > window_width:
		snake_position[0] = 0-10 
	if snake_position[1] < 0 :
		snake_position[1] = window_height
	if snake_position[1] > window_height:
		snake_position[1] = 0-10

	# if snake_position[1] < 0 or snake_position[1] > window_height-10:
	# 	game_over()
	

	#For checking if the snake collides with itself, that is his own body and if so then game over.
	for block in snake_body[1:]:
		if snake_position[0] == block[0] and snake_position[1] == block[1]:
			game_over()

	
	show_score(1, (0,0,0),'arial bold',50)

	pygame.display.update()
	fps.tick(snake_speed)