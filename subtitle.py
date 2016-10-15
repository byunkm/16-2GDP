import game_framework
import main_state
import title_state

from pico2d import *


name = "SubState"
image = None
select = None
global x, y
x = 560
y = 360


class Select():
    global x, y

    def __init__(self):
        self.image = load_image('pointer.png')

    def draw(self):
        self.image.draw(x,y)




def enter():
    global image,select

    select = Select()
    image = load_image('new1.jpg')

    pass





def exit():

    global image

    pass


def handle_events():
    global x,y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.push_state(title_state)
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                if y <110:
                    game_framework.push_state(title_state)
                else:
                    game_framework.push_state(main_state)

            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
                y -= 130
                if y<90:
                    y += 390
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
                y += 130
                if y>400:
                    y -= 390




    pass


def draw():



    clear_canvas()

    image.draw(400,400)
    select.draw()
    update_canvas()
    pass







def update():
    pass


def pause():
    pass


def resume():
    pass