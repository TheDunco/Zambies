'''Zambies: Top down zombie survival

Initialization code adopted from @author: sentdex
https://www.youtube.com/channel/UCfzlCWGWYyIQ0aLC5w48gBQ

@author: Duncan Van Keulen (djv78)
'''


import pygame
from player import Player
from zombie import Zombie

# Initialize pygame
pygame.init()

# Define a constant for frames per second
FPS = 60

# Define variables for display resolution
display_width = 800
display_height = 600

# Define color constants
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# Set up game display and clock
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Zambies')
clock = pygame.time.Clock()

# Set the background image
background_image = pygame.image.load('background2.png')


def game_loop():
    dead = False

    player_x = display_width * 0.5
    player_y = display_height * 0.5

    player_x_change = 0
    player_y_change = 0

    player = Player(gameDisplay)
    zombie1 = Zombie(gameDisplay)
    zombie2 = Zombie(gameDisplay)

    # Initialize loop variable to help with timing
    loops = 0

    player.set_speed(2.5)

    zombie1.set_speed(.7)
    zombie2.set_speed(.7)

    # Main loop
    while not dead:

        # Pygame event handling
        for event in pygame.event.get():
            last_key = event.type
            if event.type == pygame.QUIT:
                dead = True

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
        # FIXME: player_change* = 0

        player_x += player_x_change
        player_y += player_y_change

        player.set_position((player_x, player_y))

        # Set background color
        # gameDisplay.fill(WHITE)
        gameDisplay.blit(background_image,(0,0))

        # Set the start position and update the player position
        player.set_position((player_x, player_y))

        # FIXME: Put player/zombie collision logic here

        if loops > (FPS * 5):
            zombie1.update_position()
            zombie1.player_location(player_x, player_y)
            zombie1.roam()
        if loops > (FPS * 10):
            zombie2.update_position()
            zombie2.player_location(player_x, player_y)
            zombie2.roam()

        # Update the display
        pygame.display.update()
        # Set the clock speed (FPS)
        clock.tick(FPS)
        loops += 1


game_loop()
pygame.quit()
quit()
