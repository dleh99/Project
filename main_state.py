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
from Door_side import Door_lr
from Door_UD import Door_ud

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
    # print(type(red_spiders))
    server.obstacle_rocks = Obstacle_Rock()
    game_world.add_object(server.isaac_body, 1)
    game_world.add_object(server.isaac_head, 1)
    game_world.add_objects(server.red_spiders, 3)
    game_world.add_object(server.obstacle_rocks, 4)
    # server.Tile_1 = load_image('tile_1.png')
    # server.Tile_2 = load_image('tile_2.png')
    # server.Tile_3 = load_image('tile_3.png')
    # server.Tile_4 = load_image('tile_4.png')
    # server.Tile_5 = load_image('tile_5.png')
    # server.Tile_6 = load_image('tile_6.png')
    # server.Tile_7 = load_image('tile_7.png')
    # server.Tile_8 = load_image('tile_8.png')
    # server.Tile_9 = load_image('tile_9.png')
    make_Map()


def make_Map():
    f = open('d:/2DGP/Project/Stage/stage_1.txt')
    for i in range(7):
        server.tile.append(f.readline())
    f.close()

    for i in range(len(server.tile[6])):
        if server.tile[6][i] == '1':
            server.doors.append(Door_ud(800 // 2, 18, 'Door_7.png'))
        elif server.tile[6][i] == '2':
            server.doors.append(Door_lr(800 - 18, 600 // 2, 'Door_5.png'))
        elif server.tile[6][i] == '3':
            server.doors.append(Door_ud(800 // 2, 600 - 18, 'Door_8.png'))
        elif server.tile[6][i] == '4':
            server.doors.append(Door_lr(18, 600 // 2, 'Door_6.png'))
        elif server.tile[6][i] == '5':
            server.doors.append(Door_ud(800 // 2, 18, 'Door_3.png'))
        elif server.tile[6][i] == '6':
            server.doors.append(Door_lr(800 - 18, 600 // 2, 'Door_1.png'))
        elif server.tile[6][i] == '7':
            server.doors.append(Door_ud(800 // 2, 600 - 18, 'Door_4.png'))
        elif server.tile[6][i] == '8':
            server.doors.append(Door_lr(18, 600 // 2, 'Door_2.png'))
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
    for line in range(6):
        for n in range(8):
            if server.tile[line][n] == '1':
                server.Tile_1.clip_draw(0, 0, 100, 100, n * 100 + 50, (5 - line) * 100 + 50)
            elif server.tile[line][n] == '2':
                server.Tile_2.clip_draw(0, 0, 100, 100, n * 100 + 50, (5 - line) * 100 + 50)
            elif server.tile[line][n] == '3':
                server.Tile_3.clip_draw(0, 0, 100, 100, n * 100 + 50, (5 - line) * 100 + 50)
            elif server.tile[line][n] == '4':
                server.Tile_4.clip_draw(0, 0, 100, 100, n * 100 + 50, (5 - line) * 100 + 50)
            elif server.tile[line][n] == '5':
                server.Tile_5.clip_draw(0, 0, 100, 100, n * 100 + 50, (5 - line) * 100 + 50)
            elif server.tile[line][n] == '6':
                server.Tile_6.clip_draw(0, 0, 100, 100, n * 100 + 50, (5 - line) * 100 + 50)
            elif server.tile[line][n] == '7':
                server.Tile_7.clip_draw(0, 0, 100, 100, n * 100 + 50, (5 - line) * 100 + 50)
            elif server.tile[line][n] == '8':
                server.Tile_8.clip_draw(0, 0, 100, 100, n * 100 + 50, (5 - line) * 100 + 50)
            elif server.tile[line][n] == '9':
                server.Tile_9.clip_draw(0, 0, 100, 100, n * 100 + 50, (5 - line) * 100 + 50)

    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






