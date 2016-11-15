import random
import json
import os
from pico2d import *

import game_framework
import subtitle
from tower import Tower
from tower import Magictower
from uitower import Towerimage
from uitower import Magictowerimage



name = "MainState"
global x, y, z, count, gamepause

gamepause = False

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
magictowers = None
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
    global enemy, castle, back, tower, towerimage, magictowers, towerset, ingamepause, magictowerimage
    enemy = Enemy()
    castle = Castle()
    towerimage = Towerimage()
    magictowerimage = Magictowerimage()
    ingamepause = Ingamepause()
    towerset = [Tower() for i in range(10)]
    magictowers = [Magictower() for i in range(10)]
    towerset = towerset + magictowers

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

            if 690 < event.x < 730:
                if 770 > 800 - event.y > 730:
                    gamepause = True

            if 25 < event.x < 65:
                if 45 < 800 - event.y < 85:
                    towerset[count].state = True
                    magictowers[count].state =  False
            if 75<event.x<115:
                if 45 < 800 - event.y < 85:
                    magictowers[count].state = True

        if event.type == SDL_MOUSEMOTION:
            towerset[count].x, towerset[count].y = event.x, 800 - event.y
            magictowers[count].x,magictowers[count].y = event.x, 800 - event.y

        if event.type == SDL_MOUSEBUTTONUP and event.button == SDL_BUTTON_LEFT:
            if towerset[count].state:
                if 100 < event.x < 150 and 390 > 800-event.y > 340:
                    towerset[count].x, towerset[count].y = 140 , 360
                    count = (count + 1) % 10
                    towerset[count].state = False
                if 170 < event.x < 240 and 320 > 800 - event.y > 290:
                    towerset[count].x, towerset[count].y = 220, 300
                    count = (count + 1) % 10
                    towerset[count].state = False
                if 210 < event.x < 260 and  460 < 800 - event.y< 490:
                    towerset[count].x, towerset[count].y = 250,470
                    count = (count + 1) % 10
                    towerset[count].state = False
                if 300 < event.x < 350 and 360 < 800 - event.y < 390 :
                    towerset[count].x, towerset[count].y = 340, 370
                    count = (count + 1) % 10
                    towerset[count].state = False
                if 430 < event.x < 480 and 360 < 800 - event.y < 390 :
                    towerset[count].x, towerset[count].y = 470, 370
                    count = (count + 1) % 10
                    towerset[count].state = False
                if  450 < event.x < 500 and 210 < 800 - event.y <240 :
                    towerset[count].x, towerset[count].y = 490, 220
                    count = (count + 1) % 10
                    towerset[count].state = False
                if  570 < event.x < 620 and 300 < 800 - event.y <330 :
                    towerset[count].x, towerset[count].y = 610 ,310
                    count = (count + 1) %10
                    towerset[count].state = False
                if  630 < event.x < 680 and 570 < 800 - event.y <600 :
                    towerset[count].x, towerset[count].y = 670, 580
                    count = (count + 1) % 10
                    towerset[count].state = False
                if 630 < event.x < 680 and 230 < 800 - event.y < 260 :
                    towerset[count].x, towerset[count].y = 670, 240
                    count = (count + 1) % 10
                    towerset[count].state = False
            if magictowers[count].state:
                if 100 < event.x < 150 and 390 > 800 - event.y > 340:
                    magictowers[count].x, magictowers[count].y = 140, 360
                    count = (count + 1) % 10
                    magictowers[count].state = False
                if 170 < event.x < 240 and 320 > 800 - event.y > 290:
                    magictowers[count].x, magictowers[count].y = 220, 300
                    count = (count + 1) % 10
                    magictowers[count].state = False
                if 210 < event.x < 260 and 460 < 800 - event.y < 490:
                    magictowers[count].x, magictowers[count].y = 250, 470
                    count = (count + 1) % 10
                    magictowers[count].state = False
                if 300 < event.x < 350 and 360 < 800 - event.y < 390:
                    magictowers[count].x, magictowers[count].y = 340, 370
                    count = (count + 1) % 10
                    magictowers[count].state = False
                if 430 < event.x < 480 and 360 < 800 - event.y < 390:
                    magictowers[count].x, magictowers[count].y = 470, 370
                    count = (count + 1) % 10
                    magictowers[count].state = False
                if 450 < event.x < 500 and 210 < 800 - event.y < 240:
                    magictowers[count].x, magictowers[count].y = 490, 220
                    count = (count + 1) % 10
                    magictowers[count].state = False
                if 570 < event.x < 620 and 300 < 800 - event.y < 330:
                    magictowers[count].x, magictowers[count].y = 610, 310
                    count = (count + 1) % 10
                    magictowers[count].state = False
                if 630 < event.x < 680 and 570 < 800 - event.y < 600:
                    magictowers[count].x, magictowers[count].y = 670, 580
                    count = (count + 1) % 10
                    magictowers[count].state = False
                if 630 < event.x < 680 and 230 < 800 - event.y < 260:
                    magictowers[count].x, magictowers[count].y = 670, 240
                    count = (count + 1) % 10
                    magictowers[count].state = False
    
    

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
        # 객체를 통한 함수호출
        castle.draw()
        towerimage.draw()
        magictowerimage.draw()
        for tower in towerset:
            tower.draw()
        for magictower in magictowers:
            magictower.draw()


    if gamepause is True:
        ingamepause.draw()
    update_canvas()
