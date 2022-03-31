import pygame as pg
from player import Player
from voxel_render import VoxelRender
import sys
from menu import menu
from random import randrange


class App:
    def __init__(self):
        self.res = self.width, self.height = (800, 400)
        self.screen = pg.display.set_mode(self.res, pg.SCALED)
        self.clock = pg.time.Clock()
        self.player = Player()
        self.voxel_render = VoxelRender(self)
        # menu
        self.menu_trigger = True
        self.menu_picture = pg.image.load("bcgd.jpg").convert()
        # font
        self.font = pg.font.SysFont("", 36, bold=True)

    def update(self):
        self.player.update()
        self.voxel_render.update()

    def draw(self):
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
                    self.menu_trigger = False

            color = randrange(40)
            label = label_font.render('GroundMap', 1, (color, color, color))
            self.screen.blit(label, (15, -30))
            mouse_pos = pg.mouse.get_pos()
            mouse_click = pg.mouse.get_pressed()
            if button_start.collidepoint(mouse_pos):
                pg.draw.rect(self.screen, color, button_start, border_radius=25)
                self.screen.blit(start, (button_start.centerx - 130, button_start.centery - 70))
                if mouse_click[0]:
                    pass
            elif button_exit.collidepoint(mouse_pos):
                pg.draw.rect(self.screen, color, button_exit, border_radius=25)
                self.screen.blit(exit, (button_exit.centerx - 85, button_exit.centery - 70))
                if mouse_click[0]:
                    self.menu_trigger = False

            pg.display.flip()
            self.clock.tick(40)

    def run(self):
        while True:
            self.update()
            self.draw()

            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            self.clock.tick(60)
            pg.display.set_caption(f"FPS: {self.clock.get_fps()}")


if __name__ == "__main__":
    pg.init()
    app = App()
    app.run()
