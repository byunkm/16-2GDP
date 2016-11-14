import game_framework
import title_state

from pico2d import *

import game_framework
import subtitle

name = "MainState"
Map=None
Arrowtower = None


class Map:

    def __init__(self):
        self.image = load_image('easymap.png')

    def draw(self):
        self.image.draw(400, 400)

class Arrowtower:

    def __init__(self):
        self.image = load_image('tower.png')

    def draw(self):
        self.image.draw(55,60)

def enter():
    global map,arrowtower
    map = Map()
    arrowtower =Arrowtower()
    pass


def exit():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        if event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:

            pass
        if event.type == SDL_MOUSEMOTION:

           pass

        if event.type == SDL_MOUSEBUTTONUP and event.button == SDL_BUTTON_LEFT:
           pass

        if event.type == SDL_KEYDOWN and event.key == SDLK_F10:
           pass

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
           pass

def update():



    pass


def draw():
    clear_canvas()
    map.draw()
    arrowtower.draw()
    update_canvas()



    pass

