from classes.GameObject import GameObject

# class Obstacle
class Obstacle(GameObject):
    def __init__(self, image, x, y, width, height):
        super().__init__(image, x, y, width, height)