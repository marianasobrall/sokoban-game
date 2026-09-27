from classes.StepableObject import StepableObject

#class BoxSpot
class BoxSpot(StepableObject):
    def __init__(self, image, x, y, width, height):
        super().__init__(image, x, y, width, height)
        self._contains_box = False

    def contains_box(self):
        return self._contains_box