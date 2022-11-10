import pygame as pg
from settings import Settings
from alien import Alien 
import game as Game
import sys

class Menu():
    def __init__(self, settings, screen):
        self.title_1 = pg.font.SysFont(None, 100)
        self.title_2 = pg.font.SysFont(None, 100)
        self.menu_font = pg.font.SysFont(None, 40)
        self.settings = settings
        self.screen = screen

    def title_menu(self):
        start_text = self.menu_font.render('PLAY', True, (255, 255, 255))
        high_score_text = self.menu_font.render('HIGH SCORES', True, (255, 255, 255))
        start_text_rect = start_text.get_rect(center=(self.settings.screen_width / 2, 600))
        high_score_text_rect = high_score_text.get_rect(center=(self.settings.screen_width / 2, 700))
        alien_1 = pg.image.load('images/alien/alien00.png')
        alien_2 = pg.image.load('images/alien/alien10.png')
        alien_3 = pg.image.load('images/alien/alien20.png')
        ufo = pg.image.load('images/alien/alien3.png')

        while True:
            start_button = start_text_rect
            high_score_button = high_score_text_rect
            mx, my = pg.mouse.get_pos()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.click = True
                    if start_button.collidepoint((mx, my)):
                        if self.click:
                            self.click = False
                            Game.play()
                    if high_score_button.collidepoint((mx, my)):
                        if self.click:
                            self.click = False
                            print("This should go to the high score screen")
                            self.high_scores_menu()
                if event.type == pg.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.click = False


            # Write the Main Menu
            self.screen.fill((0, 0, 0))

            title_1 = self.title_1.render('SPACE', True, (255, 255, 255))
            title_2 = self.title_2.render('INVADERS', True, (0, 255, 0))
            alien_1_points = self.menu_font.render('= 10 PTS', True, (255, 255, 255))
            alien_2_points = self.menu_font.render('= 20 PTS', True, (255, 255, 255))
            alien_3_points = self.menu_font.render('= 40 PTS', True, (255, 255, 255))
            ufo_points = self.menu_font.render('= ???', True, (255, 255, 255))

            title_1_rect = title_1.get_rect(center=(self.settings.screen_width / 2, 100))
            title_2_rect = title_2.get_rect(center=(self.settings.screen_width / 2, 175))

            alien_1_points_rect = alien_1_points.get_rect(center=(self.settings.screen_width / 2, 300))
            alien_2_points_rect = alien_2_points.get_rect(center=(self.settings.screen_width / 2, 350))
            alien_3_points_rect = alien_3_points.get_rect(center=(self.settings.screen_width / 2, 400))
            ufo_points_rect = ufo_points.get_rect(center=(self.settings.screen_width / 2, 450))

            self.screen.blit(title_1, title_1_rect)
            self.screen.blit(title_2, title_2_rect)
            self.screen.blit(alien_1, (450, 280))
            self.screen.blit(alien_1_points, alien_1_points_rect)
            self.screen.blit(alien_2, (450, 330))
            self.screen.blit(alien_2_points, alien_2_points_rect)
            self.screen.blit(alien_3, (450, 380))
            self.screen.blit(alien_3_points, alien_3_points_rect)
            self.screen.blit(ufo, (444, 430))
            self.screen.blit(ufo_points, ufo_points_rect)
            self.screen.blit(start_text, start_text_rect)
            self.screen.blit(high_score_text, high_score_text_rect)

            pg.display.update()

    def get_high_scores(self):
        high_score_text = open("high_scores.txt", "r")
        high_score_list = [int(num) for num in high_score_text.read().split()]

        if self.high_score_menu_flag:
            high_score_text.close()
            return high_score_list

        max_score = max(high_score_list)
        high_score_text.close()
        print("High score is: ", max_score)
        return max_score            

    def high_scores_menu(self):
        self.high_score_menu_flag = True
        high_scores_text = self.menu_font.render('High Scores', True, (255, 255, 255))
        back_text = self.menu_font.render('Back', True, (255, 255, 255))
        high_scores_rect = high_scores_text.get_rect(center=(self.settings.screen_width / 2, 100))
        back_text_rect = back_text.get_rect(center=(self.settings.screen_width / 2, 700))

        high_score_list = self.get_high_scores()
        high_score_list.sort(reverse=True)

        ranking_1, ranking_2, ranking_3, ranking_4, ranking_5 = \
            high_score_list[0], high_score_list[1], high_score_list[2], high_score_list[3], high_score_list[4]

        while True:
            back_button = back_text_rect
            mx, my = pg.mouse.get_pos()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
                        sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.click = True
                    if back_button.collidepoint((mx, my)):
                        if self.click:
                            self.click = False
                            self.high_score_menu_flag = False
                            # self.reset()
                            self.title_menu()
                if event.type == pg.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.click = False

            self.screen.fill((0, 0, 0))
            ranking_1_text = self.menu_font.render(f'1. {ranking_1}', True, (255, 255, 255))
            ranking_1_rect = ranking_1_text.get_rect(center=(self.settings.screen_width / 2, 200))
            ranking_2_text = self.menu_font.render(f'2. {ranking_2}', True, (255, 255, 255))
            ranking_2_rect = ranking_2_text.get_rect(center=(self.settings.screen_width / 2, 250))
            ranking_3_text = self.menu_font.render(f'3. {ranking_3}', True, (255, 255, 255))
            ranking_3_rect = ranking_3_text.get_rect(center=(self.settings.screen_width / 2, 300))
            ranking_4_text = self.menu_font.render(f'4. {ranking_4}', True, (255, 255, 255))
            ranking_4_rect = ranking_4_text.get_rect(center=(self.settings.screen_width / 2, 350))
            ranking_5_text = self.menu_font.render(f'5. {ranking_5}', True, (255, 255, 255))
            ranking_5_rect = ranking_5_text.get_rect(center=(self.settings.screen_width / 2, 400))
            self.screen.blit(high_scores_text, high_scores_rect)
            self.screen.blit(back_text, back_text_rect)
            self.screen.blit(ranking_1_text, ranking_1_rect)
            self.screen.blit(ranking_2_text, ranking_2_rect)
            self.screen.blit(ranking_3_text, ranking_3_rect)
            self.screen.blit(ranking_4_text, ranking_4_rect)
            self.screen.blit(ranking_5_text, ranking_5_rect)
            pg.display.update()

