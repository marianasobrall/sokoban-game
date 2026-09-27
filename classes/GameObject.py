"""Base game object module for all entities in the Sokoban grid."""

import pygame


class GameObject(pygame.sprite.Sprite):
    """Represents a renderable sprite entity inside the 10x10 game grid."""

    def __init__(self, image: pygame.Surface, x: int, y: int, width: int, height: int):
        super().__init__()
        self._image = image
        self.rect = self._image.get_rect()
        self.set_new_position(x, y)

    def get_surface(self) -> pygame.Surface:
        """Returns the image surface."""
        return self._image

    def get_image(self) -> pygame.Surface:
        """Returns the sprite surface."""
        return self._image

    def set_image(self, image: pygame.Surface) -> None:
        """Updates the sprite surface."""
        self._image = image

    def get_rectangle(self) -> pygame.Rect:
        """Returns the bounding rectangle used for positioning and collisions."""
        return self.rect

    def set_new_position(self, x: int, y: int) -> None:
        """Sets the top-left coordinate of the entity."""
        self.rect.topleft = (x, y)

    def update(self) -> None:
        """Hook for per-frame entity logic updates."""
        pass