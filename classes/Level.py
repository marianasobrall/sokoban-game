import pygame

# stores level information
class Level:
    def __init__(self, images):
        self.__player = None 
        self.__immovable_objects = pygame.sprite.Group()
        self.__movable_objects = pygame.sprite.Group()
        self.__boxspot_objects = pygame.sprite.Group()
        self.__images = images
        self.__background_image = self.__images.LAND    

    def set_player(self, player):
        self.__player = player

    def get_player(self):
        return self.__player

    def get_immovables(self):
        return self.__immovable_objects

    def get_movables(self):
        return self.__movable_objects

    def get_boxspots(self):
        return self.__boxspot_objects
    
    def draw(self, game_display):

        # fills with the land background
        for y in range(10):  
            for x in range(10):  
                game_display.blit(self.__background_image, (x * self.__images.width, y * self.__images.height))

        # draw box spots
        for box_spot in self.__boxspot_objects:
            game_display.blit(box_spot.get_image(), box_spot.get_rectangle())

        # draw obstacles
        for obstacle in self.__immovable_objects:
            game_display.blit(obstacle.get_image(), obstacle.get_rectangle())
        
        # draw boxes 
        for obj in self.__movable_objects:
            game_display.blit(obj.get_image(), obj.get_rectangle())
        
        # draw player
        game_display.blit(self.__player.get_image(), self.__player.get_rectangle())
    
    
    # updates the state of the boxspots
    def update_box_spots(self):
        for box_spot in self.__boxspot_objects:
            box_spot._contains_box = False  
            for box in self.__movable_objects:
                if box_spot.get_rectangle().colliderect(box.get_rectangle()):
                    box_spot._contains_box = True
                    break

    # checks if the level is over
    def completed(self):
        # update box spot before
        self.update_box_spots()

        for box_spot in self.get_boxspots():
            if not box_spot.contains_box():
                return False  
            
        return True  
