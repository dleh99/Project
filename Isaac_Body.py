import os

import game_framework
from pico2d import *
import game_world
import collision
import server

os.chdir('d:/2DGP/Project/Sprite')

PIXEL_PER_METER = (1.0 / 0.033) # 1px = 3.3 cm
RUN_SPEED_MPS = 50.0 / 10.8     # 50m per 10.8 sec
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.166         # 1초에 6번 움직임
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
    def enter(body, event):
        if event == D_DOWN:
            body.velocity_x += body.Accel * RUN_SPEED_PPS
            body.dir = 2
        elif event == A_DOWN:
            body.velocity_x -= body.Accel * RUN_SPEED_PPS
            body.dir = 4
        elif event == D_UP:
            body.velocity_x -= body.Accel * RUN_SPEED_PPS
        elif event == A_UP:
            body.velocity_x += body.Accel * RUN_SPEED_PPS
        if event == W_DOWN:
            body.velocity_y += body.Accel * RUN_SPEED_PPS
            body.dir = 3
        elif event == S_DOWN:
            body.velocity_y -= body.Accel * RUN_SPEED_PPS
            body.dir = 1
        elif event == W_UP:
            body.velocity_y -= body.Accel * RUN_SPEED_PPS
        elif event == S_UP:
            body.velocity_y += body.Accel * RUN_SPEED_PPS

    def exit(body, event):
        pass

    def do(body):
        body.frame = 0

    def draw(body):
        if body.dir == 1:
            body.image.clip_draw(int(body.frame) * body.size_x, 2 * 25, body.size_x, body.size_y, body.x, body.y)
        elif body.dir == 2:
            body.image.clip_draw(int(body.frame) * body.size_x, 1 * 25, body.size_x, body.size_y, body.x, body.y)
        elif body.dir == 3:
            body.image.clip_draw(int(body.frame) * body.size_x, 2 * 25, body.size_x, body.size_y, body.x, body.y)
        elif body.dir == 4:
            body.image.clip_draw(int(body.frame) * body.size_x, 0 * 25, body.size_x, body.size_y, body.x, body.y)

