"""Module defining non-blocking grid entities that can be stepped on."""

import pygame
from classes.GameObject import GameObject


class StepableObject(GameObject):
    """Represents grid tiles that entities can walk or move over freely."""

    def __init__(self, image: pygame.Surface, x: int, y: int, width: int, height: int):
        super().__init__(image, x, y, width, height)