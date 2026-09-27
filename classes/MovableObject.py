from classes.GameObject import GameObject

class MovableObject(GameObject):
    def __init__(self, image, x, y, width, height):
        super().__init__(image, x, y, width, height)

    # add moves
    def add_move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    # remove moves
    def remove_move(self, dx, dy):
        self.rect.x -= dx
        self.rect.y -= dy
