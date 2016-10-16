import random
import json
import os
from pico2d import *

import game_framework
import title_state
import subtitle

name = "MainState"

global x, y, z
enemy = None
grass = None
pause = None
back = None
font = None
tower = None
towerui = None
towerset = None
towerimage = None


class Grass:

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


class Tower:
    global x, y, z
    x = 0
    y = 0
    z = 0

    def __init__(self):
        self.x, self.y = 60, 100
        self.image = load_image('tower.png')

    def update(self):
        self.x = x
        self.y = y

    def draw(self):
        self.image.draw(self.x, self.y)


class Enemy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('run_animation.png')
        self.dir = 1

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        if self.x >= 800:
            self.dir = -1
        elif self.x <= 0:
            self.dir = 1

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


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
    global enemy, grass, pause, back, tower, towerui, towerimage

    enemy = Enemy()
    grass = Grass()
    tower = Tower()
    towerimage = Towerimage()
    towerui = Towerui()
    pause = Pause()
    back = Back()
    pass


def exit():
    global enemy, grass, pause, back, tower,towerui, towerimage

    enemy = Enemy()
    grass = Grass()
    tower = Tower()
    towerimage = Towerimage()
    towerui = Towerui()
    pause = Pause()
    back = Back()

    del enemy
    del grass
    del pause
    del back
    del tower
    del towerui
    del towerimage


def pause():
    global x, y
    x = 400
    y = 400
    pause.draw()

    pass


def resume():
    pass


def handle_events():
    global x, y, z

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        if event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:

            if 710 < event.x < 750:
                if 800 - event.y > 750:
                    game_framework.change_state(subtitle)
                    event.x,event.y == x,y

            if 750 < event.x < 800:
                if 800 - event.y > 750:
                    pause.draw()

            if 50 < event.x < 115:
                if 70 < 800-event.y < 130:
                     z += 1

        if event.type == SDL_MOUSEBUTTONUP and event.button == SDL_BUTTON_LEFT:

            if z >= 1:
                x, y = event.x, 800 - event.y
                tower.draw()
                z -= 1

        if event.type == SDL_MOUSEMOTION:
            if z >= 1:
                x, y = event.x, 800 - event.y
                tower.draw()
            if z < 1:
                x, y != event.x, 800 - event.y

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(subtitle)


def update():
    tower.update()
    enemy.update()

    pass


def draw():
    clear_canvas()
    grass.draw()
    enemy.draw()
    towerui.draw()
    towerimage.draw()
    tower.draw()
    pause.draw()
    back.draw()
    update_canvas()

    pass

