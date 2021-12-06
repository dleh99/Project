import game_framework
from pico2d import *

import game_world
import start_state
import server


name = "Game_over_state"
image = None

def initial():
    server.isaac_head = None
    server.isaac_body = None
    server.red_spiders = None
    server.satan = None
    server.fly = None
    server.boss = None
    server.head_hunt = None
    server.isaac_hearts = None
    server.obstacle_rocks = None
    server.item = None
    server.doors = []
    server.tile = []
    server.Floor_1 = [False for _ in range(16)]
    server.Floor_1_item = [False for _ in range(16)]
    server.Floor_1_item_store = [0 for _ in range(16)]
    server.Background_num, Obs_num, Door_num, Item_num, Mob_num, Tear_num, Mob_Tear_num, Isaac_num = range(8)

def enter():
    global image
    image = load_image('title_image.png')


def exit():
    global image
    del(image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                initial()
                game_world.clear()
                game_framework.change_state(start_state)


def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass