from classes.GameObject import GameObject

#class Stepable Object
class StepableObject(GameObject):
    def __init__(self, image, x, y, width, height):
        super().__init__(image, x, y, width, height)