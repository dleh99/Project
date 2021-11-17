import random
import json
import os

from pico2d import *
import game_framework
import game_world

from Isaac_Head import Isaac_head
from Isaac_Body import Isaac_body
from Enemy_spider import *
from Obstacle import Obstacle_Rock

PIXEL_PER_METER = (1.0 / 0.033) # 1px = 3.3 cm
RUN_SPEED_MPS = 50.0 / 10.8     # 50m per 10.8 sec
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

name = "MainState"

os.chdir('d:/2DGP/Project/Sprite')

isaac_head = None
isaac_body = None
red_spiders = None
isaac_hearts = None
obstacle_rocks = None
Tile_1, Tile_2, Tile_3, Tile_4, Tile_5, Tile_6, Tile_7, Tile_8, Tile_9 = None, None, None, None, None, None, None, None, None
tile = []

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def up_collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    a_middle_Down = (a.x, bottom_a)
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    if left_b < a_middle_Down[0] < right_b and bottom_b < a_middle_Down[1] < top_b: return True
    else: return False


def down_collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    a_middle_Up = (a.x, top_a)
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    if left_b < a_middle_Up[0] < right_b and bottom_b < a_middle_Up[1] < top_b: return True
    else: return False

def left_collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    a_middle_right = (right_a, a.y)
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    if left_b < a_middle_right[0] < right_b and bottom_b < a_middle_right[1] < top_b:
        return True
    else:
        return False

def right_collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    a_middle_left = (left_a, a.y)
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    if left_b < a_middle_left[0] < right_b and bottom_b < a_middle_left[1] < top_b:
        return True
    else:
        return False

def enter():
    global isaac_head, isaac_body, red_spiders, isaac_hearts, obstacle_rocks
    global Tile_1, Tile_2, Tile_3, Tile_4, Tile_5, Tile_6, Tile_7, Tile_8, Tile_9
    isaac_head = Isaac_head()
    isaac_body = Isaac_body()
    red_spiders = [Red_Spider() for i in range(3)]
    obstacle_rocks = Obstacle_Rock()
    game_world.add_object(isaac_body, 1)
    game_world.add_object(isaac_head, 1)
    game_world.add_objects(red_spiders, 3)
    game_world.add_object(obstacle_rocks, 4)
    Tile_1 = load_image('tile_1.png')
    Tile_2 = load_image('tile_2.png')
    Tile_3 = load_image('tile_3.png')
    Tile_4 = load_image('tile_4.png')
    Tile_5 = load_image('tile_5.png')
    Tile_6 = load_image('tile_6.png')
    Tile_7 = load_image('tile_7.png')
    Tile_8 = load_image('tile_8.png')
    Tile_9 = load_image('tile_9.png')
    make_Map()


def make_Map():
    global tile
    f = open('d:/2DGP/Project/Stage/stage_1.txt')
    for i in range(6):
        tile.append(f.readline())
    f.close()


def exit():
    game_world.clear()

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
            isaac_head.handle_event(event)
            isaac_body.handle_event(event)



