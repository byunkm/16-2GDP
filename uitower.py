import random
import main_state
from pico2d import *
import main_state


class Towerimage:
    def __init__(self):
        self.image = load_image('tower.png')

    def draw(self):
        self.image.draw(45 ,65)