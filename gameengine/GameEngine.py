"""Main game engine handling Pygame lifecycle, event loop, and level progression."""

import time
import pygame
from classes.LevelFactory import LevelFactory
from decorators import collision_obstacles, collision_boxes


class GameEngine:
    """Manages display initialization, player input, decorators, and level execution."""

    def __init__(self, display_width: int, display_height: int, fps: int):
        self.display_width = display_width
        self.display_height = display_height
        self.fps = fps
        self.current_level = 1

    def run(self) -> None:
        """Initializes Pygame, loads level configurations, and runs the game loop."""
        pygame.init()
        game_display = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption("SokobanDaWish")

        clock = pygame.time.Clock()
        background_color = (255, 255, 255)
        game_display.fill(background_color)

        cell_width = self.display_width // 10
        cell_height = self.display_height // 10

        # Load at least 5 levels as required by the assignment
        levels = LevelFactory(cell_width, cell_height, 1, 2, 3, 4, 5)
        level = levels.get_level(self.current_level)

        start_time = time.time()
        is_running = True

        while is_running:
            # 1. Event Handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False

                elif event.type == pygame.KEYDOWN:
                    dx, dy = 0, 0
                    if event.key in (pygame.K_DOWN, pygame.K_s):
                        dy = cell_height
                    elif event.key in (pygame.K_UP, pygame.K_w):
                        dy = -cell_height
                    elif event.key in (pygame.K_LEFT, pygame.K_a):
                        dx = -cell_width
                    elif event.key in (pygame.K_RIGHT, pygame.K_d):
                        dx = cell_width

                    if dx != 0 or dy != 0:
                        player = level.get_player()
                        self.move_player(player, dx, dy, level)

                        # Check level completion
                        if level.completed():
                            elapsed_time = time.time() - start_time
                            player.set_score(round(elapsed_time, 2))

                            print(f"\n--- Level {self.current_level} Completed ---")
                            print(f"Steps: {player.get_moves()}")
                            print(f"Time: {player.get_score()} seconds\n")

                            self.current_level += 1
                            if self.current_level <= levels.get_level_count():
                                level = levels.get_level(self.current_level)
                                start_time = time.time()
                            else:
                                print("Congratulations! You have completed all levels!")
                                is_running = False

            # 2. Rendering (outside event loop, per-frame)
            level.draw(game_display)
            pygame.display.update()

            # 3. Frame rate control
            clock.tick(self.fps)

        pygame.quit()

    @collision_obstacles
    @collision_boxes
    def move_player(self, player, dx: int, dy: int, level) -> None:
        """Translates the player across coordinates if permitted by collision decorators."""
        if dx != 0 or dy != 0:
            player.move(dx, dy)