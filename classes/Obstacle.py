"""Immovable blocking entity module."""

import pygame
from classes.GameObject import GameObject


class Obstacle(GameObject):
    """Base class for static obstacles that cannot be traversed or pushed."""

    def __init__(self, image: pygame.Surface, x: int, y: int, width: int, height: int):
        super().__init__(image, x, y, width, height)