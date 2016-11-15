import game_framework
import subtitle
from pico2d import *


name = "TitleState"
image = None
select = None
global x, y
x = 250
y = 220

class Select():
    global x, y

    def __init__(self):
        self.image = load_image('point.png')

    def draw(self):
        self.image.draw(x,y)




def enter():
    global image,select

    select = Select()
    image = load_image('title.png')

    pass






def handle_events(frame_time):
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                if y < 140:
                    game_framework.quit()
                else:
                    game_framework.push_state(subtitle)


    pass


def draw(frame_time):

    clear_canvas()
    image.draw(400,400)
    select.draw()
    update_canvas()
    pass


def update(frame_time):
    pass


def pause():
    pass


def resume():
    pass


def exit():

    pass




