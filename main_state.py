import random
import json
import os
from pico2d import *

import game_framework
import subtitle
from tower import Tower
from uitower import Towerimage
name = "MainState"
global x, y, z, count, gamepause

gamepause = False
gameexitstate = False
count = 0
ingamepause = None
enemy = None
castle = None
pause = None
back = None
font = None
tower = None
towerui = None
towerset = None
towerimage = None


class Castle:

    def __init__(self):
        self.image = load_image('easymap.png')

    def draw(self):
        self.image.draw(400, 400)


class Ingamepause:
    def __init__(self):
        self.image = load_image('igp.png')

    def draw(self):
        self.image.draw(400, 400)


class Enemy:
    pass


class Back:
    def __init__(self):
        self.image = load_image('back.png')

    def draw(self):
        self.image.draw(730, 770)


def enter():
    global enemy, castle, pause, back, tower, towerimage, towerset, ingamepause
    enemy = Enemy()
    castle = Castle()
    towerset = [Tower() for i in range(15)]
    towerimage = Towerimage()

    ingamepause = Ingamepause()



    pass


def exit():
    pass


def handle_events():
    global x, y, z, castle, towerset, count, gamepause
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        if event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:


            if 220 < event.x < 300:
                if 330 < 800-event.y < 380:
                    if gameexitstate is True:
                        game_framework.change_state(subtitle)
                        gameexitstate = False

            if 510 < event.x < 570:
                if 330 < 800-event.y < 380:
                    gameexitstate = False

            if 690 < event.x < 730:
                if 770> 800 - event.y > 730:
                    gamepause = True


            if 25 < event.x < 65:
                if 45 < 800-event.y < 85:
                    towerset[count].state = True

        if event.type == SDL_MOUSEMOTION:

                towerset[count].x, towerset[count].y = event.x, 800 - event.y

        if event.type == SDL_MOUSEBUTTONUP and event.button == SDL_BUTTON_LEFT:
            if towerset[count].state:
                if 300 < 800-event.y < 600:
                    count = (count+1) % 15
                    towerset[count].state = False

        if event.type == SDL_KEYDOWN and event.key == SDLK_F10:
            if gamepause is True:
                 gamepause = False
                 pass

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            if gamepause is False:
                game_framework.change_state(subtitle)


def update():



    pass


def draw():
    if gamepause is False:
        clear_canvas()
        #객체를 통한 함수호출
        castle.draw()
        towerimage.draw()
        for tower in towerset:
            tower.draw()

    if gamepause is True:
        ingamepause.draw()
    update_canvas()



    pass

