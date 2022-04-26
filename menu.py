import pygame as pg
import sys
from random import randrange
from main import App
from music import Music
from options import Options


class Menu:
    def __init__(self):
        self.clock = pg.time.Clock()
        self.res = self.width, self.height = (1200, 800)
        self.screen = pg.display.set_mode(self.res, pg.SCALED)
        # menu
        self.menu_trigger = True
        self.menu_picture = pg.image.load("img/bg2.jpg").convert()
        # font
        self.font = pg.font.SysFont("Arial", 36, bold=True)

    def run(self):
        x = 0
        button_font = pg.font.Font('font/font.ttf', 72)
        label_font = pg.font.Font('font/font1.otf', 400)
        start = button_font.render('START', 1, pg.Color('lightgray'))
        button_start = pg.Rect(0, 0, 400, 150)
        button_start.center = 800, 450 - 100
        options = button_font.render('OPTION', 1, pg.Color('lightgray'))
        button_options = pg.Rect(0, 0, 400, 150)
        button_options.center = 800, 450 + 70
        exit = button_font.render('EXIT', 1, pg.Color('lightgray'))
        button_exit = pg.Rect(0, 0, 400, 150)
        button_exit.center = 800, 450 + 250

        while self.menu_trigger:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            self.screen.blit(self.menu_picture, (0, 0), (x % 1200, 400, 1200, 800))
            x += 1

            pg.draw.rect(self.screen, (0, 0, 0), button_start, border_radius=25, width=10)
            self.screen.blit(start, (button_start.centerx - 120, button_start.centery - 60))

            pg.draw.rect(self.screen, (0, 0, 0), button_options, border_radius=25, width=10)
            self.screen.blit(options, (button_options.centerx - 150, button_options.centery - 60))

            pg.draw.rect(self.screen, (0, 0, 0), button_exit, border_radius=25, width=10)
            self.screen.blit(exit, (button_exit.centerx - 80, button_exit.centery - 60))

            color = randrange(30)

            label = label_font.render('Ground', True, (color, color, color))
            self.screen.blit(label, (15, -30))

            mouse_pos = pg.mouse.get_pos()
            mouse_click = pg.mouse.get_pressed()
            if button_start.collidepoint(mouse_pos):
                pg.draw.rect(self.screen, color, button_start, border_radius=25)
                self.screen.blit(start, (button_start.centerx - 120, button_start.centery - 60))
                if mouse_click[0]:
                    # action at click
                    app = App()
                    app.run()

            elif button_options.collidepoint(mouse_pos):
                pg.draw.rect(self.screen, color, button_options, border_radius=25)
                self.screen.blit(options, (button_options.centerx - 150, button_options.centery - 60))
                if mouse_click[0]:
                    # action at click
                    opp = Options()
                    opp.drawing()
                    self.menu_trigger = False

            elif button_exit.collidepoint(mouse_pos):
                pg.draw.rect(self.screen, color, button_exit, border_radius=25)
                self.screen.blit(exit, (button_exit.centerx - 80, button_exit.centery - 60))
                if mouse_click[0]:
                    pg.quit()
                    sys.exit()

            pg.display.flip()
            self.clock.tick(20)


if __name__ == "__main__":
    Music.play_music()
    pg.init()
    manu = Menu()
    manu.run()