import game_framework
from pico2d import *

import game_world
import start_state
import server


name = "Game_over_state"
image = None
font = None
score = 0

def initial():
    # =============================================
    server.isaac_head = None
    server.isaac_body = None
    server.isaac_hearts = None
    # =============================================
    server.red_spiders = None
    server.satan = None
    server.ly = None
    server.boss = None
    server.head_hunt = None
    # =============================================
    server.obstacle_rocks = None
    server.item = None
    # =============================================
    server.background_sound = None
    server.sound_do = 0
    server.do = 0
    # =============================================
    server.doors = []
    server.tile = []
    server.next_door = None
    server.Floor_1 = [False for _ in range(16)]
    server.Floor_1_item = [False for _ in range(16)]
    server.Floor_1_item_store = [0 for _ in range(16)]
    server.Floor_2 = [False for _ in range(36)]
    server.Floor_2_item = [False for _ in range(36)]
    server.Floor_2_item_store = [0 for _ in range(36)]
    server.Background_num, Obs_num, Door_num, Item_num, Mob_num, Tear_num, Mob_Tear_num, Isaac_num = range(8)

def enter():
    global image, font, score
    score = (- get_time() + server.isaac_head.start_time + server.isaac_head.Score)
    font = load_font('ENCR10B.TTF', 60)
    image = load_image('game_over_image.png')
    server.background_sound = load_music('death_sound.mp3')
    server.background_sound.set_volume(30)
    server.background_sound.repeat_play()


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
    global score
    clear_canvas()
    image.draw(400, 300)
    font.draw((800 // 2), 300 - 100, '%0.f' % score, (255, 255, 255))
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass