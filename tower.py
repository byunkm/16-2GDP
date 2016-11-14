import random
import main_state
from pico2d import *
import subtitle
import game_framework


class Tower:
    image = None
    global x, y, z
    x = 0
    y = 0
    z = 0

    def __init__(self):
        self.state = False
        self.count = 0
        self.x, self.y = 30,50
        if Tower.image == None:
             Tower.image = load_image('tower.png')

    def draw(self):
        if self.state == True:
             self.image.draw(self.x, self.y)
