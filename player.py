'''Zambies: Player class
Created Fall 2018
@author: Duncan Van Keulen (djv78)
'''

import pygame
import math


class Player(pygame.sprite.Sprite):
    def __init__(self, speed=3, init_health=100, player_x=0, player_y=0):
        ''' Constructor for Player sprite class'''
        super().__init__()
        self.health = init_health
        self.speed = speed
        self.image = pygame.image.load('Player1rotated.png')
        self.original_image = self.image
        self.x = player_x
        self.y = player_y

        self.rect = self.image.get_rect()

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def move(self):
        ''' Adopted from code by @author: dustin bennett
        https://stackoverflow.com/users/5504244/dustin-bennett
        on page
        https://stackoverflow.com/questions/23841128/pygame-how-to-check-mouse-coordinates
        '''

        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.x, mouse_y - self.y
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        self.image = pygame.transform.rotate(self.original_image, int(angle))
        self.rect = self.image.get_rect(center=(self.x, self.y))

        x_change_factor = round((self.speed * math.sin(angle)), 2)
        y_change_factor = round((self.speed * math.cos(angle)), 2)

        self.x += x_change_factor
        self.y += y_change_factor

        # print('Angle:', angle, ' | relx:', rel_x, ' |rely', rel_y, ' | YFacor:', y_change_factor, \
        #       ' | XFactor:', x_change_factor, ' | X:',self.x, ' | Y:',self.y)


# class Player:
#     ''' Class for making the player object'''
#     def __init__(self, display):
#         ''' Constructor for Player class'''
#         # Dimensions are 28x39
#         self._player_image = pygame.image.load('Player1.png')
#         self._display = display
#         self._health = 100
#         self._player_x = 0
#         self._player_y = 0
#         self._player_speed = 0
#         self.update_position()
#
#     def update_position(self):
#         ''' Update the position of the player'''
#         self._display.blit(self._player_image, (self._player_x,self._player_y))
#
#     def set_position(self, coords):
#         ''' Set the position of the player'''
#         self._player_x = coords[0]
#         self._player_y = coords[1]
#         self.update_position()
#
#     def set_health(self, health):
#         '''Set the health of the player'''
#         self._health = health
#
#     def wound(self, multiplier=1):
#         '''Take 1 point away from health times the optional multiplier'''
#         self._health -= (1 * multiplier)
#
#     def set_speed(self, speed):
#         '''Set the speed of the player'''
#         self._player_speed = speed
#
#     def get_speed(self):
#         '''Return the speed of the player'''
#         return self._player_speed
#
#     def get_health(self):
#         '''Return the health'''
#         return self._health
