'''Zambies: Top down zombie survival

Initialization code adopted from @author: sentdex
https://www.youtube.com/channel/UCfzlCWGWYyIQ0aLC5w48gBQ
Created Fall 2018
@author: Duncan Van Keulen (djv78)
'''


import pygame
import random
from levels import levels
from player import Player
from zombie import Zombie

# Initialize pygame
pygame.init()

# Define a constant for frames per second
FPS = 60

# Define variables for display resolution
display_width = 800
display_height = 600

# Set up game display and clock
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Zambies')
clock = pygame.time.Clock()

# Set the background image
background_image = pygame.image.load('background2.png')

zombie_init = Zombie(gameDisplay)
zombie_init.set_speed(0.5)
zombie_list = [zombie_init]


def add_zombies(instances, speed=0.7, speed_level=1):
    ''' Adds specified number of zombies to zombie_list'''

    instances += 1
    if speed_level == 1:
        speed *= random.randint(9, 12)/10
    if speed_level == 2:
        speed *= random.randint(10, 14)/10
    if speed_level == 3:
        speed *= random.randint(11, 16)/10
    if speed_level == 4:
        speed *= random.randint(14, 20)/10
    if speed_level == 5:
        speed *= random.randint(16, 26)/10

    for number in range(instances):
        name = 'zombie{num} = Zombie(gameDisplay)\nzombie{num}.set_speed({speed})\nzombie_list.append(zombie{num})'\
            .format(num=number, speed=speed)
        exec(name)


def game_loop():
    ''' The main loop for running the game'''
    dead = False

    # Set the player's initial position
    player_x = display_width * 0.5
    player_y = display_height * 0.5

    # Initialize variables for how much the player moves
    player_x_change = 0
    player_y_change = 0

    # Initialize the player object
    player = Player(gameDisplay)

    # Initialize loop variable to help with timing
    loops = 0

    # Initialize the player's speed
    player.set_speed(2.5)

    zombie_speed = 0.7

    level = 1

    # Main loop
    while not dead:

        # Pygame event handling
        for event in pygame.event.get():
            last_key = event.type
            if event.type == pygame.QUIT:
                dead = True

        # FIXME: Change this to have player follow the mouse
        # If keydown event, check if it was WASD and respond by moving
        if event.type == pygame.KEYDOWN:
            last_key = event.key
        if last_key == pygame.K_a:
            player_x_change = -player.get_speed()
        if last_key == pygame.K_d:
            player_x_change = player.get_speed()
        if last_key == pygame.K_w:
            player_y_change = -player.get_speed()
        if last_key == pygame.K_s:
            player_y_change = player.get_speed()

        # If WASD was released, stop moving
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_w or event.key == pygame.K_s:
                player_x_change = 0
                player_y_change = 0

        # FIXME: Put collide logic here for player/zombie, walls... later as well
        # FIXME: player_change = 0

        player_x += player_x_change
        player_y += player_y_change

        player.set_position((player_x, player_y))

        # Set background color
        # gameDisplay.fill(WHITE)
        gameDisplay.blit(background_image,(0,0))

        # Set the start position and update the player position
        player.set_position((player_x, player_y))

        # Player death logic
        if player.get_health() < 0:
            dead = True

        # FIXME: Put player/zombie collision logic here

        # Level switching logic
        if level == 1:
            exec(levels[0])
            if loops > 40*FPS:
                loops = 0
                level += 1
        elif level == 2:
            exec(levels[1])
            if loops > 40*FPS:
                loops = 0
                level += 1
        elif level == 3:
            if loops > 40*FPS:
                loops = 0
            exec(levels[2])
        elif level == 4:
            if loops > 40* FPS:
                loops = 0
            exec(levels[3])

        for zombie in zombie_list:
            zombie.update_position()
            zombie.player_location(player_x, player_y)
            zombie.roam()

        # Update the display
        pygame.display.update()
        # Set the clock speed (FPS)
        clock.tick(FPS)
        loops += 1


game_loop()
pygame.quit()
quit()