def update():
    global isaac_head, isaac_body, red_spiders

    for game_object in game_world.all_objects():
        game_object.update()
    for mob in game_world.Mob_objects():
        if abs(isaac_body.x - mob.x) > 100:
            mob.x += (isaac_body.x - mob.x) / 500
        else:
            mob.x += (isaac_body.x - mob.x) / 200
        if abs(isaac_body.y - mob.y) > 100:
            mob.y += (isaac_body.y - mob.y) / 500
        else:
            mob.y += (isaac_body.y - mob.y) / 200
        mob.x = clamp(mob.pixel_x // 2, mob.x, 800 - mob.pixel_x // 2)
        mob.y = clamp(mob.pixel_y // 2, mob.y, 600 - (mob.pixel_y // 2))
        if not isaac_head.invincibility:
            if up_collide(isaac_body, mob) or down_collide(isaac_head, mob) or left_collide(isaac_head, mob) or\
                left_collide(isaac_body, mob) or right_collide(isaac_head, mob) or right_collide(isaac_body, mob)or\
                    collide(isaac_body, mob) or collide(isaac_head, mob):
                isaac_head.invincibility = True
                isaac_body.life -= 1
                isaac_head.life -= 1
                if up_collide(isaac_body, mob):
                    isaac_body.y += RUN_SPEED_PPS // 3
                    isaac_head.y += RUN_SPEED_PPS // 3
                elif down_collide(isaac_head, mob):
                    isaac_body.y -= RUN_SPEED_PPS // 3
                    isaac_head.y -= RUN_SPEED_PPS // 3
                elif left_collide(isaac_head, mob) or left_collide(isaac_body, mob):
                    isaac_body.x -= RUN_SPEED_PPS // 3
                    isaac_head.x -= RUN_SPEED_PPS // 3
                else:
                    isaac_body.x += RUN_SPEED_PPS // 3
                    isaac_head.x += RUN_SPEED_PPS // 3
    for mob in game_world.Mob_objects():
        for tear in game_world.Tear_objects():
            if collide(mob, tear):
                game_world.remove_object(tear)
                mob.hp -= tear.power
                if mob.hp <= 0:
                    game_world.remove_object(mob)
    for obs in game_world.Obs_objects():
        if up_collide(isaac_body, obs):
            isaac_body.y -= isaac_body.velocity_y * game_framework.frame_time
            isaac_head.y -= isaac_head.velocity_y * game_framework.frame_time
        if down_collide(isaac_head, obs):
            isaac_body.y -= isaac_body.velocity_y * game_framework.frame_time
            isaac_head.y -= isaac_head.velocity_y * game_framework.frame_time
        if left_collide(isaac_head, obs):
            isaac_body.x -= isaac_body.velocity_x * game_framework.frame_time
            isaac_head.x -= isaac_head.velocity_x * game_framework.frame_time
        if left_collide(isaac_body, obs):
            isaac_body.x -= isaac_body.velocity_x * game_framework.frame_time
            isaac_head.x -= isaac_head.velocity_x * game_framework.frame_time
        if right_collide(isaac_head, obs):
            isaac_body.x -= isaac_body.velocity_x * game_framework.frame_time
            isaac_head.x -= isaac_head.velocity_x * game_framework.frame_time
        if right_collide(isaac_body, obs):
            isaac_body.x -= isaac_body.velocity_x * game_framework.frame_time
            isaac_head.x -= isaac_head.velocity_x * game_framework.frame_time
    # delay(1.0)


def draw():
    global tile
    global Tile_1, Tile_2, Tile_3, Tile_4, Tile_5, Tile_6, Tile_7, Tile_8, Tile_9
    clear_canvas()
    for line in range(6):
        for n in range(8):
            if tile[line][n] == '1':
                Tile_1.clip_draw(0, 0, 100, 100, n * 100 + 50, (5 - line) * 100 + 50)
            elif tile[line][n] == '2':
                Tile_2.clip_draw(0, 0, 100, 100, n * 100 + 50, (5 - line) * 100 + 50)
            elif tile[line][n] == '3':
                Tile_3.clip_draw(0, 0, 100, 100, n * 100 + 50, (5 - line) * 100 + 50)
            elif tile[line][n] == '4':
                Tile_4.clip_draw(0, 0, 100, 100, n * 100 + 50, (5 - line) * 100 + 50)
            elif tile[line][n] == '5':
                Tile_5.clip_draw(0, 0, 100, 100, n * 100 + 50, (5 - line) * 100 + 50)
            elif tile[line][n] == '6':
                Tile_6.clip_draw(0, 0, 100, 100, n * 100 + 50, (5 - line) * 100 + 50)
            elif tile[line][n] == '7':
                Tile_7.clip_draw(0, 0, 100, 100, n * 100 + 50, (5 - line) * 100 + 50)
            elif tile[line][n] == '8':
                Tile_8.clip_draw(0, 0, 100, 100, n * 100 + 50, (5 - line) * 100 + 50)
            elif tile[line][n] == '9':
                Tile_9.clip_draw(0, 0, 100, 100, n * 100 + 50, (5 - line) * 100 + 50)

    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






