import random
import json
import os
from pico2d import *

import game_framework
import subtitle

from anemy import Anemy
global worldmap
worldmap =400
name = "MainState"
map = None
anemy = None


class Map:
    def __init__(self):
        self.image = load_image('MAP.jpg')

    def draw(self):
        self.image.draw(worldmap, worldmap)


def enter():
    global map, anemy
    map = Map()
    anemy = Anemy()
    pass


def exit():
    pass

def collide(a, b):

    pass

def handle_events(frame_time):

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        else:
         anemy.handle_event(event)

def update(frame_time):
    anemy.update(frame_time)


    pass


def draw(frame_time):
     clear_canvas()
     map.draw()
     anemy.draw()

     update_canvas()
