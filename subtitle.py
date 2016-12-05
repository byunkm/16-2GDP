import game_framework
import title_state
import main_state
from pico2d import *

name = "difficultly Select"
image = None
select = None
global selectpointx, selectpointy, move, easymode

selectpointx = 225
selectpointy = 550
move = 170
easymode = 230

class Select():
    def __init__(self):
        self.image = load_image('pointer.png')

    def draw(self):
        self.image.draw(selectpointx, selectpointy)


def enter():
    global image, select
    select = Select()
    image = load_image('easy.jpg')

    pass


def exit():
    global image
    pass


def handle_events(frame_time):
    events = get_events()
    global selectpointx
    #왜 너만지우면 오류가 생길까?

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.push_state(title_state)

            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                if selectpointx < easymode:
                    game_framework.push_state(main_state)

            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
                selectpointx += move
                if selectpointx > 550:
                    selectpointx = 225

            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
                selectpointx -= move
                if selectpointx < 225:
                    selectpointx = 395


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

