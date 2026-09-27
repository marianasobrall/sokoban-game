"""Collision validation decorators controlling player and box transitions."""

from functools import wraps
import pygame


def collision_obstacles(func):
    """Validates grid boundaries and immovable collisions before executing a move."""
    @wraps(func)
    def wrapper(self, player, dx, dy, level):
        player.add_move(dx, dy)

        # Check if proposed position exceeds grid bounds
        if not (0 <= player.rect.x < self.display_width and 0 <= player.rect.y < self.display_height):
            player.remove_move(dx, dy)
            return False

        # Check collisions with static obstacles
        collided_obstacles = pygame.sprite.spritecollide(player, level.get_immovables(), dokill=False)
        if collided_obstacles:
            player.remove_move(dx, dy)
            return False

        player.remove_move(dx, dy)
        return func(self, player, dx, dy, level)

    return wrapper


def collision_boxes(func):
    """Validates box chain pushing, obstacle impacts, and grid edges."""
    @wraps(func)
    def wrapper(self, player, dx, dy, level):
        player.add_move(dx, dy)

        collided_boxes = pygame.sprite.spritecollide(player, level.get_movables(), dokill=False)
        if collided_boxes:
            collided_box = collided_boxes[0]
            collided_box.add_move(dx, dy)

            # Check if pushed box exceeds grid boundaries
            if not (0 <= collided_box.rect.x < self.display_width and 0 <= collided_box.rect.y < self.display_height):
                collided_box.remove_move(dx, dy)
                player.remove_move(dx, dy)
                return False

            # Check if box collides with another box (simultaneous pushing is prohibited)
            level.get_movables().remove(collided_box)
            if pygame.sprite.spritecollide(collided_box, level.get_movables(), dokill=False):
                collided_box.remove_move(dx, dy)
                player.remove_move(dx, dy)
                level.get_movables().add(collided_box)
                return False
            level.get_movables().add(collided_box)

            # Check if box hits an obstacle
            if pygame.sprite.spritecollide(collided_box, level.get_immovables(), dokill=False):
                collided_box.remove_move(dx, dy)
                player.remove_move(dx, dy)
                return False

        player.remove_move(dx, dy)
        return func(self, player, dx, dy, level)

    return wrapper