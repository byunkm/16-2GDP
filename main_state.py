import random
import json
import os
from pico2d import *
import game_framework
import subtitle
import game_over
import game_clear
from anemy import Boss, Anemy, Level2
from tower import Tower,Cannontower,Arrowweapon,Cannonweapon
name = "MainGameStage"
global worldmap, count, score, life, bosslife,cannoncount ,bgm
global scorefontx, scorefonty ,lifefontx, lifefonty, bosslifefontx, bosslifefonty
scorefontx = 450
scorefonty = 770
lifefontx = 650
lifefonty = 770
bosslifefontx=450
bosslifefonty=720
count = 0
cannoncount=0
score = 0
worldmap = 400
life = 20
bosslife = 150

start = False
map = None
anemy = None
level2 = None
boss = None
arrowtower = None
cannontower = None
arrowweapon = None
bgm=None

print(start)

class Map:
    def __init__(self):
        self.image = load_image('Beach.png')

    def draw(self):
        self.image.draw(worldmap, worldmap)

    def get_bb(self):
        return 50, 150, 260, 750

    def draw_bb(self):
        draw_rectangle(*self.get_bb())





def enter():
    global bgm,map, anemy, boss, arrowtower, cannontower, arrowweapon, cannonweapon,level2
    map = Map()
    anemy = [Anemy() for i in range (20)]
    level2 = [Level2() for i in range (40)]

    boss = Boss()
    arrowtower = [Tower() for i in range(5)]
    cannontower = Cannontower()
    arrowweapon = [Arrowweapon() for i in range(5)]
    cannonweapon = Cannonweapon()
    ##bgm = load_music('BGM.wav')
    ##bgm.set_volume(64)
    ##bgm.repeat_play()


def exit():
    pass

def collide (a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a< left_b  : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True



def handle_events(frame_time):
    global arrowtower, count, start
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()

        if event.type == SDL_MOUSEMOTION:
            if arrowtower[count].state == True:
                arrowtower[count].x, arrowtower[count].y = event.x, 800 - event.y
            if cannontower.state == True:
                cannontower.x, cannontower.y = event.x, 800-event.y
            pass

        elif event.type == SDL_KEYDOWN and event.key == SDLK_F1:
            if start == False:
             start = True


        if event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            if event.x<50 and 800-event.y<50:
                arrowtower[count].state = True
            if 200>event.x>100 and 800-event.y<50:
                #if life>=10 and score>=60:
                    cannontower.state = True

        if event.type == SDL_MOUSEBUTTONUP and event.button == SDL_BUTTON_LEFT:
            if arrowtower[count].state == True and clamp(250,event.x,300) and 800-event.y>550:
                #clamp(0, self.x, 1650)
                arrowtower[count].x, arrowtower[count].y = 280,580
                arrowtower[count].state = False
                arrowtower[count].building = True
                arrowweapon[count].state = True
                arrowweapon[count].shot = True

                if arrowweapon[count].shot == True:
                   arrowweapon[count].x = arrowtower[count].x
                   arrowweapon[count].y = arrowtower[count].y
                count = (count+1)%5

            if arrowtower[count].state == True and clamp(250,event.x,300) and 550 > 800 - event.y > 450:
                arrowtower[count].x, arrowtower[count].y = 280, 490
                arrowtower[count].state = False
                arrowtower[count].building = True
                arrowweapon[count].state = True
                arrowweapon[count].shot = True

                if arrowweapon[count].shot == True:
                    arrowweapon[count].x = arrowtower[count].x
                    arrowweapon[count].y = arrowtower[count].y
                count = (count + 1) % 5

            if arrowtower[count].state == True and clamp(250,event.x,300) and 450>800 - event.y > 350:
                arrowtower[count].x, arrowtower[count].y = 280, 400
                arrowtower[count].state = False
                arrowtower[count].building = True
                arrowweapon[count].state = True
                arrowweapon[count].shot = True

                if arrowweapon[count].shot == True:
                    arrowweapon[count].x = arrowtower[count].x
                    arrowweapon[count].y = arrowtower[count].y
                count = (count + 1) % 5

            if cannontower.state == True and clamp(250,event.x,300) and 450>800 - event.y > 350:
                cannontower.x, cannontower.y = 210, 400
                cannontower.state = False
                cannontower.building = True
                cannonweapon.state = True
                cannonweapon.shot = True

                if cannonweapon.shot == True:
                    cannonweapon.x = cannontower.x
                    cannonweapon.y = cannontower.y



            if arrowtower[count].state == True and clamp(250,event.x,300) and 350 > 800 - event.y > 250:
                arrowtower[count].x, arrowtower[count].y = 280, 310
                arrowtower[count].state = False
                arrowtower[count].building = True
                arrowweapon[count].state = True
                arrowweapon[count].shot = True

                if arrowweapon[count].shot == True:
                    arrowweapon[count].x = arrowtower[count].x
                    arrowweapon[count].y = arrowtower[count].y
                count = (count + 1) % 5

            if arrowtower[count].state == True and clamp(250,event.x,300) and 250 > 800 - event.y > 150:
                arrowtower[count].x, arrowtower[count].y = 280, 220
                arrowtower[count].state = False
                arrowtower[count].building = True
                arrowweapon[count].state = True
                arrowweapon[count].shot = True

                if arrowweapon[count].shot == True:
                    arrowweapon[count].x = arrowtower[count].x
                    arrowweapon[count].y = arrowtower[count].y
                count = (count + 1) % 5


def update(frame_time):
    global anemy, arrowweapon, score, level2, life, bosslife

    boss.update(frame_time)
    for level1 in anemy:
        level1.update(frame_time)
    for level1 in anemy:
        for arrow in arrowweapon:
            if collide(arrow, level1):
                anemy.remove(level1)
                arrow.x = 300
                score = score + 1
                print(score)
        if collide(map, level1):
            anemy.remove(level1)
            life = life -1
            print(life)

    for leveltwo in level2:
        leveltwo.update(frame_time)
    for leveltwo in level2:
        for arrow in arrowweapon:
            if collide(arrow, leveltwo):
                level2.remove(leveltwo)
                arrow.x = 300
                score = score + 1
                print(score)

    for arrow in arrowweapon:
        arrow.update(frame_time)

        if arrow.x >= 800:
            arrow.x = 300
        if collide(arrow, boss):
            arrow.x = 300
            bosslife -= 1
    if cannonweapon.x >=800:
        cannonweapon.x = 250
    if collide(cannonweapon, boss):
            cannonweapon.x = 250
            bosslife -= 2




    cannonweapon.update(frame_time)

    if life == 0:
        game_framework.push_state(game_over)
    if bosslife <=0:
        game_framework.push_state(game_clear)

    pass
def pause():
    pass


def draw(frame_time):
     clear_canvas()
     map.draw()
     for level1 in anemy:
         level1.draw()
     for leveltwo in level2:
         leveltwo.draw()

     boss.draw()
     boss.draw_bb()
     for i in range(5):
      arrowtower[i].draw()

     for arrow in arrowweapon:
         arrow.draw(frame_time)

     cannontower.draw()
     cannonweapon.draw(frame_time)

     font = load_font('ENCR10B.TTF',30)
     font.draw(lifefontx, lifefonty,'Life:%d'%life)
     font.draw(scorefontx, scorefonty,'Score:%d'%score)
     if score==60:
         font.draw(bosslifefontx,bosslifefonty,'BossLife :%d'%bosslife)

     update_canvas()
