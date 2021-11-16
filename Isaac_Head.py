import os

import game_framework
from pico2d import *

import game_world

os.chdir('d:/2DGP/Project/Sprite')

PIXEL_PER_METER = (1.0 / 0.033) # 1px = 3.3 cm
RUN_SPEED_MPS = 50.0 / 10.8     # 50m per 10.8 sec
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 2

W_DOWN, A_DOWN, S_DOWN, D_DOWN, W_UP, A_UP, S_UP, D_UP, LEFT_DOWN, RIGHT_DOWN, UP_DOWN, DOWN_DOWN = range(12)

key_event_table = {
    (SDL_KEYDOWN, SDLK_w): W_DOWN,
    (SDL_KEYDOWN, SDLK_a): A_DOWN,
    (SDL_KEYDOWN, SDLK_s): S_DOWN,
    (SDL_KEYDOWN, SDLK_d): D_DOWN,
    (SDL_KEYUP, SDLK_w): W_UP,
    (SDL_KEYUP, SDLK_a): A_UP,
    (SDL_KEYUP, SDLK_s): S_UP,
    (SDL_KEYUP, SDLK_d): D_UP,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
}

class IdleState:
    def enter(head, event):
        if event == D_DOWN:
            head.velocity_x += RUN_SPEED_PPS
            head.dir = 2
        elif event == A_DOWN:
            head.velocity_x -= RUN_SPEED_PPS
            head.dir = 4
        elif event == D_UP:
            head.velocity_x -= RUN_SPEED_PPS
        elif event == A_UP:
            head.velocity_x += RUN_SPEED_PPS
        if event == W_DOWN:
            head.velocity_y += RUN_SPEED_PPS
            head.dir = 3
        elif event == S_DOWN:
            head.velocity_y -= RUN_SPEED_PPS
            head.dir = 1
        elif event == W_UP:
            head.velocity_y -= RUN_SPEED_PPS
        elif event == S_UP:
            head.velocity_y += RUN_SPEED_PPS

    def exit(head, event):
        pass

    def do(head):
        head.frame = (head.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

    def draw(head):
        if head.dir == 1:
            head.image.clip_draw(0 * head.size_x, 0, head.size_x, head.size_y, head.x, head.y)
        elif head.dir == 2:
            head.image.clip_draw(2 * head.size_x, 0, head.size_x, head.size_y, head.x, head.y)
        elif head.dir == 3:
            head.image.clip_draw(4 * head.size_x, 0, head.size_x, head.size_y, head.x, head.y)
        elif head.dir == 4:
            head.image.clip_draw(6 * head.size_x, 0, head.size_x, head.size_y, head.x, head.y)

class One_RunState:

    def enter(head, event):
        if event == D_DOWN:
            head.velocity_x += RUN_SPEED_PPS
            head.dir = 2
        elif event == A_DOWN:
            head.velocity_x -= RUN_SPEED_PPS
            head.dir = 4
        elif event == D_UP:
            head.velocity_x -= RUN_SPEED_PPS
        elif event == A_UP:
            head.velocity_x += RUN_SPEED_PPS
        if event == W_DOWN:
            head.velocity_y += RUN_SPEED_PPS
            head.dir = 3
        elif event == S_DOWN:
            head.velocity_y -= RUN_SPEED_PPS
            head.dir = 1
        elif event == W_UP:
            head.velocity_y -= RUN_SPEED_PPS
        elif event == S_UP:
            head.velocity_y += RUN_SPEED_PPS

    def exit(head, event):
        pass

    def do(head):
        head.x += head.velocity_x * game_framework.frame_time
        head.y += head.velocity_y * game_framework.frame_time
        head.x = clamp(head.size_x // 2, head.x, 800 - head.size_x // 2)
        head.y = clamp(head.size_y // 2 + 17, head.y, 600 - head.size_y // 2)

    def draw(head):
        if head.dir == 1:
            head.image.clip_draw(0 * head.size_x, 0, head.size_x, head.size_y, head.x, head.y)
        elif head.dir == 2:
            head.image.clip_draw(2 * head.size_x, 0, head.size_x, head.size_y, head.x, head.y)
        elif head.dir == 3:
            head.image.clip_draw(4 * head.size_x, 0, head.size_x, head.size_y, head.x, head.y)
        elif head.dir == 4:
            head.image.clip_draw(6 * head.size_x, 0, head.size_x, head.size_y, head.x, head.y)


class Two_RunState:

    def enter(head, event):
        if event == D_DOWN:
            head.velocity_x += RUN_SPEED_PPS
            head.dir = 2
        elif event == A_DOWN:
            head.velocity_x -= RUN_SPEED_PPS
            head.dir = 4
        elif event == D_UP:
            head.velocity_x -= RUN_SPEED_PPS
        elif event == A_UP:
            head.velocity_x += RUN_SPEED_PPS
        if event == W_DOWN:
            head.velocity_y += RUN_SPEED_PPS
            head.dir = 3
        elif event == S_DOWN:
            head.velocity_y -= RUN_SPEED_PPS
            head.dir = 1
        elif event == W_UP:
            head.velocity_y -= RUN_SPEED_PPS
        elif event == S_UP:
            head.velocity_y += RUN_SPEED_PPS

    def exit(head, event):
        pass

    def do(head):
        head.x += head.velocity_x * game_framework.frame_time
        head.y += head.velocity_y * game_framework.frame_time
        head.x = clamp(head.size_x // 2, head.x, 800 - head.size_x // 2)
        head.y = clamp(head.size_y // 2 + 17, head.y, 600 - head.size_y // 2)

    def draw(head):
        if head.dir == 1:
            head.image.clip_draw(0 * head.size_x, 0, head.size_x, head.size_y, head.x, head.y)
        elif head.dir == 2:
            head.image.clip_draw(2 * head.size_x, 0, head.size_x, head.size_y, head.x, head.y)
        elif head.dir == 3:
            head.image.clip_draw(4 * head.size_x, 0, head.size_x, head.size_y, head.x, head.y)
        elif head.dir == 4:
            head.image.clip_draw(6 * head.size_x, 0, head.size_x, head.size_y, head.x, head.y)

class Three_RunState:

    def enter(head, event):
        if event == D_DOWN:
            head.velocity_x += RUN_SPEED_PPS
            head.dir = 2
        elif event == A_DOWN:
            head.velocity_x -= RUN_SPEED_PPS
            head.dir = 4
        elif event == D_UP:
            head.velocity_x -= RUN_SPEED_PPS
        elif event == A_UP:
            head.velocity_x += RUN_SPEED_PPS
        if event == W_DOWN:
            head.velocity_y += RUN_SPEED_PPS
            head.dir = 3
        elif event == S_DOWN:
            head.velocity_y -= RUN_SPEED_PPS
            head.dir = 1
        elif event == W_UP:
            head.velocity_y -= RUN_SPEED_PPS
        elif event == S_UP:
            head.velocity_y += RUN_SPEED_PPS

    def exit(head, event):
        pass

    def do(head):
        head.x += head.velocity_x * game_framework.frame_time
        head.y += head.velocity_y * game_framework.frame_time
        head.x = clamp(head.size_x // 2, head.x, 800 - head.size_x // 2)
        head.y = clamp(head.size_y // 2 + 17, head.y, 600 - head.size_y // 2)

    def draw(head):
        if head.dir == 1:
            head.image.clip_draw(0 * head.size_x, 0, head.size_x, head.size_y, head.x, head.y)
        elif head.dir == 2:
            head.image.clip_draw(2 * head.size_x, 0, head.size_x, head.size_y, head.x, head.y)
        elif head.dir == 3:
            head.image.clip_draw(4 * head.size_x, 0, head.size_x, head.size_y, head.x, head.y)
        elif head.dir == 4:
            head.image.clip_draw(6 * head.size_x, 0, head.size_x, head.size_y, head.x, head.y)


next_state_table = {
    IdleState: {W_DOWN: One_RunState, A_DOWN: One_RunState, S_DOWN: One_RunState, D_DOWN: One_RunState,
                W_UP: One_RunState, A_UP: One_RunState, S_UP: One_RunState, D_UP: One_RunState},
    One_RunState: {W_DOWN: Two_RunState, A_DOWN: Two_RunState, S_DOWN: Two_RunState, D_DOWN: Two_RunState,
                W_UP: IdleState, A_UP: IdleState, S_UP: IdleState, D_UP: IdleState},
    Two_RunState: {W_DOWN: Three_RunState, A_DOWN: Three_RunState, S_DOWN: Three_RunState, D_DOWN: Three_RunState,
                W_UP: One_RunState, A_UP: One_RunState, S_UP: One_RunState, D_UP: One_RunState},
    Three_RunState: {W_DOWN: Three_RunState, A_DOWN: Three_RunState, S_DOWN: Three_RunState, D_DOWN: Three_RunState,
                W_UP: Two_RunState, A_UP: Two_RunState, S_UP: Two_RunState, D_UP: Two_RunState}
}

class Isaac_head:

    def __init__(self):
        self.image = load_image('Isaac_Head.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 1                # 1 = 정면, 2 = 오른쪽, 3 = 위, 4 = 왼쪽
        self.frame = 0
        self.velocity_x = 0
        self.velocity_y = 0
        self.x = 800 // 2
        self.y = 600 // 2 + 25
        self.size_x = 45
        self.size_y = 42
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def get_bb(self):
        return self.x - self.size_x // 2, self.y - self.size_y // 2, self.x + self.size_x // 2, self.y + self.size_y // 2


    def fire_ball(self):
        pass


    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))
        draw_rectangle(*self.get_bb())
        #fill here


    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
