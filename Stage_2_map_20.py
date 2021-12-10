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
import Stage_2_map_19
import Stage_2_map_21
import Stage_2_map_26

from Enemy_Fly import *
from Enemy_spider import *
from Enemy_Head_hunt import *
from Enemy_Satan import *

PIXEL_PER_METER = (1.0 / 0.033) # 1px = 3.3 cm
RUN_SPEED_MPS = 50.0 / 10.8     # 50m per 10.8 sec
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

name = "Stage_2_map_20"

def enter():
    # if not server.Floor_2[server.isaac_head.nowPos]:
    #     rand_num = random.randint(0, 8)
    #     if rand_num == 0:
    #         server.red_spiders = [Red_Spider() for i in range(4)]
    #         game_world.add_objects(server.red_spiders, server.Mob_num)
    #     elif rand_num == 1:
    #         server.red_spiders = [Red_Spider() for i in range(2)]
    #         game_world.add_objects(server.red_spiders, server.Mob_num)
    #         server.fly = [Fly() for i in range(5)]
    #         game_world.add_objects(server.fly, server.Mob_num)
    #     elif rand_num == 2:
    #         server.red_spiders = Red_Spider()
    #         server.head_hunt = [Head_hunt(i * 2) for i in range(4)]
    #         game_world.add_object(server.red_spiders, server.Mob_num)
    #         game_world.add_objects(server.head_hunt, server.Mob_num)
    #     elif rand_num == 3:
    #         server.satan = [Satan(i + 1) for i in range(2)]
    #         game_world.add_objects(server.satan, server.Mob_num)
    #     elif rand_num == 4:
    #         server.satan = Satan(1)
    #         game_world.add_object(server.satan, server.Mob_num)
    #         server.red_spiders = [Red_Spider() for i in range(3)]
    #         game_world.add_objects(server.red_spiders, server.Mob_num)
    #     elif rand_num == 5:
    #         server.fly = [Fly() for i in range(5)]
    #         game_world.add_objects(server.fly, server.Mob_num)
    #         server.head_hunt = [Head_hunt(i) for i in range(4)]
    #         game_world.add_objects(server.head_hunt, server.Mob_num)
    #     elif rand_num == 6:
    #         server.satan = [Satan(i + 1) for i in range(2)]
    #         game_world.add_objects(server.satan, server.Mob_num)
    #         server.fly = [Fly() for i in range(2)]
    #         game_world.add_objects(server.fly, server.Mob_num)
    #     elif rand_num == 7:
    #         server.red_spiders = [Red_Spider() for i in range(7)]
    #         game_world.add_objects(server.red_spiders, server.Mob_num)
    make_map.make_Map('d:/2DGP/Project/Stage/stage_2/stage_20.txt')


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
        server.Floor_2[20] = True
    if server.isaac_head.nowPos == 19:
        game_framework.change_state(Stage_2_map_19)
    if server.isaac_head.nowPos == 21:
        game_framework.change_state(Stage_2_map_21)
    if server.isaac_head.nowPos == 26:
        game_framework.change_state(Stage_2_map_26)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()