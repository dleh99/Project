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
from heart import Isaac_heart

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
    isaac_hearts = [Isaac_heart((i + 1), 550) for i in range(isaac_head.life)]
    red_spiders = [Red_Spider() for i in range(3)]
    game_world.add_object(isaac_body, 1)
    game_world.add_object(isaac_head, 1)
    game_world.add_objects(red_spiders, 3)
    game_world.add_objects(isaac_hearts, 0)


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
    for i in range(3):
        if abs(isaac_body.x - red_spiders[i].x) > 100:
            red_spiders[i].x += (isaac_body.x - red_spiders[i].x) / 500
        else:
            red_spiders[i].x += (isaac_body.x - red_spiders[i].x) / 200
        if abs(isaac_body.y - red_spiders[i].y) > 100:
            red_spiders[i].y += (isaac_body.y - red_spiders[i].y) / 500
        else:
            red_spiders[i].y += (isaac_body.y - red_spiders[i].y) / 200
        red_spiders[i].x = clamp(red_spiders[i].pixel_x // 2, red_spiders[i].x, 800 - red_spiders[i].pixel_x // 2)
        red_spiders[i].y = clamp(red_spiders[i].pixel_y // 2, red_spiders[i].y, 600 - (red_spiders[i].pixel_y // 2))
    #     if collide(red_spiders[i], Isaac_tear):
    #         red_spiders[i].hp -= Isaac_tear.power
        if not isaac_head.invincibility:
            if collide(isaac_body, red_spiders[i]):
                isaac_head.invincibility = True
                isaac_body.life -= 1
            if collide(isaac_head, red_spiders[i]):
                isaac_head.invincibility = True
                isaac_head.life -= 1
    if isaac_body.life < isaac_head.life:
        isaac_head.life = isaac_body.life
        print('몸에 맞았나봐용')
    elif isaac_body.life > isaac_head.life:
        isaac_body.life = isaac_head.life
        print('머리에 맞았나봐용')

    for heart in isaac_hearts:
        isaac_hearts.remove(heart)
        game_world.remove_object(heart)
    isaac_hearts = [Isaac_heart((i + 1), 550) for i in range(isaac_head.life)]
    print(isaac_hearts[0].x)
    game_world.add_objects(isaac_hearts, 0)
    # delay(1.0)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






