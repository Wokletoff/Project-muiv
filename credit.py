import pygame as pg
import sys
from random import randrange


class About:
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
        text_font = pg.font.Font('font/font.ttf', 100)
        text_font2 = pg.font.Font('font/font.ttf', 20)
        label_font = pg.font.Font('font/font1.otf', 350)

        back = button_font.render('BACK', 1, pg.Color('lightgray'))
        button_back = pg.Rect(0, 0, 250, 100)
        button_back.center = 1070, 450 + 280

        while self.menu_trigger:
             for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

             self.screen.blit(self.menu_picture, (0, 0), (x % 1200, 400, 1200, 800))
             x += 1

             color = randrange(40)

             label = label_font.render('CREDIT', 1, (color, color, color))
             self.screen.blit(label, (100, -30))

             text1 = text_font.render("!!!Thanks for play!!!", 1, (color, color, color))
             self.screen.blit(text1, (40, 350))

             text2 = text_font2.render("Credit by Woklet", 1, (color, color, color))
             self.screen.blit(text2, (20, 750))

             pg.draw.rect(self.screen, (0, 0, 0), button_back, border_radius=25, width=10)
             self.screen.blit(back, (button_back.centerx - 105, button_back.centery - 68))

             mouse_pos = pg.mouse.get_pos()
             mouse_click = pg.mouse.get_pressed()
             if button_back.collidepoint(mouse_pos):
                 pg.draw.rect(self.screen, color, button_back, border_radius=25)
                 self.screen.blit(back, (button_back.centerx - 105, button_back.centery - 68))
                 if mouse_click[0]:
                     # action at click

                     self.menu_trigger = False


             pg.display.flip()
             self.clock.tick(20)