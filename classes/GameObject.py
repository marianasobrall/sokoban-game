import pygame

#class GameObject
class GameObject(pygame.sprite.Sprite):
    def __init__(self, image, x, y, width, height):
        super().__init__()
        self._surface = pygame.Surface((width, height))
        self._image = image
        self._rectangle = self._image.get_rect()
        self.set_new_position(x, y)
        self.rect = self.get_rectangle()
        
    def get_surface(self):
        return self._surface
    
    def get_image(self):
        return self._image
    
    def get_rectangle(self):
        return self._rectangle
    
    def set_image(self, image):
        self._image = image
    
    def set_new_position(self, x, y):
        self._rectangle.topleft = (x, y)
    
    def update():
        pass
