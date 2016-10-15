import random
import json
import os

from pico2d import *

import game_framework
import title_state
import subtitle

name = "MainState"
global x,y
enemy = None
grass = None
pause = None
back = None
font = None
tower = None
towerui = None


class Grass:
    global x,y

    def __init__(self):
        self.image = load_image('castle.png')

    def draw(self):
        self.image.draw(400, 400)


class Towerui:
    def __init__(self):
        self.image = load_image('towerui.png')

    def draw(self):
        self.image.draw(120,100)


class Tower:
    global x, y
    x=60
    y=100
    def __init__(self):
        self.image = load_image('tower.png')

    def draw(self):
        self.image.draw(x, y)

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


def enter():
    global enemy, grass, pause, back, tower, towerui


    enemy = Enemy()
    grass = Grass()
    tower = Tower()
    towerui = Towerui()
    pause = Pause()
    back = Back()
    pass


def exit():
    global enemy , grass, pause, back
    del(enemy)
    del(grass)
    del(pause)
    del(back)
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    global x, y
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        if event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            if event.x>710 and event.x<750:
                if 800 - event.y >750:
                  game_framework.change_state(subtitle)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(subtitle)

    pass


def update():
    enemy.update()
    pass


def draw():
    clear_canvas()
    grass.draw()
    towerui.draw()
    tower.draw()
    pause.draw()
    back.draw()
    update_canvas()
    pass





