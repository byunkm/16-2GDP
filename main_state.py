import random
import json
import os
from pico2d import *
import game_framework
import subtitle
from anemy import Boss
from anemy import Anemy
from tower import Tower,Cannontower,Arrowweapon
global worldmap,count
count = 0

worldmap =400
name = "MainState"
map = None
anemy = None
boss = None
arrowtower = None
cannontower = None
arrowweapon = None



class Map:
    def __init__(self):
        self.image = load_image('Beach.png')

    def draw(self):
        self.image.draw(worldmap, worldmap)


def enter():
    global map, anemy, boss, arrowtower, cannontower, arrowweapon
    map = Map()
    anemy = [Anemy() for i in range (20)]
    boss = Boss()
    arrowtower = [Tower() for i in range(5)]
    cannontower = Cannontower()
    arrowweapon = [Arrowweapon() for i in range(5)]
    pass


def exit():
    pass

def collide (a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a< left_b  : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True



def handle_events(frame_time):
    global arrowtower, count
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type == SDL_MOUSEMOTION:
            if arrowtower[count].state == True:
                arrowtower[count].x, arrowtower[count].y = event.x, 800 - event.y
            pass

        if event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            if event.x<50 and 800-event.y<50:
                arrowtower[count].state = True

        if event.type == SDL_MOUSEBUTTONUP and event.button == SDL_BUTTON_LEFT:
            if arrowtower[count].state == True :
                arrowtower[count].state = False
                arrowtower[count].building = True
                arrowweapon[count].state = True
                arrowweapon[count].shot = True

                if arrowweapon[count].shot == True:
                   arrowweapon[count].x = arrowtower[count].x
                   arrowweapon[count].y = arrowtower[count].y
                count = (count+1)%5



def update(frame_time):
    global anemy, arrowweapon

    boss.update(frame_time)
    for an in anemy:
        an.update(frame_time)

    for an in anemy:
        for bn in arrowweapon:
            if collide(bn, an):
                anemy.remove(an)
                bn.x = 300

    for bn in arrowweapon:
        bn.update(frame_time)




    pass


def draw(frame_time):
     clear_canvas()
     map.draw()
     for an in anemy:
        an.draw()
        an.draw_bb()

     boss.draw()
     for i in range(5):
      arrowtower[i].draw()

     for bn in arrowweapon:
        bn.draw(frame_time)
        bn.draw_bb()
     cannontower.draw()

     update_canvas()
