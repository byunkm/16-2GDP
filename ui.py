import random

from pico2d import *


class Uiarrowtower:

    def __init__(self):
        self.image = load_image('tower.png')

    def draw(self):
        self.image.draw(45,65)
