import game_framework
import pico2d
import start_state
import Stage_1_map_0
import os

os.chdir('d:/2DGP/Project/Sprite')


pico2d.open_canvas(800, 600)
game_framework.run(Stage_1_map_0)
pico2d.close_canvas()
