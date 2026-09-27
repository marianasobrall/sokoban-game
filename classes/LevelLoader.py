from classes.Level import Level
from classes.Player import Player
from classes.PineTree import PineTree
from classes.Box import Box
from classes.BoxSpot import BoxSpot
from classes.ImageCollection import ImageCollection
from Exception import InvalidCharacter, ExtraCharacter, MissingElement, BoxCount

class LevelLoader:
    def __init__(self, width, height, *args):
        # map to store levels
        self.__level_map = {} 
        self.load_levels(width, height,*args)   
                
    def load_levels(self, width, height, *num_files):
        # load levels from collections/level
        for num_file in num_files:
            level = self.__load_level( width, height, "collections/level" + str(num_file) + ".txt" )
            self.__level_map[num_file] = level

    # returns the number of loaded levels
    def get_level_count(self):
        return len(self.__level_map)
    
    # returns specific level
    def get_level(self, id_level):
        return self.__level_map[id_level]
        
    def __load_level(self, width, height, caminho_file):
        level_grid = [] 
        num_player = 0
        num_box = 0
        num_box_spot = 0
    
        # open file and read lines
        with open(caminho_file, 'r') as file:
            lines = file.readlines()
            #limited to the first 10 lines
            lines = lines[:10]
            # go line by line
            for line_number, line in enumerate(lines, start=1):
                line = line.strip()
                elements = list(line)
                
                try:
                    # check +10 elements
                    if len(elements) > 10: 
                        raise ExtraCharacter(f"Há mais do que 10 caracteres no {caminho_file} na linha {line_number}")      

                    # check -10 elements
                    if len(elements) < 10:  
                        raise MissingElement(f"Faltam {10 - len(elements)} no {caminho_file} elemento(s)  na linha {line_number}.")
                    
                    # check for invalid characters
                    for char in elements:
                        if char not in "pobs_":
                            raise InvalidCharacter(f"Caracter inválido '{char}' encontrado em {caminho_file}, linha {line_number}")

                #if there is an extra character, ignore
                except ExtraCharacter as e:
                    print(e)
                    elements = elements[:10] 

                #if there is a missing element, fill the space with _
                except MissingElement as e:
                    print(e)
                    elements.extend(['_'] * (10 - len(elements))) 

                # count elements 
                num_box += elements.count("b")
                num_box_spot += elements.count("s")
                num_player += elements.count("p")

                # add line on level_grid
                level_grid.append(elements)


        # raise exceptions 
        if num_player == 0:
            raise MissingElement(f"The player has not been found on {caminho_file}")
        elif num_player > 1:
            raise ExtraCharacter(f"There is more than 1 player on {caminho_file}")
        if num_box == 0:
            raise MissingElement(f"Box has not been found on {caminho_file}")
        if num_box_spot == 0:
            raise MissingElement(f"Box spot has not been found {caminho_file}")
        
        if num_box != num_box_spot:
            raise BoxCount(f"O número de boxes ({num_box}) não é igual ao número de box slots ({num_box_spot}) no {caminho_file}.")       
        
        # create the level  
        image = ImageCollection(width, height)
        level = Level(image)
                
        for y in range(len(level_grid)):  
            for x in range(len(level_grid[y])):  
                char = level_grid[y][x]
                if char == 'p':  
                    player = Player(image.PLAYER_RIGHT, x * width, y * height, width, height, image.PLAYER_LEFT)
                    level.set_player(player)
                elif char == 'o':  
                    obstacle = PineTree(image.PINETREE, x * width, y * height, width, height)
                    level.get_immovables().add(obstacle)
                elif char == 'b':  
                    box = Box(image.BOX, x * width, y * height, width, height)
                    level.get_movables().add(box)
                elif char == 's': 
                    boxspot = BoxSpot(image.BOXSPOT, x * width, y * height, width, height)
                    level.get_boxspots().add(boxspot)

        return level       