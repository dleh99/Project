import random
import json
import os

from pico2d import *
import game_framework
import game_world
import server
from item_store_load import *

import Stage_1_map_11

from Tile import *
from Item import *
import make_map
import destroy_map
from Enemy_Boss_Teratoma import *

PIXEL_PER_METER = (1.0 / 0.033) # 1px = 3.3 cm
RUN_SPEED_MPS = 50.0 / 10.8     # 50m per 10.8 sec
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

name = "Stage_1_map_15"

def enter():
    if not server.Floor_1[server.isaac_head.nowPos]:
        server.boss = TERATOMA_pase_1()
        game_world.add_object(server.boss, server.Mob_num)
        server.background_sound = load_music('Boss_sound.mp3')
        server.background_sound.set_volume(30)
        server.background_sound.repeat_play()
    make_map.make_Map('d:/2DGP/Project/Stage/stage_1/stage_15.txt')


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
        if server.do == 0:
            server.do += 1
            server.Floor_1[15] = True
            game_world.add_object(Tile_n(800 // 2, 400), server.Obs_num)
            if not server.Floor_1_item[server.isaac_head.nowPos]:
                if server.Floor_1_item_store[server.isaac_head.nowPos] == 0:
                    store(4)
                else:
                    load(server.Floor_1_item_store[server.isaac_head.nowPos])
        if server.sound_do == 0:
            server.sound_do += 1
            server.background_sound = load_music('Stage_sound.mp3')
            server.background_sound.set_volume(30)
            server.background_sound.repeat_play()
    if server.isaac_head.nowPos == 11:
        game_framework.change_state(Stage_1_map_11)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
