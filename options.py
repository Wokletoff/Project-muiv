import pygame as pg
import sys
from random import randrange


class Options:
    def __init__(self):
        self.clock = pg.time.Clock()
        self.res = self.width, self.height = (1200, 800)
        self.screen = pg.display.set_mode(self.res, pg.SCALED)
        # menu
        self.menu_trigger = True
        self.menu_picture = pg.image.load("img/bg2.jpg").convert()
        # font
        self.font = pg.font.SysFont("Arial", 36, bold=True)

    def drawing(self):
        x = 0
        button_font = pg.font.Font('font/font.ttf', 72)
        label_font = pg.font.Font('font/font1.otf', 350)

        res = button_font.render('RESOLUTION', 1, pg.Color('lightgray'))
        button_res = pg.Rect(0, 0, 400, 150)
        button_res.center = 600, 450 - 100

        while self.menu_trigger:
             for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

             self.screen.blit(self.menu_picture, (0, 0), (x % 1200, 400, 1200, 800))
             x += 1

             color = randrange(40)

             label = label_font.render('Options', 1, (color, color, color))
             self.screen.blit(label, (15, -30))

             pg.display.flip()
             self.clock.tick(20)