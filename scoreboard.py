import pygame as pg 
import csv
# import pygame.font

class Scoreboard:
    def __init__(self, game): 
        self.score = 0
        self.level = 0
        self.high_score = 0
        
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.text_color = (30, 30, 30)
        self.font = pg.font.SysFont(None, 48)

        self.score_image = None 
        self.score_rect = None
        self.prep_score()

        self.load_high_score()
        self.high_score_image = None
        self.high_score_rect = None
        self.prep_high_score()


    def increment_score(self): 
        self.score += self.settings.alien_points
        self.prep_score()

    def prep_score(self): 
        score_str = str(self.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def write_high_score(self):
        file_object = open("score.txt", "w")
        file_object.write(str(self.high_score))
        file_object.close()

    def load_high_score(self):
        with open("score.txt", "r") as file:
            high_score_read = int(file.read())
            print(high_score_read)

            if high_score_read > self.high_score:
                self.high_score = high_score_read


    def prep_high_score(self):
        high_score_str = str(self.high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.center = self.screen_rect.center
        self.high_score_rect.top = 20

    def reset(self): 
        self.high_score = self.score
        self.write_high_score()
        self.score = 0
        self.update()

    def update(self): 
        # TODO: other stuff
        self.draw()

    def draw(self): 
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)