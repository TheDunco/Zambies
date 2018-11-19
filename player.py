'''Zambies: Player class
Created Fall 2018
@author: Duncan Van Keulen (djv78)
'''

import pygame


class Player:
    ''' Class for making the player object'''
    def __init__(self, display):
        '''Constructor for Player class'''
        # Dimensions are 28x39
        self._player_image = pygame.image.load('Player1.png')
        self._display = display
        self._health = 100
        self._player_x = 0
        self._player_y = 0
        self._player_speed = 0
        self.update_position()

    def update_position(self):
        '''Update the position of the player'''
        self._display.blit(self._player_image, (self._player_x,self._player_y))

    def set_position(self, coords):
        '''Set the position of the player'''
        self._player_x = coords[0]
        self._player_y = coords[1]
        self.update_position()

    def set_health(self, health):
        self._health = health

    def set_speed(self, speed):
        '''Set the speed of the player'''
        self._player_speed = speed

    def get_speed(self):
        '''Return the speed of the player'''
        return self._player_speed
