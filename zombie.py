
import pygame
import random


class Zombie:

    def __init__(self, display):
        '''Constructor for Zombie class'''
        # Dimensions of image are 37x37
        self._zombie_image = pygame.image.load('zombie.png')
        self._display = display
        self._health = 100
        self._zombie_x = random.randint(30, 770)
        self._zombie_y = random.randint(30, 570)
        self._player_x = 0
        self._player_y = 0
        self._speed = 0
        self._x_distance = 0
        self._y_distance = 0
        self.update_position()

    def update_position(self):
        '''Update the position of the zombie object'''
        self._display.blit(self._zombie_image, (self._zombie_x,self._zombie_y))

    def set_position(self, coords):
        '''Set the position of the zombie object'''
        self._zombie_x = coords[0]
        self._zombie_y = coords[1]
        self.update_position()

    def set_health(self, health):
        self._health = health

    def player_location(self, x, y):
        '''Receive and update the position of the player'''
        self._player_x = x
        self._player_y = y

    def set_speed(self, speed):
        '''Set the speed of the zombie'''
        self._speed = speed

    def get_speed(self):
        '''Return the speed of the zombie'''
        return self._speed

    def roam(self):
        '''Zombie AI roaming functionality'''
        if self._zombie_x > self._player_x:
            self._zombie_x -= self._speed
        if self._zombie_x < self._player_x:
            self._zombie_x += self._speed

        if self._zombie_y > self._player_y:
            self._zombie_y -= self._speed
        if self._zombie_y < self._player_y:
            self._zombie_y += self._speed

        self.set_position((self._zombie_x, self._zombie_y))
        self.update_position()
