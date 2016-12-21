import random
from pico2d import*

import main_state
global level1speed,level2speed,bossspeed
global level2start, bossstart
level1speed = 0.5
level2speed = 0.6

level2start = 20
bossstart = 60

class Anemy:
    PIXEL_PER_METER = (20.0 / 0.6)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 3

    image = None
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 3

    image = None

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND = 0, 1, 2, 3

    def __init__(self):
        self.x, self.y = random.randint(1000,1650),random.randint(220,600)
        self.frame = random.randint(0, 2)
        self.life_time = 0.0
        self.total_frames = random.randint(0,2)
        self.dir = 0
        self.state = self.LEFT_STAND
        if Anemy.image == None:
            Anemy.image = load_image('moster.png')

    def update(self, frame_time):
        def clamp(minimum, x, maximum):
            return max(minimum, min(x, maximum))

        self.life_time += frame_time
        distance = Anemy.RUN_SPEED_PPS * frame_time
        self.total_frames += Anemy.FRAMES_PER_ACTION * Anemy.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 3
        if main_state.start == True:
         self.x += -level1speed* distance
        self.x = clamp(0, self.x, 1650)


    def draw(self):
        self.image.clip_draw(self.frame * 100, 0 , 100, 100, self.x, self.y)

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x+50, self.y + 50

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Level2:
    PIXEL_PER_METER = (20.0 / 0.6)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 3

    image = None
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 3

    image = None

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND = 0, 1, 2, 3

    def __init__(self):
        self.x, self.y = random.randint(1000,1650),random.randint(220,600)
        self.frame = random.randint(0, 2)
        self.life_time = 0.0
        self.total_frames = random.randint(0,2)
        self.dir = 0
        self.state = self.LEFT_STAND
        if Level2.image == None:
            Level2.image = load_image('Enemy1_sheet.png')

    def update(self, frame_time):
        def clamp(minimum, x, maximum):
            return max(minimum, min(x, maximum))

        self.life_time += frame_time
        distance = Level2.RUN_SPEED_PPS * frame_time
        self.total_frames += Level2.FRAMES_PER_ACTION * Level2.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 3
        if main_state.score >= level2start:
         self.x += -level1speed* distance
        self.x = clamp(0, self.x, 1650)


    def draw(self):
        self.image.clip_draw(self.frame * 100, 200 , 100, 100, self.x, self.y)

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x+50, self.y + 50

    def draw_bb(self):

        draw_rectangle(*self.get_bb())


class Boss:
    PIXEL_PER_METER = (20.0 / 0.6)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8
    image = None
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    image = None

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND = 0, 1, 2, 3

    def __init__(self):
        self.x, self.y = 1000, 400
        self.frame = random.randint(0, 7)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 0
        self.state = self.LEFT_RUN
        if Boss.image == None:
            Boss.image = load_image('animation_sheet.png')

    def update(self, frame_time):
        def clamp(minimum, x, maximum):
            return max(minimum, min(x, maximum))

        self.life_time += frame_time
        distance = Anemy.RUN_SPEED_PPS * frame_time
        self.total_frames += Anemy.FRAMES_PER_ACTION * Anemy.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 8
        if main_state.score >= bossstart:
         self.x += -0.1 * distance
        self.x = clamp(0, self.x, 1000)

    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def draw_bb(self):
        draw_rectangle(*self.get_bb())




