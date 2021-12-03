import game_framework
import pico2d
import start_state
import set_up
import os

os.chdir('d:/2DGP/Project/Sprite')


pico2d.open_canvas(800, 600)
game_framework.run(set_up)
pico2d.close_canvas()
