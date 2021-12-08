import random
import json
import os

from pico2d import *
import game_framework
import game_world
import server

from Obstacle import *
import make_map
import destroy_map
import Stage_2_map_10
import Stage_2_map_22

PIXEL_PER_METER = (1.0 / 0.033) # 1px = 3.3 cm
RUN_SPEED_MPS = 50.0 / 10.8     # 50m per 10.8 sec
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

name = "Stage_2_map_16"

def enter():
    make_map.make_Map('d:/2DGP/Project/Stage/stage_2/stage_16.txt')


def exit():
    destroy_map.destroy()


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            server.isaac_head.handle_event(event)
            server.isaac_body.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()
    if len(game_world.objects[server.Mob_num]) == 0:
        server.Floor_2[16] = True
    if server.isaac_head.nowPos == 10:
        game_framework.change_state(Stage_2_map_10)
    if server.isaac_head.nowPos == 22:
        game_framework.change_state(Stage_2_map_22)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()