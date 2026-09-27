"""Pine tree obstacle entity module."""

import pygame
from classes.Obstacle import Obstacle


class PineTree(Obstacle):
    """Pine tree obstacle placed across the grid."""

    def __init__(self, image: pygame.Surface, x: int, y: int, width: int, height: int):
        super().__init__(image, x, y, width, height)