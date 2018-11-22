'''Zambies: Zombie class
Created Fall 2018
@author: Duncan Van Keulen (djv78)
'''

import pygame
import random


class Zombie(pygame.sprite.Sprite):
    def __init__(self, speed=0.7, init_health=100, zomb_x=0, zomb_y=0):
        ''' Constructor for Zombie sprite class'''
        super().__init__()
        self.health = init_health
        self.speed = speed
        self.image = pygame.image.load('zombie.png')
        self.zombie_x = zomb_x
        self.zombie_y = zomb_y
        self.player_x = 0
        self.player_y = 0

        self.rect = self.image.get_rect()

    def update_player_coords(self, x, y):
        ''' Update the current position of the player'''
        self.player_x = x
        self.player_y = y

    def move(self):
        ''' Zombie AI roaming functionality'''
        if self.zombie_x > self.player_x:
            self.rect.x -= self.speed
        if self.zombie_x < self.player_x:
            self.rect.x += self.speed

        if self.zombie_y > self.player_y:
            self.rect.y -= self.speed
        if self.zombie_y < self.player_y:
            self.rect.y += self.speed






# class Zombie:
#     ''' Class for making zombie objects'''
#
#     def __init__(self, display):
#         '''Constructor for Zombie class'''
#         # Dimensions of image are 37x37
#         super().__init__()
#         self._zombie_image = pygame.image.load('zombie.png')
#         self._display = display
#         self._health = 100
#         self._zombie_x = random.randint(30, 770)
#         self._zombie_y = random.randint(30, 570)
#         self._player_x = 0
#         self._player_y = 0
#         self._speed = 0
#         self._x_distance = 0
#         self._y_distance = 0
#         self.update_position()
#
#     def update_position(self):
#         '''Update the position of the zombie object'''
#         self._display.blit(self._zombie_image, (self._zombie_x,self._zombie_y))
#
#     def set_position(self, coords):
#         '''Set the position of the zombie object'''
#         self._zombie_x = coords[0]
#         self._zombie_y = coords[1]
#         self.update_position()
#
#     def set_health(self, health):
#         '''Set the health of the zombie'''
#         self._health = health
#
#     def get_health(self):
#         '''Return the health of the zombie'''
#         return self._health
#
#     def wound(self, multiplier=1):
#         '''Take 1 point away from health times the optional multiplier'''
#         self._health -= (1 * multiplier)
#
#     def player_location(self, x, y):
#         '''Receive and update the position of the player'''
#         self._player_x = x
#         self._player_y = y
#
#     def set_speed(self, speed):
#         '''Set the speed of the zombie'''
#         self._speed = speed
#
#     def get_speed(self):
#         '''Return the speed of the zombie'''
#         return self._speed
#
#     def roam(self):
#         '''Zombie AI roaming functionality'''
#         if self._zombie_x > self._player_x:
#             self._zombie_x -= self._speed
#         if self._zombie_x < self._player_x:
#             self._zombie_x += self._speed
#
#         if self._zombie_y > self._player_y:
#             self._zombie_y -= self._speed
#         if self._zombie_y < self._player_y:
#             self._zombie_y += self._speed
#
#         self.set_position((self._zombie_x, self._zombie_y))
#         self.update_position()
