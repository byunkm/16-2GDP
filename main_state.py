import random
import json
import os
from pico2d import *

import game_framework
import subtitle

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
        self.image = load_image('castle.png')

    def draw(self):
        self.image.draw(400, 400)


class Towerui:
    def __init__(self):
        self.image = load_image('towerui.png')

    def draw(self):
        self.image.draw(120,100)


class Towerimage:
    def __init__(self):
        self.image = load_image('tower.png')

    def draw(self):
        self.image.draw(60,100)


class Ingamepause:
    def __init__(self):
        self.image = load_image('igp.png')

    def draw(self):
        self.image.draw(400, 400)


class Gameexit:
    def __init__(self):
        self.image = load_image('gameexit.png')

    def draw(self):
        self.image.draw(400,400)


class Tower:
#클래스 변수선언
    image = None
    global x, y, z
    x = 0
    y = 0
    z = 0

#def 클래스함수(매서드) 생성
#init 은 생성자
    def __init__(self):
        self.state = False
        self.count = 0
        self.x, self.y = 60,100
        if Tower.image == None:
             Tower.image = load_image('tower.png')

    def draw(self):
        if self.state == True:
             self.image.draw(self.x, self.y)


class Enemy:
    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.state = 0
        self.image = load_image('red.png')
        self.dir = 0.25

    def update(self):
        self.frame = (self.frame + 1) % 4
        self.y += self.dir

        if self.y <= 0:
            self.dir = 50

        if self.y >= 400:
            self.dir = -10

    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)


class Pause:
    def __init__(self):
        self.image = load_image('pause.jpg')

    def draw(self):
        self.image.draw(770, 770)


class Back:
    def __init__(self):
        self.image = load_image('back.png')

    def draw(self):
        self.image.draw(730, 770)


def enter():
    global enemy, castle, pause, back, tower, towerui, towerimage, towerset, ingamepause, gameexit

    enemy = Enemy()
    castle = Castle()
    towerset = [Tower() for i in range(15)]
    towerimage = Towerimage()
    towerui = Towerui()
    pause = Pause()
    ingamepause = Ingamepause()
    gameexit = Gameexit()
    back = Back()

    pass

#def exit():
   # pass


def handle_events():
    global x, y, z, castle, towerset, count, gamepause, gameexitstate
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        if event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:

            if 710 < event.x < 750:
                if 800 - event.y > 750:

                    if gamepause is False:
                        gameexitstate = True

            if 220 < event.x < 300:
                if 330 < 800-event.y < 380:
                    if gameexitstate is True:
                        game_framework.change_state(subtitle)
                        gameexitstate = False

            if 510 < event.x < 570:
                if 330 < 800-event.y < 380:
                    gameexitstate = False

            if 750 < event.x < 800:
                if 800 - event.y > 750:
                    gamepause = True
                    if gameexitstate is True:
                        gamepause = False

            if 50 < event.x < 115:
                if 70 < 800-event.y < 130:
                    towerset[count].state = True

        if event.type == SDL_MOUSEMOTION:

                towerset[count].x, towerset[count].y = event.x, 800 - event.y

        if event.type == SDL_MOUSEBUTTONUP and event.button == SDL_BUTTON_LEFT:
            if towerset[count].state:
                if 800-event.y < 300 or 800-event.y > 600:
                    towerset[count].state = False
                    towerset[count].x, towerset[count].y = 60, 100

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

    if gamepause is False:
        enemy.update()

    pass


def draw():
    if gamepause is False:
        clear_canvas()
        #객체를 통한 함수호출
        castle.draw()
        enemy.draw()
        towerui.draw()
        towerimage.draw()
        for tower in towerset:
            tower.draw()
        pause.draw()
        back.draw()
        if gameexitstate is True:
            gameexit.draw()
    if gamepause is True:
        ingamepause.draw()
    update_canvas()



    pass

