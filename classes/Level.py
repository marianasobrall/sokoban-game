"""Level management module holding entities and victory conditions."""

import pygame
from classes.ImageCollection import ImageCollection


class Level:
    """Stores, renders, and evaluates completion states for an active level."""

    def __init__(self, images: ImageCollection):
        self.__player = None
        self.__immovable_objects = pygame.sprite.Group()
        self.__movable_objects = pygame.sprite.Group()
        self.__boxspot_objects = pygame.sprite.Group()
        self.__images = images
        self.__background_image = self.__images.LAND

    def set_player(self, player) -> None:
        """Sets the player instance."""
        self.__player = player

    def get_player(self):
        """Returns the player instance."""
        return self.__player

    def get_immovables(self) -> pygame.sprite.Group:
        """Returns immovable obstacle sprites."""
        return self.__immovable_objects

    def get_movables(self) -> pygame.sprite.Group:
        """Returns pushable box sprites."""
        return self.__movable_objects

    def get_boxspots(self) -> pygame.sprite.Group:
        """Returns target box spot sprites."""
        return self.__boxspot_objects

    def draw(self, game_display: pygame.Surface) -> None:
        """Renders the 10x10 background and all entities in layering order."""
        for y in range(10):
            for x in range(10):
                game_display.blit(
                    self.__background_image,
                    (x * self.__images.width, y * self.__images.height),
                )

        # Slots are drawn first so that boxes and player sit on top of them
        for box_spot in self.__boxspot_objects:
            game_display.blit(box_spot.get_image(), box_spot.get_rectangle())

        for obstacle in self.__immovable_objects:
            game_display.blit(obstacle.get_image(), obstacle.get_rectangle())

        for obj in self.__movable_objects:
            game_display.blit(obj.get_image(), obj.get_rectangle())

        if self.__player:
            game_display.blit(self.__player.get_image(), self.__player.get_rectangle())

    def update_box_spots(self) -> None:
        """Checks collisions between boxes and spots, updating each spot's state."""
        for box_spot in self.__boxspot_objects:
            has_box = any(
                box_spot.get_rectangle().colliderect(box.get_rectangle())
                for box in self.__movable_objects
            )
            box_spot.set_contains_box(has_box)

    def completed(self) -> bool:
        """Returns True if every box spot currently contains a box."""
        self.update_box_spots()
        return all(box_spot.contains_box() for box_spot in self.__boxspot_objects)