import pygame as pg
import pymunk.pygame_util
pymunk.pygame_util.positive_y_is_up = False

PER = WIDTH, HEIGHT = 1200, 1000
FPS = 60

pg.init()
display = pg.display.set_mode(PER)
time = pg.time.Clock()
draw_options = pymunk.pygame_util.DrawOptions(display)

place = pymunk.Space()
place.gravity = 0, 2000

while True:
    display.fill(pg.Color('White'))

    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()

    place.step(1 / FPS)
    place.debug_draw(draw_options)

    pg.display.flip()
    time.tick(FPS)