class One_RunState:

    def enter(body, event):
        if event == D_DOWN:
            body.velocity_x += body.Accel * RUN_SPEED_PPS
            body.dir = 2
        elif event == A_DOWN:
            body.velocity_x -= body.Accel * RUN_SPEED_PPS
            body.dir = 4
        elif event == D_UP:
            body.velocity_x -= body.Accel * RUN_SPEED_PPS
        elif event == A_UP:
            body.velocity_x += body.Accel * RUN_SPEED_PPS
        if event == W_DOWN:
            body.velocity_y += body.Accel * RUN_SPEED_PPS
            body.dir = 3
        elif event == S_DOWN:
            body.velocity_y -= body.Accel * RUN_SPEED_PPS
            body.dir = 1
        elif event == W_UP:
            body.velocity_y -= body.Accel * RUN_SPEED_PPS
        elif event == S_UP:
            body.velocity_y += body.Accel * RUN_SPEED_PPS

    def exit(body, event):
        pass

    def do(body):
        body.x += body.velocity_x * game_framework.frame_time
        body.y += body.velocity_y * game_framework.frame_time
        body.x = clamp(30 + 45 // 2, body.x, 800 - 30 - 45 // 2)
        body.y = clamp(30 + body.size_y // 2, body.y, 600 - 30 - (34 + body.size_y // 2))
        body.frame = (body.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 10

    def draw(body):
        if body.dir == 1:
            body.image.clip_draw(int(body.frame) * body.size_x, 2 * 25, body.size_x, body.size_y, body.x, body.y)
        elif body.dir == 2:
            body.image.clip_draw(int(body.frame) * body.size_x, 1 * 25, body.size_x, body.size_y, body.x, body.y)
        elif body.dir == 3:
            body.image.clip_draw(int(body.frame) * body.size_x, 2 * 25, body.size_x, body.size_y, body.x, body.y)
        elif body.dir == 4:
            body.image.clip_draw(int(body.frame) * body.size_x, 0 * 25, body.size_x, body.size_y, body.x, body.y)


class Two_RunState:

    def enter(body, event):
        if event == D_DOWN:
            body.velocity_x += body.Accel * RUN_SPEED_PPS
            body.dir = 2
        elif event == A_DOWN:
            body.velocity_x -= body.Accel * RUN_SPEED_PPS
            body.dir = 4
        elif event == D_UP:
            body.velocity_x -= body.Accel * RUN_SPEED_PPS
        elif event == A_UP:
            body.velocity_x += body.Accel * RUN_SPEED_PPS
        if event == W_DOWN:
            body.velocity_y += body.Accel * RUN_SPEED_PPS
            body.dir = 3
        elif event == S_DOWN:
            body.velocity_y -= body.Accel * RUN_SPEED_PPS
            body.dir = 1
        elif event == W_UP:
            body.velocity_y -= body.Accel * RUN_SPEED_PPS
        elif event == S_UP:
            body.velocity_y += body.Accel * RUN_SPEED_PPS

    def exit(body, event):
        pass

    def do(body):
        body.x += body.velocity_x * game_framework.frame_time
        body.y += body.velocity_y * game_framework.frame_time
        body.x = clamp(30 + 45 // 2, body.x, 800 - 30 - 45 // 2)
        body.y = clamp(30 + body.size_y // 2, body.y, 600 - 30 - (34 + body.size_y // 2))
        body.frame = (body.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 10

    def draw(body):
        if body.dir == 1:
            body.image.clip_draw(int(body.frame) * body.size_x, 2 * 25, body.size_x, body.size_y, body.x, body.y)
        elif body.dir == 2:
            body.image.clip_draw(int(body.frame) * body.size_x, 1 * 25, body.size_x, body.size_y, body.x, body.y)
        elif body.dir == 3:
            body.image.clip_draw(int(body.frame) * body.size_x, 2 * 25, body.size_x, body.size_y, body.x, body.y)
        elif body.dir == 4:
            body.image.clip_draw(int(body.frame) * body.size_x, 0 * 25, body.size_x, body.size_y, body.x, body.y)

class Three_RunState:

    def enter(body, event):
        if event == D_DOWN:
            body.velocity_x += body.Accel * RUN_SPEED_PPS
            body.dir = 2
        elif event == A_DOWN:
            body.velocity_x -= body.Accel * RUN_SPEED_PPS
            body.dir = 4
        elif event == D_UP:
            body.velocity_x -= body.Accel * RUN_SPEED_PPS
        elif event == A_UP:
            body.velocity_x += body.Accel * RUN_SPEED_PPS
        if event == W_DOWN:
            body.velocity_y += body.Accel * RUN_SPEED_PPS
            body.dir = 3
        elif event == S_DOWN:
            body.velocity_y -= body.Accel * RUN_SPEED_PPS
            body.dir = 1
        elif event == W_UP:
            body.velocity_y -= body.Accel * RUN_SPEED_PPS
        elif event == S_UP:
            body.velocity_y += body.Accel * RUN_SPEED_PPS

    def exit(body, event):
        pass

    def do(body):
        body.x += body.velocity_x * game_framework.frame_time
        body.y += body.velocity_y * game_framework.frame_time
        body.x = clamp(30 + 45 // 2, body.x, 800 - 30 - 45 // 2)
        body.y = clamp(30 + body.size_y // 2, body.y, 600 - 30 - (34 + body.size_y // 2))
        body.frame = (body.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 10

    def draw(body):
        if body.dir == 1:
            body.image.clip_draw(int(body.frame) * body.size_x, 2 * 25, body.size_x, body.size_y, body.x, body.y)
        elif body.dir == 2:
            body.image.clip_draw(int(body.frame) * body.size_x, 1 * 25, body.size_x, body.size_y, body.x, body.y)
        elif body.dir == 3:
            body.image.clip_draw(int(body.frame) * body.size_x, 2 * 25, body.size_x, body.size_y, body.x, body.y)
        elif body.dir == 4:
            body.image.clip_draw(int(body.frame) * body.size_x, 0 * 25, body.size_x, body.size_y, body.x, body.y)


next_state_table = {
    IdleState: {W_DOWN: One_RunState, A_DOWN: One_RunState, S_DOWN: One_RunState, D_DOWN: One_RunState,
                W_UP: One_RunState, A_UP: One_RunState, S_UP: One_RunState, D_UP: One_RunState,
                DOWN_DOWN: IdleState, RIGHT_DOWN: IdleState, UP_DOWN: IdleState, LEFT_DOWN: IdleState},
    One_RunState: {W_DOWN: Two_RunState, A_DOWN: Two_RunState, S_DOWN: Two_RunState, D_DOWN: Two_RunState,
                W_UP: IdleState, A_UP: IdleState, S_UP: IdleState, D_UP: IdleState,
                DOWN_DOWN: One_RunState, RIGHT_DOWN: One_RunState, UP_DOWN: One_RunState, LEFT_DOWN: One_RunState},
    Two_RunState: {W_DOWN: Three_RunState, A_DOWN: Three_RunState, S_DOWN: Three_RunState, D_DOWN: Three_RunState,
                W_UP: One_RunState, A_UP: One_RunState, S_UP: One_RunState, D_UP: One_RunState,
                DOWN_DOWN: Two_RunState, RIGHT_DOWN: Two_RunState, UP_DOWN: Two_RunState, LEFT_DOWN: Two_RunState},
    Three_RunState: {W_DOWN: Three_RunState, A_DOWN: Three_RunState, S_DOWN: Three_RunState, D_DOWN: Three_RunState,
                W_UP: Two_RunState, A_UP: Two_RunState, S_UP: Two_RunState, D_UP: Two_RunState,
                DOWN_DOWN: Three_RunState, RIGHT_DOWN: Three_RunState, UP_DOWN: Three_RunState, LEFT_DOWN: Three_RunState}
}

class Isaac_body:

    def __init__(self):
        self.image = load_image('Isaac_Body_Full.png')
        self.dir = 1                # 1 = 정면, 2 = 오른쪽, 3 = 위, 4 = 왼쪽
        self.frame = 0
        self.velocity_x = 0
        self.velocity_y = 0
        self.Accel = 1.0
        self.x = 800 // 2
        self.y = 600 // 2
        self.size_x = 29
        self.size_y = 25
        self.life = 3
        self.invincibility = False
        self.invincibilitycount = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.nowPos = 1

    def get_bb(self):
        return self.x - self.size_x // 2, self.y - self.size_y // 2, self.x + self.size_x // 2, self.y + self.size_y // 2

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        if self.invincibility:
            self.invincibilitycount += 1
            if self.invincibilitycount == 1000:
                self.invincibility = False
                self.invincibilitycount = 0
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

        for mob in game_world.Mob_objects():
            for isaac in game_world.Isaac_objects():
                if abs(isaac.x - mob.x) > 100:
                    mob.x += (isaac.x - mob.x) / 1000
                else:
                    mob.x += (isaac.x - mob.x) / 400
                if abs(isaac.y - mob.y) > 100:
                    mob.y += (isaac.y - mob.y) / 1000
                else:
                    mob.y += (isaac.y - mob.y) / 400
                mob.x = clamp(mob.pixel_x // 2, mob.x, 800 - mob.pixel_x // 2)
                mob.y = clamp(mob.pixel_y // 2, mob.y, 600 - (mob.pixel_y // 2))
                if not isaac.invincibility:
                    if collision.up_collide(isaac, mob) or collision.down_collide(isaac, mob) or collision.left_collide(isaac, mob) or \
                            collision.right_collide(isaac, mob) or collision.collide(isaac, mob):
                        for all in game_world.Isaac_objects():
                            all.invincibility = True
                            all.life -= 1
                        if collision.up_collide(isaac, mob):
                            for all in game_world.Isaac_objects():
                                all.y += RUN_SPEED_PPS // 3
                        elif collision.down_collide(isaac, mob):
                            for all in game_world.Isaac_objects():
                                all.y -= RUN_SPEED_PPS // 3
                        elif collision.left_collide(isaac, mob):
                            for all in game_world.Isaac_objects():
                                all.x -= RUN_SPEED_PPS // 3
                        else:
                            for all in game_world.Isaac_objects():
                                all.x += RUN_SPEED_PPS // 3
        for door in game_world.Door_objects():
            if collision.collide(door, self):
                if server.Floor_1[self.nowPos]:
                    if self.y <= 100:
                        for me in game_world.Isaac_objects():
                            me.y += 450
                            me.nowPos += 3
                    elif self.y >= 500:
                        for me in game_world.Isaac_objects():
                            me.y -= 450
                            me.nowPos -= 3
                    elif self.x <= 100:
                        for me in game_world.Isaac_objects():
                            me.x += 650
                            me.nowPos -= 1
                    elif self.x >= 700:
                        for me in game_world.Isaac_objects():
                            me.x -= 650
                            me.nowPos += 1

    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())
        #fill here


    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
