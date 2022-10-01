import pygame as pg
from settings import Settings

class menu():
    def __init__(self, game):
        self.settings = Settings()
        self.game = game
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = -100
    
    def draw_text(self, text, size, x, y):
        font = pg.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface, text_rect)
