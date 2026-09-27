import pygame

def collision_obstacles(func):
    def wrapper(self, player, dx, dy, level):
        player.add_move(dx, dy) # nova posição player

        # checks if player is outside of the grid
        if not (0 <= player.rect.x < self.display_width and 0 <= player.rect.y < self.display_height):
            player.remove_move(dx, dy) # back
            return False

        # check collisions with obstacles
        collided_obstacles = pygame.sprite.spritecollide(player, level.get_immovables(), dokill=False)

        if collided_obstacles: 
            player.remove_move(dx, dy) # back
            return False

        # no collision
        player.remove_move(dx, dy) # back
        return func(self, player, dx, dy, level)
    return wrapper


def collision_boxes(func):
    def wrapper(self, player, dx, dy, level):
        player.add_move(dx, dy)

        # check collisions with boxes
        collided_boxes = pygame.sprite.spritecollide(player, level.get_movables(), dokill=False)

        if collided_boxes: 
            collided_box = collided_boxes[0] 

            # new box position
            collided_box.add_move(dx, dy)

            # checks if box goes outside the grid
            if not ((0 <= collided_box.rect.x < self.display_width and 0 <= collided_box.rect.y < self.display_height)):
                collided_box.remove_move(dx, dy) #volta
                player.remove_move(dx, dy)
                return False

            # remove collided box from boxes
            level.get_movables().remove(collided_box)
            # verifica colisão da caixa com outras caixas
            if pygame.sprite.spritecollide(collided_box, level.get_movables(), dokill=False):
                collided_box.remove_move(dx, dy) #back
                player.remove_move(dx, dy)    
                level.get_movables().add(collided_box)
                return False
            level.get_movables().add(collided_box) #adds collided box back to the group

            # checks box collision with obstacles
            if pygame.sprite.spritecollide(collided_box, level.get_immovables(), dokill=False):
                collided_box.remove_move(dx, dy) #volta
                player.remove_move(dx, dy)
                return False

        player.remove_move(dx, dy)
        return func(self, player, dx, dy, level)
    return wrapper
