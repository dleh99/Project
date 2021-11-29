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
from Door import *
from Tile import *

PIXEL_PER_METER = (1.0 / 0.033) # 1px = 3.3 cm
RUN_SPEED_MPS = 50.0 / 10.8     # 50m per 10.8 sec
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

import Stage_1_map_1

name = "MainState"

os.chdir('d:/2DGP/Project/Sprite')

def enter():
    server.isaac_head = Isaac_head()
    server.isaac_body = Isaac_body()
    server.red_spiders = [Red_Spider() for i in range(3)]
    server.obstacle_rocks = Obstacle_Rock()
    game_world.add_object(server.isaac_body, 1)
    game_world.add_object(server.isaac_head, 1)
    game_world.add_objects(server.red_spiders, 3)
    game_world.add_object(server.obstacle_rocks, 4)
    make_Map()


def make_Map():
    f = open('d:/2DGP/Project/Stage/stage_1.txt')
    for i in range(7):
        server.tile.append(f.readline())
    f.close()

    for line in range(6):
        for n in range(8):
            if server.tile[line][n] == '1':
                game_world.add_object(Tile_1(line, n), 0)
            elif server.tile[line][n] == '2':
                game_world.add_object(Tile_2(line, n), 0)
            elif server.tile[line][n] == '3':
                game_world.add_object(Tile_3(line, n), 0)
            elif server.tile[line][n] == '4':
                game_world.add_object(Tile_4(line, n), 0)
            elif server.tile[line][n] == '5':
                game_world.add_object(Tile_5(line, n), 0)
            elif server.tile[line][n] == '6':
                game_world.add_object(Tile_6(line, n), 0)
            elif server.tile[line][n] == '7':
                game_world.add_object(Tile_7(line, n), 0)
            elif server.tile[line][n] == '8':
                game_world.add_object(Tile_8(line, n), 0)
            else:
                game_world.add_object(Tile_9(line, n), 0)

    for i in range(len(server.tile[6])):
        if server.tile[6][i] == '1':
            server.doors.append(Door_Down(800 // 2, 18))
        elif server.tile[6][i] == '2':
            server.doors.append(Door_right(800 - 18, 600 // 2))
        elif server.tile[6][i] == '3':
            server.doors.append(Door_Up(800 // 2, 600 - 18))
        elif server.tile[6][i] == '4':
            server.doors.append(Door_left(18, 600 // 2))
    game_world.add_objects(server.doors, 5)


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
    # for door in game_world.Door_objects():
    #     for isaac in game_world.Isaac_objects():
    #         if left_collide(isaac, door):
    #             for all in game_world.Isaac_objects():
    #                 all.x = 30 + 23
    #             game_framework.change_state(Stage_1_map_1)
    # delay(1.0)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






