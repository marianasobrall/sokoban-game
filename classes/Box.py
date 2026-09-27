"""Pushable box entity module."""

import pygame
from classes.MovableObject import MovableObject


class Box(MovableObject):
    """Represents a pushable puzzle box."""

    def __init__(self, image: pygame.Surface, x: int, y: int, width: int, height: int):
        super().__init__(image, x, y, width, height)