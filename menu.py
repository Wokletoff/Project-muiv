import pygame as pg
import sys
from random import randrange


class Menu:
    def __init__(self):
        self.clock = pg.time.Clock()
        self.res = self.width, self.height = (1200, 800)
        self.screen = pg.display.set_mode(self.res, pg.SCALED)
        # menu
        self.menu_trigger = True
        self.menu_picture = pg.image.load("bcgd.jpg").convert()
        # font
        self.font = pg.font.SysFont("Arial", 36, bold=True)

    def update(self):
        x = 0
        button_font = pg.font.Font('font.ttf', 72)
        label_font = pg.font.Font('font1.otf', 400)
        start = button_font.render('START', 1, pg.Color('lightgray'))
        button_start = pg.Rect(0, 0, 400, 150)
        button_start.center = 800, 450
        exit = button_font.render('EXIT', 1, pg.Color('lightgray'))
        button_exit = pg.Rect(0, 0, 400, 150)
        button_exit.center = 800, 450 + 200

        while self.menu_trigger:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            self.screen.blit(self.menu_picture, (0, 0), (x % 1200, 400, 1200, 800))
            x += 1

            pg.draw.rect(self.screen, (0, 0, 0), button_start, border_radius=25, width=10)
            self.screen.blit(start, (button_start.centerx - 130, button_start.centery - 70))

            pg.draw.rect(self.screen, (0, 0, 0), button_exit, border_radius=25, width=10)
            self.screen.blit(exit, (button_exit.centerx - 85, button_exit.centery - 70))

            color = randrange(40)

            label = label_font.render('GroundMap', 1, (color, color, color))
            self.screen.blit(label, (15, -30))

            mouse_pos = pg.mouse.get_pos()
            mouse_click = pg.mouse.get_pressed()
            if button_start.collidepoint(mouse_pos):
                pg.draw.rect(self.screen, color, button_start, border_radius=25)
                self.screen.blit(start, (button_start.centerx - 130, button_start.centery - 70))
                if mouse_click[0]:
                    # action at click
                    self.menu_trigger = False

            elif button_exit.collidepoint(mouse_pos):
                pg.draw.rect(self.screen, color, button_exit, border_radius=25)
                self.screen.blit(exit, (button_exit.centerx - 85, button_exit.centery - 70))
                if mouse_click[0]:
                    pg.quit()
                    sys.exit()

            pg.display.flip()
            self.clock.tick(20)