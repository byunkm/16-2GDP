import game_framework
import title_state
import main_state
from pico2d import *

name = "SubState"
image = None
select = None
global x, y


class Select():
    global x, y
    x = 225
    y = 550
    def __init__(self):
        self.image = load_image('pointer.png')

    def draw(self):
        self.image.draw(x,y)


def enter():
    global image,select

    select = Select()
    image = load_image('easy.jpg')

    pass





def exit():

    global image

    pass


def handle_events(frame_time):
    global x,y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.push_state(title_state)

            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                if x < 230:
                    game_framework.push_state(main_state)

            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
                x += 170
                if x > 550:
                    x=225


            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
                x -= 170
                if x < 225:
                    x=395
                pass

    pass


def draw(frame_time):

    clear_canvas()

    image.draw(400, 400)
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

