import game_framework
import main_state
import subtitle
from pico2d import *


name = "TitleState"
image = None
select = None
global x, y
x = 600
y = 280


class Select():
    global x, y

    def __init__(self):
        self.image = load_image('pointer.png')

    def draw(self):
        self.image.draw(x,y)




def enter():
    global image,select

    select = Select()
    image = load_image('maindragon1.jpg')

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
                game_framework.quit()
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                if y <140:
                    game_framework.quit()
                else:
                    game_framework.push_state(subtitle)

            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
                y -= 150
                if y<120:
                    y += 300
                pass
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
                y += 150
                if y>300:
                    y -= 300
                pass



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






