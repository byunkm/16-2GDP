import game_framework

from pico2d import*

class Boundingbox:
    def __init__(self):
        self.x, self.y = 670, 580

    def get_bb(self):
        return self.x - 60, self.y - 60, self.x + 60, self.y + 60

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
