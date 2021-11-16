import random
import json
import os

from pico2d import *
import game_framework
import game_world

from Isaac_Head import Isaac_head
from Isaac_Body import Isaac_body

name = "MainState"

isaac_head = None
isaac_body = None

def enter():
    global issac_head, isaac_body
    issac_head = Isaac_head()
    isaac_body = Isaac_body()
    game_world.add_object(issac_head, 1)
    game_world.add_object(isaac_body, 0)


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
            issac_head.handle_event(event)
            isaac_body.handle_event(event)



def update():
    for game_object in game_world.all_objects():
        game_object.update()
    # delay(0.1)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






