"""Level factory module parsing files and instantiating game objects."""

import os
from classes.Level import Level
from classes.Player import Player
from classes.PineTree import PineTree
from classes.Box import Box
from classes.BoxSpot import BoxSpot
from classes.ImageCollection import ImageCollection
from exceptions import (
    InvalidCharacterError,
    ExtraCharacterError,
    MissingElementError,
    BoxCountMismatchError,
)


class LevelFactory:
    """Parses text configuration files and creates configured Level objects."""

    def __init__(self, width: int, height: int, *level_numbers: int):
        self.__level_map = {}
        # Preload shared textures once across all levels
        self.__images = ImageCollection(width, height)
        self.load_levels(width, height, *level_numbers)

    def load_levels(self, width: int, height: int, *level_numbers: int) -> None:
        """Loads and parses level files based on variable arguments."""
        for num in level_numbers:
            filepath = os.path.join("collections", f"level{num}.txt")
            level = self.__load_level(width, height, filepath)
            self.__level_map[num] = level

    def get_level_count(self) -> int:
        """Returns the number of loaded levels."""
        return len(self.__level_map)

    def get_level(self, level_id: int) -> Level:
        """Retrieves a specific level instance by its identifier."""
        return self.__level_map[level_id]

    def __load_level(self, width: int, height: int, filepath: str) -> Level:
        level_grid = []
        num_player = 0
        num_box = 0
        num_box_spot = 0

        with open(filepath, "r", encoding="utf-8") as file:
            lines = [line.rstrip("\r\n") for line in file.readlines()[:10]]

            for line_number, line in enumerate(lines, start=1):
                elements = list(line)

                # Requisite: Invalid characters terminate execution with file and line info
                for char in elements:
                    if char not in "pobs_":
                        raise InvalidCharacterError(
                            f"Invalid character '{char}' found in file '{filepath}' at line {line_number}."
                        )

                # Requisite: Extra characters are logged and truncated
                try:
                    if len(elements) > 10:
                        raise ExtraCharacterError(
                            f"Warning: Line {line_number} in '{filepath}' has extra elements. Truncated to 10."
                        )
                except ExtraCharacterError as err:
                    print(err)
                    elements = elements[:10]

                # Requisite: Missing characters are logged and padded with '_'
                try:
                    if len(elements) < 10:
                        raise MissingElementError(
                            f"Warning: Line {line_number} in '{filepath}' is missing elements. Filled with '_'."
                        )
                except MissingElementError as err:
                    print(err)
                    elements.extend(["_"] * (10 - len(elements)))

                num_box += elements.count("b")
                num_box_spot += elements.count("s")
                num_player += elements.count("p")
                level_grid.append(elements)

        # Structural level validation
        if num_player != 1:
            raise MissingElementError(
                f"File '{filepath}' must contain exactly 1 player (found {num_player})."
            )
        if num_box == 0:
            raise MissingElementError(f"No boxes ('b') found in '{filepath}'.")
        if num_box_spot == 0:
            raise MissingElementError(f"No box spots ('s') found in '{filepath}'.")
        if num_box != num_box_spot:
            raise BoxCountMismatchError(
                f"Box count ({num_box}) does not match spot count ({num_box_spot}) in '{filepath}'."
            )

        level = Level(self.__images)

        for y, row in enumerate(level_grid):
            for x, char in enumerate(row):
                pos_x = x * width
                pos_y = y * height

                if char == "p":
                    player = Player(
                        self.__images.PLAYER_RIGHT,
                        pos_x,
                        pos_y,
                        width,
                        height,
                        self.__images.PLAYER_LEFT,
                    )
                    level.set_player(player)
                elif char == "o":
                    obstacle = PineTree(self.__images.PINETREE, pos_x, pos_y, width, height)
                    level.get_immovables().add(obstacle)
                elif char == "b":
                    box = Box(self.__images.BOX, pos_x, pos_y, width, height)
                    level.get_movables().add(box)
                elif char == "s":
                    boxspot = BoxSpot(self.__images.BOXSPOT, pos_x, pos_y, width, height)
                    level.get_boxspots().add(boxspot)

        return level