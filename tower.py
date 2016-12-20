import random
from pico2d import *
import main_state
import subtitle
import game_framework

class Tower:
    image = None
    def __init__(self):
        self.state = False
        self.count = 0
        self.x, self.y = 50,50
        self.state = False
        self.building = False
        if Tower.image == None:
             Tower.image = load_image('magictower.png')

    def draw(self):

         self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 25, self.y - 50, self.x + 25, self.y + 50

    def draw_bb(self):
         draw_rectangle(*self.get_bb())


class Arrowweapon:

    image = None
    def __init__(self):
        self.state = False
        self.shot = False
        self.count = 0
        self.x, self.y = 50, 50

        self.state = False
        if Arrowweapon.image == None:
            Arrowweapon.image = load_image('arrow.png')

    def draw(self,frame_time):
        if self.state == True:
            self.image.draw(self.x, self.y)

    def update(self, frame_time):
        if self.shot == True:
         self.x += self.x * frame_time



    def get_bb(self):
        return self.x -50,self.y - 50, self.x +50, self.y+50

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    ##def get_bb(self):
    ##    return self.x - 25, self.y - 50, self.x + 25, self.y + 50

    ##def draw_bb(self):
    ##    draw_rectangle(*self.get_bb())


class Magictower:
    image = None
    def __init__(self):
        self.state = False
        self.count = 0
        self.x, self.y = 0,0
        if Magictower.image == None:
             Magictower.image = load_image('magictower.png')

    def draw(self):
        if self.state == True:
             self.image.draw(self.x, self.y)


    def get_bb(self):
        return self.x - 25, self.y - 50, self.x + 25, self.y + 50


    def draw_bb(self):
        if self.state == True:
             draw_rectangle(*self.get_bb())
class Cannontower:
    image = None

    def __init__(self):
        self.state = False
        self.count = 0
        self.x, self.y = 130,50
        if Cannontower.image == None:
            Cannontower.image = load_image('cannontower.png')

    def draw(self):
         self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 25, self.y - 50, self.x + 25, self.y + 50

    def draw_bb(self):
        if self.state == True:
            draw_rectangle(*self.get_bb())