import game_framework
import start_state
import main_state
import test

import platform
import os

from pico2d import *


##if platform.architecture()[0] == '32bit':
##    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x86"
##else:
##    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x64"
open_canvas(800,800)
game_framework.run(main_state)
close_canvas()