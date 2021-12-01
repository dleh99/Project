from Isaac_Head import Isaac_head
from Isaac_Body import Isaac_body
import server
import random
import json
import os

from pico2d import *
import game_framework
import game_world

import Stage_1_map_0

name = "set_up"

def enter():
    server.isaac_head = Isaac_head()
    server.isaac_body = Isaac_body()
    game_world.add_object(server.isaac_body, 8)
    game_world.add_object(server.isaac_head, 8)
    game_framework.change_state(Stage_1_map_0)

def update():
    pass

def draw():
    pass


def exit():
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    pass
