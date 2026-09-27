from classes.MovableObject import MovableObject

class Player(MovableObject):
    def __init__(self, image_right, x, y, width, height, image_left):
        super().__init__( image_right, x, y, width, height)
        self.__score = int(0) 
        self.__move_count = int(0)
        self._image_left = image_left
        self._image_right = image_right      
        
    def get_score(self):
        return self.__score

    def get_moves(self):
        return self.__move_count 
    
    # player moves
    def move(self, dx, dy):
        if dx < 0:
            self.set_image(self._image_left)
        elif dx > 0:
            self.set_image(self._image_right)
        
        self.__move_count += 1
        self.add_move(dx,dy)

        # print player´s steps
        print("Steps:", self.__move_count)

    def set_score(self, time):
        self.__score = time  

