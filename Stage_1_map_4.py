# import random
# import json
# import os
#
# from pico2d import *
# import game_framework
# import game_world
#
# from Enemy_spider import *
# from Item import Item_clasic
#
# import State_1_map_2
#
# PIXEL_PER_METER = (1.0 / 0.033) # 1px = 3.3 cm
# RUN_SPEED_MPS = 50.0 / 10.8     # 50m per 10.8 sec
# RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
#
# name = "Stage_1_map_1"
#
# os.chdir('d:/2DGP/Project/Sprite')
#
# item = None
# Tile_1, Tile_2, Tile_3, Tile_4, Tile_5, Tile_6, Tile_7, Tile_8, Tile_9 = None, None, None, None, None, None, None, None, None
# doors = []
# tile = []
#
# def collide(a, b):
#     left_a, bottom_a, right_a, top_a = a.get_bb()
#     left_b, bottom_b, right_b, top_b = b.get_bb()
#
#     if left_a > right_b: return False
#     if right_a < left_b: return False
#     if top_a < bottom_b: return False
#     if bottom_a > top_b: return False
#
#     return True
#
# def up_collide(a, b):
#     left_a, bottom_a, right_a, top_a = a.get_bb()
#     a_middle_Down = (a.x, bottom_a)
#     left_b, bottom_b, right_b, top_b = b.get_bb()
#
#     if left_a > right_b: return False
#     if right_a < left_b: return False
#     if top_a < bottom_b: return False
#     if bottom_a > top_b: return False
#     if left_b < a_middle_Down[0] < right_b and bottom_b < a_middle_Down[1] < top_b: return True
#     else: return False
#
#
# def down_collide(a, b):
#     left_a, bottom_a, right_a, top_a = a.get_bb()
#     a_middle_Up = (a.x, top_a)
#     left_b, bottom_b, right_b, top_b = b.get_bb()
#
#     if left_a > right_b: return False
#     if right_a < left_b: return False
#     if top_a < bottom_b: return False
#     if bottom_a > top_b: return False
#     if left_b < a_middle_Up[0] < right_b and bottom_b < a_middle_Up[1] < top_b: return True
#     else: return False
#
# def left_collide(a, b):
#     left_a, bottom_a, right_a, top_a = a.get_bb()
#     a_middle_right = (right_a, a.y)
#     left_b, bottom_b, right_b, top_b = b.get_bb()
#
#     if left_a > right_b: return False
#     if right_a < left_b: return False
#     if top_a < bottom_b: return False
#     if bottom_a > top_b: return False
#     if left_b < a_middle_right[0] < right_b and bottom_b < a_middle_right[1] < top_b:
#         return True
#     else:
#         return False
#
# def right_collide(a, b):
#     left_a, bottom_a, right_a, top_a = a.get_bb()
#     a_middle_left = (left_a, a.y)
#     left_b, bottom_b, right_b, top_b = b.get_bb()
#
#     if left_a > right_b: return False
#     if right_a < left_b: return False
#     if top_a < bottom_b: return False
#     if bottom_a > top_b: return False
#     if left_b < a_middle_left[0] < right_b and bottom_b < a_middle_left[1] < top_b:
#         return True
#     else:
#         return False
#
# def enter():
#     global Tile_1, Tile_2, Tile_3, Tile_4, Tile_5, Tile_6, Tile_7, Tile_8, Tile_9
#     global item
#     Tile_1 = load_image('tile_1.png')
#     Tile_2 = load_image('tile_2.png')
#     Tile_3 = load_image('tile_3.png')
#     Tile_4 = load_image('tile_4.png')
#     Tile_5 = load_image('tile_5.png')
#     Tile_6 = load_image('tile_6.png')
#     Tile_7 = load_image('tile_7.png')
#     Tile_8 = load_image('tile_8.png')
#     Tile_9 = load_image('tile_9.png')
#     item = Item_clasic()
#     game_world.add_object(item, 6)
#     make_Map()
#
#
# def make_Map():
#     global tile, doors
#     f = open('d:/2DGP/Project/Stage/stage_2.txt')
#     for i in range(7):
#         tile.append(f.readline())
#     f.close()
#
#     for i in range(len(tile[6])):
#         if tile[6][i] == '1':
#             doors.append(Door_ud(800 // 2, 18, 'Door_7.png'))
#         elif tile[6][i] == '2':
#             doors.append(Door_lr(800 - 18, 600 // 2, 'Door_5.png'))
#         elif tile[6][i] == '3':
#             doors.append(Door_ud(800 // 2, 600 - 18, 'Door_8.png'))
#         elif tile[6][i] == '4':
#             doors.append(Door_lr(18, 600 // 2, 'Door_6.png'))
#         elif tile[6][i] == '5':
#             doors.append(Door_ud(800 // 2, 18, 'Door_3.png'))
#         elif tile[6][i] == '6':
#             doors.append(Door_lr(800 - 18, 600 // 2, 'Door_1.png'))
#         elif tile[6][i] == '7':
#             doors.append(Door_ud(800 // 2, 600 - 18, 'Door_4.png'))
#         elif tile[6][i] == '8':
#             doors.append(Door_lr(18, 600 // 2, 'Door_2.png'))
#     game_world.add_objects(doors, 5)
#
#
# def exit():
#     global doors
#     for door in doors:
#         game_world.remove_object(door)
#
# def pause():
#     pass
#
#
# def resume():
#     pass
#
#
# def handle_events():
#     events = get_events()
#     for event in events:
#         if event.type == SDL_QUIT:
#             game_framework.quit()
#         elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
#                 game_framework.quit()
#         else:
#             for isaac in game_world.Isaac_objects():
#                 isaac.handle_event(event)
#
#
# def update():
#
#     for game_object in game_world.all_objects():
#         game_object.update()
#     for mob in game_world.Mob_objects():
#         for isaac in game_world.Isaac_objects():
#             if abs(isaac.x - mob.x) > 100:
#                 mob.x += (isaac.x - mob.x) / 1000
#             else:
#                 mob.x += (isaac.x - mob.x) / 400
#             if abs(isaac.y - mob.y) > 100:
#                 mob.y += (isaac.y - mob.y) / 1000
#             else:
#                 mob.y += (isaac.y - mob.y) / 400
#             mob.x = clamp(mob.pixel_x // 2, mob.x, 800 - mob.pixel_x // 2)
#             mob.y = clamp(mob.pixel_y // 2, mob.y, 600 - (mob.pixel_y // 2))
#             if not isaac.invincibility:
#                 if up_collide(isaac, mob) or down_collide(isaac, mob) or left_collide(isaac, mob) or \
#                         right_collide(isaac, mob) or collide(isaac, mob):
#                     for all in game_world.Isaac_objects():
#                         all.invincibility = True
#                         all.life -= 1
#                     if up_collide(isaac, mob):
#                         for all in game_world.Isaac_objects():
#                             all.y += RUN_SPEED_PPS // 3
#                     elif down_collide(isaac, mob):
#                         for all in game_world.Isaac_objects():
#                             all.y -= RUN_SPEED_PPS // 3
#                     elif left_collide(isaac, mob):
#                         for all in game_world.Isaac_objects():
#                             all.x -= RUN_SPEED_PPS // 3
#                     else:
#                         for all in game_world.Isaac_objects():
#                             all.x += RUN_SPEED_PPS // 3
#     for mob in game_world.Mob_objects():
#         for tear in game_world.Tear_objects():
#             if collide(mob, tear):
#                 game_world.remove_object(tear)
#                 mob.hp -= tear.power
#                 if mob.hp <= 0:
#                     game_world.remove_object(mob)
#     for obs in game_world.Obs_objects():
#         for isaac in game_world.Isaac_objects():
#             if up_collide(isaac, obs):
#                 for all in game_world.Isaac_objects():
#                     all.y -= all.velocity_y * game_framework.frame_time
#             if down_collide(isaac, obs):
#                 for all in game_world.Isaac_objects():
#                     all.y -= all.velocity_y * game_framework.frame_time
#             if left_collide(isaac, obs):
#                 for all in game_world.Isaac_objects():
#                     all.x -= all.velocity_x * game_framework.frame_time
#             if right_collide(isaac, obs):
#                 for all in game_world.Isaac_objects():
#                     all.x -= all.velocity_x * game_framework.frame_time
#         for tear in game_world.Tear_objects():
#             if collide(tear, obs):
#                 game_world.remove_object(tear)
#         for enemy_tear in game_world.Mob_Tear_objects():
#             if collide(enemy_tear, obs):
#                 game_world.remove_object(enemy_tear)
#     for door in game_world.Door_objects():
#         for isaac in game_world.Isaac_objects():
#             if right_collide(isaac, door):
#                 for all in game_world.Isaac_objects():
#                     pass
#             elif up_collide(isaac, door):
#                 for all in game_world.Isaac_objects():
#                     all.y = 600 - 30
#                     game_framework.change_state(State_1_map_2)
#     for item in game_world.Item_objects():
#         for isaac in game_world.Isaac_objects():
#             if collide(isaac, item):
#                 game_world.remove_object(item)
#                 for all in game_world.Isaac_objects():
#                     all.life += 4
#     # delay(1.0)
import random
import json
import os

from pico2d import *
import game_framework
import game_world
import server

import Stage_1_map_1
import Stage_1_map_5

from Isaac_Head import Isaac_head
from Isaac_Body import Isaac_body
from Item import *
import make_map
import destroy_map

PIXEL_PER_METER = (1.0 / 0.033) # 1px = 3.3 cm
RUN_SPEED_MPS = 50.0 / 10.8     # 50m per 10.8 sec
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

name = "Stage_1_map_4"

def enter():
    if server.item == None:
        server.item = Item_Heal()
        game_world.add_object(server.item, 6)
    make_map.make_Map('d:/2DGP/Project/Stage/stage_4.txt')


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
    if len(game_world.objects[3]) == 0:
        server.Floor_1[1] = True
    if server.isaac_head.nowPos == 1:
        game_framework.change_state(Stage_1_map_1)
    if server.isaac_head.nowPos == 5:
        game_framework.change_state(Stage_1_map_5)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
