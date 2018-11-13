
import pygame
import math


class Player:

    def __init__(self, display):
        self._player_image = pygame.image.load('Player1.png')
        self._display = display
        self._player_x = 0
        self._player_y = 0
        self.update_position()

    def update_position(self):
        self._display.blit(self._player_image, (self._player_x,self._player_y))

    def set_position(self, coords):
        self._player_x = coords[0]
        self._player_y = coords[1]
        self.update_position()