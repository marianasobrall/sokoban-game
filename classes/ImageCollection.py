import pygame

class ImageCollection:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        self.BOXSPOT = pygame.Surface((self.width, self.height))
        self.BOX = pygame.Surface((self.width, self.height))
        self.PLAYER_LEFT = pygame.Surface((self.width, self.height))
        self.PLAYER_RIGHT = pygame.Surface((self.width, self.height))
        self.LAND = pygame.Surface((self.width, self.height))
        self.PINETREE = pygame.Surface((self.width, self.height))
        
        self.load_images()  
        self.transform_scale()  

    # load images
    def load_images(self):
        self.BOXSPOT = pygame.image.load('images/box_spot.png')
        self.BOX = pygame.image.load('images/box.png')
        self.PLAYER_LEFT = pygame.image.load('images/fireman_left.png')
        self.PLAYER_RIGHT = pygame.image.load('images/fireman_right.png')
        self.LAND = pygame.image.load('images/land.png')
        self.PINETREE = pygame.image.load('images/pine.png')

    # transform image scale
    def transform_scale(self):
        self.BOXSPOT = pygame.transform.scale(self.BOXSPOT, (self.width, self.height))
        self.BOX = pygame.transform.scale(self.BOX, (self.width, self.height))
        self.PLAYER_LEFT = pygame.transform.scale(self.PLAYER_LEFT, (self.width, self.height))
        self.PLAYER_RIGHT = pygame.transform.scale(self.PLAYER_RIGHT, (self.width, self.height))
        self.LAND = pygame.transform.scale(self.LAND, (self.width, self.height))
        self.PINETREE = pygame.transform.scale(self.PINETREE, (self.width, self.height))