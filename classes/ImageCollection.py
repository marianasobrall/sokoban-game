"""Asset manager for loading and scaling all game textures."""

import pygame


class ImageCollection:
    """Loads and scales textures to match the required grid cell dimensions."""

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        self.BOXSPOT = None
        self.BOX = None
        self.PLAYER_LEFT = None
        self.PLAYER_RIGHT = None
        self.LAND = None
        self.PINETREE = None

        self.load_images()
        self.transform_scale()

    def load_images(self) -> None:
        """Loads all raw image surfaces from the images directory."""
        self.BOXSPOT = pygame.image.load("images/box_spot.png")
        self.BOX = pygame.image.load("images/box.png")
        self.PLAYER_LEFT = pygame.image.load("images/fireman_left.png")
        self.PLAYER_RIGHT = pygame.image.load("images/fireman_right.png")
        self.LAND = pygame.image.load("images/land.png")
        self.PINETREE = pygame.image.load("images/pine.png")

    def transform_scale(self) -> None:
        """Scales loaded surfaces to cell width and height."""
        target_size = (self.width, self.height)
        self.BOXSPOT = pygame.transform.scale(self.BOXSPOT, target_size)
        self.BOX = pygame.transform.scale(self.BOX, target_size)
        self.PLAYER_LEFT = pygame.transform.scale(self.PLAYER_LEFT, target_size)
        self.PLAYER_RIGHT = pygame.transform.scale(self.PLAYER_RIGHT, target_size)
        self.LAND = pygame.transform.scale(self.LAND, target_size)
        self.PINETREE = pygame.transform.scale(self.PINETREE, target_size)