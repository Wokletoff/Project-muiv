import pygame as pg
import sys
from random import randrange
from settings import settings
from main import App
from music import Music


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
        button_start.center = 600, 450 - 100

        about = button_font.render('CRED', 1, pg.Color('lightgray'))
        button_about = pg.Rect(0, 0, 300, 150)
        button_about.center = 180, 450 + 250

        options = button_font.render('OPTION', 1, pg.Color('lightgray'))
        button_options = pg.Rect(0, 0, 400, 150)
        button_options.center = 600, 450 + 70

        exit = button_font.render('EXIT', 1, pg.Color('lightgray'))
        button_exit = pg.Rect(0, 0, 400, 150)
        button_exit.center = 600, 450 + 250

        help = button_font.render('HELP', 1, pg.Color('lightgray'))
        button_help = pg.Rect(0, 0, 300, 150)
        button_help.center = 1020, 450 + 250

        next_function = None
        while self.menu_trigger:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            self.screen.blit(self.menu_picture, (0, 0), (x % 1200, 400, 1200, 800))
            x += 1

            pg.draw.rect(self.screen, (0, 0, 0), button_start, border_radius=25, width=10)
            self.screen.blit(start, (button_start.centerx - 120, button_start.centery - 60))

            pg.draw.rect(self.screen, (0, 0, 0), button_help, border_radius=25, width=10)
            self.screen.blit(help, (button_help.centerx - 105, button_help.centery - 68))

            pg.draw.rect(self.screen, (0, 0, 0), button_about, border_radius=25, width=10)
            self.screen.blit(about, (button_about.centerx - 100, button_about.centery - 60))

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
                    app = App()
                    self.menu_trigger = False
                    next_function = app.run

            elif button_options.collidepoint(mouse_pos):
                pg.draw.rect(self.screen, color, button_options, border_radius=25)
                self.screen.blit(options, (button_options.centerx - 150, button_options.centery - 60))
                if mouse_click[0]:
                    self.menu_trigger = False
                    next_function = self.option

            elif button_about.collidepoint(mouse_pos):
                pg.draw.rect(self.screen, color, button_about, border_radius=25)
                self.screen.blit(about, (button_about.centerx - 100, button_about.centery - 60))
                if mouse_click[0]:
                    self.menu_trigger = False
                    next_function = self.credits

            elif button_help.collidepoint(mouse_pos):
                pg.draw.rect(self.screen, color, button_help, border_radius=25)
                self.screen.blit(help, (button_help.centerx - 150, button_help.centery - 60))
                if mouse_click[0]:
                    # action at click
                    self.menu_trigger = False
                    next_function = self.help

            elif button_exit.collidepoint(mouse_pos):
                pg.draw.rect(self.screen, color, button_exit, border_radius=25)
                self.screen.blit(exit, (button_exit.centerx - 80, button_exit.centery - 60))
                if mouse_click[0]:
                    pg.event.post(pg.event.Event(pg.QUIT))

            pg.display.flip()
            self.clock.tick(20)
        if next_function:
            self.menu_trigger = True
            next_function()

    def option(self):
        x = 0
        button_font = pg.font.Font('font/font.ttf', 72)
        label_font = pg.font.Font('font/font1.otf', 350)

        volume = button_font.render('Mapchange', 1, pg.Color('lightgray'))
        button_mapchane = pg.Rect(0, 0, 600, 150)
        button_mapchane.center = 600, 450 - 100

        back = button_font.render('BACK', 1, pg.Color('lightgray'))
        button_back = pg.Rect(0, 0, 250, 100)
        button_back.center = 1070, 450 + 280

        next_function = None

        while self.menu_trigger:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            self.screen.blit(self.menu_picture, (0, 0), (x % 1200, 400, 1200, 800))
            x += 1

            pg.draw.rect(self.screen, (0, 0, 0), button_mapchane, border_radius=25, width=10)
            self.screen.blit(volume, (button_mapchane.centerx - 240, button_mapchane.centery - 68))

            pg.draw.rect(self.screen, (0, 0, 0), button_back, border_radius=25, width=10)
            self.screen.blit(back, (button_back.centerx - 105, button_back.centery - 68))

            color = randrange(40)

            label = label_font.render('Options', 1, (color, color, color))
            self.screen.blit(label, (15, -30))

            text = button_font.render(f"{settings.int_map}", 1, (color, color, color))
            self.screen.blit(text, (970, 280))

            mouse_pos = pg.mouse.get_pos()
            mouse_click = pg.mouse.get_pressed()

            if button_back.collidepoint(mouse_pos):
                pg.draw.rect(self.screen, color, button_back, border_radius=25)
                self.screen.blit(back, (button_back.centerx - 105, button_back.centery - 68))
                if mouse_click[0]:
                    # action at click
                    self.menu_trigger = False
                    next_function = self.run

            elif button_mapchane.collidepoint(mouse_pos):
                pg.draw.rect(self.screen, color, button_mapchane, border_radius=25)
                self.screen.blit(volume, (button_mapchane.centerx - 240, button_mapchane.centery - 68))
                if mouse_click[0]:
                        def func(self, int_map):
                            settings.int_map += 1
                            if settings.int_map > 3:
                                settings.int_map = 1
                        func(self, settings._int_map)


            pg.display.flip()
            self.clock.tick(20)

        if next_function:
            self.menu_trigger = True
            next_function()

    def credits(self):
        x = 0
        button_font = pg.font.Font('font/font.ttf', 72)
        text_font = pg.font.Font('font/font.ttf', 100)
        text_font2 = pg.font.Font('font/font.ttf', 20)
        label_font = pg.font.Font('font/font1.otf', 350)

        back = button_font.render('BACK', 1, pg.Color('lightgray'))
        button_back = pg.Rect(0, 0, 250, 100)
        button_back.center = 1070, 450 + 280

        next_function = None

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
                    next_function = self.run

            pg.display.flip()
            self.clock.tick(20)

        if next_function:
            self.menu_trigger = True
            next_function()

    def help(self):
        x = 0
        button_font = pg.font.Font('font/font.ttf', 72)
        text_font = pg.font.Font('font/font.ttf', 40)
        label_font = pg.font.Font('font/font1.otf', 350)

        back = button_font.render('BACK', 1, pg.Color('lightgray'))
        button_back = pg.Rect(0, 0, 250, 100)
        button_back.center = 1070, 450 + 280

        next_function = None

        while self.menu_trigger:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            self.screen.blit(self.menu_picture, (0, 0), (x % 1200, 400, 1200, 800))
            x += 1

            color = randrange(40)

            label = label_font.render('HELP', 1, (color, color, color))
            self.screen.blit(label, (300, -30))

            text1 = text_font.render("Control position - (WASD, Q, E)", 1, (color, color, color))
            self.screen.blit(text1, (40, 350))

            text2 = text_font.render("Control ??amera (up, down, left, right)", 1, (color, color, color))
            self.screen.blit(text2, (40, 400))

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
                    next_function = self.run

            pg.display.flip()
            self.clock.tick(20)

        if next_function:
            self.menu_trigger = True
            next_function()


if __name__ == "__main__":
    Music.play_music()
    pg.init()
    menu = Menu()
    menu.run()
