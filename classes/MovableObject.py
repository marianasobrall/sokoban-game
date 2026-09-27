"""Dynamic entity module capable of movement within the grid."""

import pygame
from classes.GameObject import GameObject


class MovableObject(GameObject):
    """Base class for objects that can translate across coordinates."""

    def __init__(self, image: pygame.Surface, x: int, y: int, width: int, height: int):
        super().__init__(image, x, y, width, height)

    def add_move(self, dx: int, dy: int) -> None:
        """Applies a translation offset to the object's position."""
        self.rect.x += dx
        self.rect.y += dy

    def remove_move(self, dx: int, dy: int) -> None:
        """Reverts a translation offset from the object's position."""
        self.rect.x -= dx
        self.rect.y -= dy