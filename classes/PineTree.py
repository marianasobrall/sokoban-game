from classes.Obstacle import Obstacle

# class PineTree
class PineTree(Obstacle):
    def __init__(self, image, x, y, width, height):
        super().__init__(image, x, y, width, height)