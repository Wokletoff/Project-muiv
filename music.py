import pygame as pg


class Music:

    @staticmethod
    def play_music():
        pg.mixer.pre_init(44100, -16, 2, 2048)
        pg.mixer.init()
        pg.mixer.music.load('sound/theme3.mp3')
        pg.mixer.music.play(10)
