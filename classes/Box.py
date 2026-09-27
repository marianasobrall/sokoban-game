from classes.MovableObject import MovableObject

# class Box
class Box(MovableObject):
    def __init__(self, image, x, y, width, height):
        super().__init__(image, x, y, width, height)
        