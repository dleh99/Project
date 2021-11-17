import random
import json
import os

from pico2d import *
import game_framework
import game_world

from Isaac_Head import Isaac_head
from Isaac_Body import Isaac_body
from Enemy_spider import *
from Isaac_Tear import Isaac_tear

name = "MainState"

isaac_head = None
isaac_body = None
red_spiders = None
isaac_hearts = None

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def enter():
    global isaac_head, isaac_body, red_spiders, isaac_hearts
    isaac_head = Isaac_head()
    isaac_body = Isaac_body()
    red_spiders = [Red_Spider() for i in range(3)]
    game_world.add_object(isaac_body, 1)
    game_world.add_object(isaac_head, 1)
    game_world.add_objects(red_spiders, 3)


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
    global isaac_head, isaac_body, red_spiders, isaac_hearts

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
        #     if collide(red_spiders[i], Isaac_tear):
        #         red_spiders[i].hp -= Isaac_tear.power
        if not isaac_head.invincibility:
            if collide(isaac_body, mob):
                isaac_head.invincibility = True
                isaac_body.life -= 1
                isaac_head.life -= 1
            if collide(isaac_head, mob):
                isaac_head.invincibility = True
                isaac_body.life -= 1
                isaac_head.life -= 1
    # delay(1.0)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






