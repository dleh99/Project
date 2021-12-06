import game_framework
from pico2d import *
import server
import game_world

import set_up
import Stage_2_map_8


name = "stage2_set_up"
image = None
timer = 0

def enter():
    global image
    image = load_image('next_stage_image.png')
    server.isaac_body.next_floor(8)
    server.isaac_head.next_floor(8)


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
                game_framework.change_state(Stage_2_map_8)


def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()


def update():
    global timer
    timer += game_framework.frame_time

    if timer >= 3.0:
        game_framework.change_state(Stage_2_map_8)


def pause():
    pass


def resume():
    pass