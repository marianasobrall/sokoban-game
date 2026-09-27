"""Player entity module controlled by keyboard input."""

import pygame
from classes.MovableObject import MovableObject


class Player(MovableObject):
    """Main character tracking steps taken, level time, and sprite orientation."""

    def __init__(
        self,
        image_right: pygame.Surface,
        x: int,
        y: int,
        width: int,
        height: int,
        image_left: pygame.Surface,
    ):
        super().__init__(image_right, x, y, width, height)
        self.__score_time = 0
        self.__move_count = 0
        self._image_left = image_left
        self._image_right = image_right

    def get_score(self) -> int:
        """Returns the completion time in seconds for the level."""
        return self.__score_time

    def set_score(self, time_in_seconds: int) -> None:
        """Stores the completion time in seconds."""
        self.__score_time = time_in_seconds

    def get_moves(self) -> int:
        """Returns the total number of valid steps taken by the player."""
        return self.__move_count

    def move(self, dx: int, dy: int) -> None:
        """Updates sprite orientation, increments step count, and moves player."""
        if dx < 0:
            self.set_image(self._image_left)
        elif dx > 0:
            self.set_image(self._image_right)

        self.__move_count += 1
        self.add_move(dx, dy)
        print("Steps:", self.__move_count)