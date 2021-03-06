import game_framework
from pico2d import *
import server

import set_up
import rank_state


name = "TitleState"
image = None


def enter():
    global image
    server.background_sound = load_music('title.mp3')
    server.background_sound.set_volume(30)
    server.background_sound.repeat_play()
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
                game_framework.change_state(set_up)
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_r):
                game_framework.change_state(rank_state)


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






