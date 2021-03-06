import random
import json
import os

from pico2d import *
import game_framework
import game_world
import server

import Stage_1_map_7
import Stage_1_map_10
import Stage_1_map_15

from Item import *
import make_map
import destroy_map
from Obstacle import *

PIXEL_PER_METER = (1.0 / 0.033) # 1px = 3.3 cm
RUN_SPEED_MPS = 50.0 / 10.8     # 50m per 10.8 sec
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

name = "Stage_1_map_11"

def enter():
    server.obstacle_rocks = [Obstacle_Rock(52 + 45 * i, 52 + 45 * j) for i in range(0, 7) for j in range(0, 5)] \
                            + [Obstacle_Rock(480 + 45 * i, 52 + 45 * j) for i in range(0, 7) for j in range(0, 5)] \
                            + [Obstacle_Rock(52 + 45 * i, 366 + 45 * j) for i in range(0, 7) for j in range(0, 5)] \
                            + [Obstacle_Rock(480 + 45 * i, 366 + 45 * j) for i in range(0, 7) for j in range(0, 5)] \
                            + [Obstacle_Sting(800 // 2, 600 * 3 // 4, 2), Obstacle_Sting(800 // 2, 600 // 4, 2),
                               Obstacle_Sting(800 // 4, 600 // 2, 2), \
                               Obstacle_Sting(800 * 3 // 4, 600 // 2, 2), Obstacle_Sting(800 // 2, 600 // 2, 0)]
    game_world.add_objects(server.obstacle_rocks, server.Obs_num)
    make_map.make_Map('d:/2DGP/Project/Stage/stage_1/stage_11.txt')


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
        server.Floor_1[11] = True
    if server.isaac_head.nowPos == 7:
        game_framework.change_state(Stage_1_map_7)
    if server.isaac_head.nowPos == 10:
        game_framework.change_state(Stage_1_map_10)
    if server.isaac_head.nowPos == 15:
        game_framework.change_state(Stage_1_map_15)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
