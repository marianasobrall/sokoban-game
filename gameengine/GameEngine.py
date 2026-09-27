import pygame
from classes.LevelLoader import LevelLoader
from Decorators import collision_obstacles, collision_boxes

import time

class GameEngine:
    def __init__(self, display_width, display_height, fps):
        self.display_width = display_width
        self.display_height = display_height
        self.fps = fps
        self.current_level = 1

    def run(self):
        pygame.init()
        game_display = pygame.display.set_mode((self.display_width, self.display_height))

        # game name
        game_name = "SokobanDaWish"
        pygame.display.set_caption(game_name)

        # initialize game clock
        clock = pygame.time.Clock()

        # initialize white color
        white = (255, 255, 255)

        # paint initial state of screen 
        game_display.fill(white)

        # load level
        levels = LevelLoader(self.display_width/10, self.display_height/10, 1, 2, 3, 4, 5)
        level = levels.get_level(self.current_level)
        
        inicio_tempo = time.time()
        # run game
        crashed = False
        while not crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True 

            # detects pressed on keys
                if event.type == pygame.KEYDOWN: 
                    dx, dy = 0, 0 
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s: 
                        dy = self.display_width/10
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        dy = -self.display_width/10
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        dx = -self.display_width/10
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        dx = self.display_width/10
                    
                    # move player
                    player = level.get_player()                   
                    self.move_player(player, dx, dy, level) 

                    # check if level is completed
                    if level.completed():
                        fim_tempo = time.time()
                        player.set_score(fim_tempo - inicio_tempo)

                        print("Level", self.current_level, "completed!")
                        print(player.get_moves(), "steps on level", self.current_level)
                        print(round(player.get_score(), 2), "seconds on level", self.current_level)
                        
                        # goes to next level
                        self.current_level += 1
                        if self.current_level <= levels.get_level_count():
                            level = levels.get_level(self.current_level)
                            inicio_tempo = time.time()
                        else: # if last level, finish game
                            print("Você completou todos os níveis!")
                            crashed = True        
                

            #draws level
            level.draw(game_display)  
            
            pygame.display.update()
            clock.tick(self.fps)

        pygame.quit()


    # checks if the player can move
    @collision_obstacles
    @collision_boxes
    def move_player(self, player, dx, dy, level):
        # if there is movement
        if dx != 0 or dy != 0: 
            # move player
            player.move(dx, dy) 


        


