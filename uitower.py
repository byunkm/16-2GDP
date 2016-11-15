import random
import main_state
from pico2d import *
import main_state


class Towerimage:
    def __init__(self):
        self.image = load_image('tower.png')

    def draw(self):
        self.image.draw(45 ,65)


class Magictowerimage:
    def __init__(self):
        self.image = load_image('magictower.png')

    def draw(self):
        self.image.draw(100, 65)


class Cannontowerimage:
    def __init__(self):
        self.image = load_image('cannontower.png')

    def draw(self):
        self.image.draw(160, 70)