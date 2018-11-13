'''Zambies: Top down zombie survival

Initialization code adopted from @author: sentdex
https://www.youtube.com/channel/UCfzlCWGWYyIQ0aLC5w48gBQ

@author: Duncan Van Keulen (djv78)
'''


import pygame
from player import Player

# Initialize pygame
pygame.init()

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
background_image = pygame.image.load('background.jpg')

player_x = display_width * 0.5
player_y = display_height * 0.5

player_x_change = 0
player_y_change = 0

player = Player(gameDisplay)

dead = False

# Main loop
while not dead:

    # Pygame event handling
    for event in pygame.event.get():
        last_key = event.type
        if event.type == pygame.QUIT:
            dead = True

    if event.type == pygame.KEYDOWN:
        last_key = event.key
    if last_key == pygame.K_a:
        player_x_change = -2
    if last_key == pygame.K_d:
        player_x_change = 2
    if last_key == pygame.K_w:
        player_y_change = -2
    if last_key == pygame.K_s:
        player_y_change = 2

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_w or event.key == pygame.K_s:
            player_x_change = 0
            player_y_change = 0

    player_x += player_x_change
    player_y += player_y_change

    player.set_position((player_x, player_y))

    # Set background color
    # gameDisplay.fill(WHITE)
    gameDisplay.blit(background_image,(0,0))

    # Set the start position and update the player position
    player.set_position((player_x, player_y))
    player.update_position()

    # Update the display
    pygame.display.update()
    # Set the clock speed (FPS)
    clock.tick(60)

pygame.quit()
quit()
