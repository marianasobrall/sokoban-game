"""Target slot tile module where boxes must be placed."""

import pygame
from classes.StepableObject import StepableObject


class BoxSpot(StepableObject):
    """Represents a designated destination spot for a box."""

    def __init__(self, image: pygame.Surface, x: int, y: int, width: int, height: int):
        super().__init__(image, x, y, width, height)
        self._contains_box = False

    def contains_box(self) -> bool:
        """Returns True if a box is currently placed on this spot."""
        return self._contains_box

    def set_contains_box(self, state: bool) -> None:
        """Updates the occupation state while respecting encapsulation."""
        self._contains_box = state