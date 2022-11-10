import pygame as pg
from settings import Settings
import game_functions as gf

from laser import Lasers, LaserType
from alien import Aliens
from ship import Ship
from sound import Sound
from scoreboard import Scoreboard
from barrier import Barriers
#from menu import Menu
import sys


class Game:

    def __init__(self):
        pg.init()
        self.settings = Settings()
        size = self.settings.screen_width, self.settings.screen_height  # tuple
        self.screen = pg.display.set_mode(size=size)
        self.screen_rect = self.screen.get_rect()
        pg.display.set_caption("Space Invaders")

        self.high_scores()
        self.click = False
        self.game_is_active = False
        self.high_score_menu_flag = False

        self.sound = Sound(bg_music="sounds/Background_music.wav")
        self.scoreboard = Scoreboard(game=self)
        self.ship_lasers = Lasers(settings=self.settings, type=LaserType.SHIP)
        self.alien_lasers = Lasers(settings=self.settings, type=LaserType.ALIEN)
        self.barriers = Barriers(game=self)
        self.ship = Ship(game=self)
        self.aliens = Aliens(game=self)
        #self.ufo = UFO(game=self)
        self.settings.initialize_speed_settings()
        self.game_is_over = False

        #self.menu = Menu(settings=self.settings, screen=self.screen)

        #self.play_button = Button(settings=self.settings, screen=self.screen, msg="Play")
        #self.high_score_button = high_score_button(settings=self.settings, screen=self.screen, msg="High Score")  

        self.title_1 = pg.font.SysFont(None, 100)
        self.title_2 = pg.font.SysFont(None, 100)
        self.menu_font = pg.font.SysFont(None, 40)

    def reset(self):
        print('Resetting game...')

        self.ship.reset()
        self.aliens.reset()
        self.ship_lasers.reset()
        self.alien_lasers.reset()
        self.sound.reset_bg_music(self.game_is_over)
        if self.game_is_over:
            self.barriers.reset()
            self.scoreboard.reset()
            self.game_is_over = False

    def high_scores(self):
        f = open('high_scores.txt', 'r')
        f.close()

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

    def game_over(self):
        print('All ships gone: game over!')

        self.sound.gameover()
        self.game_is_over = True
        self.check_high_score()
        self.reset()
        #self.menu.title_menu()
        self.title_menu()

    def check_high_score(self):
        print("Score: ", self.scoreboard.score)
        high_score_text = open("high_scores.txt", "r+")
        high_score_list = [int(num) for num in high_score_text.read().split()]
        min_value = min(high_score_list)

        if self.scoreboard.all_time_high_score < self.scoreboard.score or self.scoreboard.score > min_value:
            for n in range(len(high_score_list)):
                if min_value == high_score_list[n]:
                    high_score_list[n] = self.scoreboard.score
                    break

            string_list = [str(x) + "\n" for x in high_score_list]
            high_score_text.seek(0)
            high_score_text.writelines(string_list)
            high_score_text.close()

    def play(self):
        self.ship.ship_limit = self.settings.ship_limit
        self.sound.play_bg()
        while True:  # at the moment, only exits in gf.check_events if Ctrl/Cmd-Q pressed
            gf.check_events(settings=self.settings, ship=self.ship)
            self.screen.fill(self.settings.bg_color)
            self.ship.update()
            self.aliens.update()
            self.barriers.update()
            self.scoreboard.update()
            pg.display.flip()

#Attempted to implement in menu.py however due to time constraints, moved the functions to be called in game.py
    def title_menu(self):
        self.sound.play_bg()
        start_text = self.menu_font.render('PLAY', True, (255, 255, 255))
        high_score_text = self.menu_font.render('HIGH SCORES', True, (255, 255, 255))
        start_text_rect = start_text.get_rect(center=(self.settings.screen_width / 2, 600))
        high_score_text_rect = high_score_text.get_rect(center=(self.settings.screen_width / 2, 700))
        alien_0 = pg.image.load('images/alien/alien00.png')
        alien_1 = pg.image.load('images/alien/alien10.png')
        alien_2 = pg.image.load('images/alien/alien20.png')
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
                            self.play()
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
            alien_0_points = self.menu_font.render('= 10 PTS', True, (255, 255, 255))
            alien_1_points = self.menu_font.render('= 20 PTS', True, (255, 255, 255))
            alien_2_points = self.menu_font.render('= 40 PTS', True, (255, 255, 255))
            ufo_points = self.menu_font.render('= ???', True, (255, 255, 255))

            title_1_rect = title_1.get_rect(center=(self.settings.screen_width / 2, 100))
            title_2_rect = title_2.get_rect(center=(self.settings.screen_width / 2, 175))

            alien_0_points_rect = alien_0_points.get_rect(center=(self.settings.screen_width / 2, 300))
            alien_1_points_rect = alien_1_points.get_rect(center=(self.settings.screen_width / 2, 350))
            alien_2_points_rect = alien_2_points.get_rect(center=(self.settings.screen_width / 2, 400))
            ufo_points_rect = ufo_points.get_rect(center=(self.settings.screen_width / 2, 450))

            self.screen.blit(title_1, title_1_rect)
            self.screen.blit(title_2, title_2_rect)
            self.screen.blit(alien_0, (450, 280))
            self.screen.blit(alien_0_points, alien_0_points_rect)
            self.screen.blit(alien_1, (450, 330))
            self.screen.blit(alien_1_points, alien_1_points_rect)
            self.screen.blit(alien_2, (450, 380))
            self.screen.blit(alien_2_points, alien_2_points_rect)
            self.screen.blit(ufo, (444, 430))
            self.screen.blit(ufo_points, ufo_points_rect)
            self.screen.blit(start_text, start_text_rect)
            self.screen.blit(high_score_text, high_score_text_rect)

            pg.display.update()

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


def main():
    g = Game()
    #g.menu.title_menu()
    g.title_menu()
    # g.play()


if __name__ == '__main__':
    main()
