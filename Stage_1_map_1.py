import random
import json
import os

from pico2d import *
import game_framework
import game_world
import server

from Isaac_Head import Isaac_head
from Isaac_Body import Isaac_body
from Enemy_spider import *
from Obstacle import Obstacle_Rock
import make_map

PIXEL_PER_METER = (1.0 / 0.033) # 1px = 3.3 cm
RUN_SPEED_MPS = 50.0 / 10.8     # 50m per 10.8 sec
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

name = "Stage_1_map_2"

def enter():
    if not server.Floor_1[1]:
        server.red_spiders = [Red_Spider() for i in range(3)]
        game_world.add_objects(server.red_spiders, 3)
    server.obstacle_rocks = Obstacle_Rock()
    server.isaac_head = Isaac_head()
    server.isaac_body = Isaac_body()
    game_world.add_object(server.isaac_body, 1)
    game_world.add_object(server.isaac_head, 1)
    game_world.add_object(server.obstacle_rocks, 4)
    make_map.make_Map('d:/2DGP/Project/Stage/stage_1.txt')


def exit():
    for door in server.doors:
        game_world.remove_object(door)
    game_world.remove_object(server.obstacle_rocks)


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
    if len(game_world.objects[3]) == 0:
        server.Floor_1[1] = True
    print(server.isaac_head.nowPos)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






