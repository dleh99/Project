import os

import pico2d.pico2d

import Obstacle
import Tile
import game_framework
from pico2d import *
import game_world
import collision
import server
from Isaac_Head import Isaac_head
import game_over_state
import stage2_set_up

os.chdir('d:/2DGP/Project/Sprite')

PIXEL_PER_METER = (1.0 / 0.033) # 1px = 3.3 cm
RUN_SPEED_MPS = 60.0 / 10.8     # 50m per 10.8 sec
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.166         # 1초에 6번 움직임
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 2

W_DOWN, A_DOWN, S_DOWN, D_DOWN, W_UP, A_UP, S_UP, D_UP, LEFT_DOWN, RIGHT_DOWN, UP_DOWN, DOWN_DOWN, Die = range(13)

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
            body.velocity_x += RUN_SPEED_PPS
            body.dir = 2
        elif event == A_DOWN:
            body.velocity_x -= RUN_SPEED_PPS
            body.dir = 4
        elif event == D_UP:
            body.velocity_x -= RUN_SPEED_PPS
        elif event == A_UP:
            body.velocity_x += RUN_SPEED_PPS
        if event == W_DOWN:
            body.velocity_y += RUN_SPEED_PPS
            body.dir = 3
        elif event == S_DOWN:
            body.velocity_y -= RUN_SPEED_PPS
            body.dir = 1
        elif event == W_UP:
            body.velocity_y -= RUN_SPEED_PPS
        elif event == S_UP:
            body.velocity_y += RUN_SPEED_PPS

    def exit(body, event):
        pass

    def do(body):
        body.frame = 0
        if body.life <= 0:
            body.add_event(Die)

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
            body.velocity_x += RUN_SPEED_PPS
            body.dir = 2
        elif event == A_DOWN:
            body.velocity_x -= RUN_SPEED_PPS
            body.dir = 4
        elif event == D_UP:
            body.velocity_x -= RUN_SPEED_PPS
        elif event == A_UP:
            body.velocity_x += RUN_SPEED_PPS
        if event == W_DOWN:
            body.velocity_y += RUN_SPEED_PPS
            body.dir = 3
        elif event == S_DOWN:
            body.velocity_y -= RUN_SPEED_PPS
            body.dir = 1
        elif event == W_UP:
            body.velocity_y -= RUN_SPEED_PPS
        elif event == S_UP:
            body.velocity_y += RUN_SPEED_PPS

    def exit(body, event):
        pass

    def do(body):
        body.x += body.Accel * body.velocity_x * game_framework.frame_time
        body.y += body.Accel * body.velocity_y * game_framework.frame_time
        body.x = clamp(30 + 45 // 2, body.x, 800 - 30 - 45 // 2)
        body.y = clamp(30 + body.size_y // 2, body.y, 600 - 30 - (34 + body.size_y // 2))
        body.frame = (body.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 10
        body.collision_obs()
        if body.life <= 0:
            body.add_event(Die)

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
            body.velocity_x += RUN_SPEED_PPS
            body.dir = 2
        elif event == A_DOWN:
            body.velocity_x -= RUN_SPEED_PPS
            body.dir = 4
        elif event == D_UP:
            body.velocity_x -= RUN_SPEED_PPS
        elif event == A_UP:
            body.velocity_x += RUN_SPEED_PPS
        if event == W_DOWN:
            body.velocity_y += RUN_SPEED_PPS
            body.dir = 3
        elif event == S_DOWN:
            body.velocity_y -= RUN_SPEED_PPS
            body.dir = 1
        elif event == W_UP:
            body.velocity_y -= RUN_SPEED_PPS
        elif event == S_UP:
            body.velocity_y += RUN_SPEED_PPS

    def exit(body, event):
        pass

    def do(body):
        body.x += body.Accel * body.velocity_x * game_framework.frame_time
        body.y += body.Accel * body.velocity_y * game_framework.frame_time
        body.x = clamp(30 + 45 // 2, body.x, 800 - 30 - 45 // 2)
        body.y = clamp(30 + body.size_y // 2, body.y, 600 - 30 - (34 + body.size_y // 2))
        body.frame = (body.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 10
        body.collision_obs()
        if body.life <= 0:
            body.add_event(Die)

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
            body.velocity_x += RUN_SPEED_PPS
            body.dir = 2
        elif event == A_DOWN:
            body.velocity_x -= RUN_SPEED_PPS
            body.dir = 4
        elif event == D_UP:
            body.velocity_x -= RUN_SPEED_PPS
        elif event == A_UP:
            body.velocity_x += RUN_SPEED_PPS
        if event == W_DOWN:
            body.velocity_y += RUN_SPEED_PPS
            body.dir = 3
        elif event == S_DOWN:
            body.velocity_y -= RUN_SPEED_PPS
            body.dir = 1
        elif event == W_UP:
            body.velocity_y -= RUN_SPEED_PPS
        elif event == S_UP:
            body.velocity_y += RUN_SPEED_PPS

    def exit(body, event):
        pass

    def do(body):
        body.x += body.Accel * body.velocity_x * game_framework.frame_time
        body.y += body.Accel * body.velocity_y * game_framework.frame_time
        body.x = clamp(30 + 45 // 2, body.x, 800 - 30 - 45 // 2)
        body.y = clamp(30 + body.size_y // 2, body.y, 600 - 30 - (34 + body.size_y // 2))
        body.frame = (body.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 10
        body.collision_obs()
        if body.life <= 0:
            body.add_event(Die)

    def draw(body):
        if body.dir == 1:
            body.image.clip_draw(int(body.frame) * body.size_x, 2 * 25, body.size_x, body.size_y, body.x, body.y)
        elif body.dir == 2:
            body.image.clip_draw(int(body.frame) * body.size_x, 1 * 25, body.size_x, body.size_y, body.x, body.y)
        elif body.dir == 3:
            body.image.clip_draw(int(body.frame) * body.size_x, 2 * 25, body.size_x, body.size_y, body.x, body.y)
        elif body.dir == 4:
            body.image.clip_draw(int(body.frame) * body.size_x, 0 * 25, body.size_x, body.size_y, body.x, body.y)

class Die_State:

    def enter(body, event):
        body.velocity_x = 0
        body.velocity_y = 0
        body.frame = 0
        body.image = None
        body.invincibility = True
        body.image = load_image('Isaac_Dead.png')

    def exit(body, event):
        pass

    def do(body):
        body.Die_count += game_framework.frame_time
        if body.Die_count <= 1.0:
            if body.Shake:
                body.Shake_num += 1
                body.x += 0.3
                if body.Shake_num == 10:
                    body.Shake_num = 0
                    body.Shake = False
            else:
                body.Shake_num += 1
                body.x -= 0.3
                if body.Shake_num == 10:
                    body.Shake_num = 0
                    body.Shake = True
        if body.Die_count >= 1.0:
            body.frame = 1
        if body.Die_count >= 1.2:
            body.frame = 2
        if body.Die_count >= 2.5:
            game_framework.change_state(game_over_state)
        body.invincibilitycount = 0

    def draw(body):
        body.image.clip_draw(body.frame * 58, 0, 58, 54, int(body.x), int(body.y))

next_state_table = {
    IdleState: {W_DOWN: One_RunState, A_DOWN: One_RunState, S_DOWN: One_RunState, D_DOWN: One_RunState,
                W_UP: One_RunState, A_UP: One_RunState, S_UP: One_RunState, D_UP: One_RunState,
                DOWN_DOWN: IdleState, RIGHT_DOWN: IdleState, UP_DOWN: IdleState, LEFT_DOWN: IdleState,
                Die: Die_State},
    One_RunState: {W_DOWN: Two_RunState, A_DOWN: Two_RunState, S_DOWN: Two_RunState, D_DOWN: Two_RunState,
                W_UP: IdleState, A_UP: IdleState, S_UP: IdleState, D_UP: IdleState,
                DOWN_DOWN: One_RunState, RIGHT_DOWN: One_RunState, UP_DOWN: One_RunState, LEFT_DOWN: One_RunState,
                Die: Die_State},
    Two_RunState: {W_DOWN: Three_RunState, A_DOWN: Three_RunState, S_DOWN: Three_RunState, D_DOWN: Three_RunState,
                W_UP: One_RunState, A_UP: One_RunState, S_UP: One_RunState, D_UP: One_RunState,
                DOWN_DOWN: Two_RunState, RIGHT_DOWN: Two_RunState, UP_DOWN: Two_RunState, LEFT_DOWN: Two_RunState,
                Die: Die_State},
    Three_RunState: {W_DOWN: Three_RunState, A_DOWN: Three_RunState, S_DOWN: Three_RunState, D_DOWN: Three_RunState,
                W_UP: Two_RunState, A_UP: Two_RunState, S_UP: Two_RunState, D_UP: Two_RunState,
                DOWN_DOWN: Three_RunState, RIGHT_DOWN: Three_RunState, UP_DOWN: Three_RunState, LEFT_DOWN: Three_RunState,
                Die: Die_State},
    Die_State: {W_DOWN: Die_State, A_DOWN: Die_State, S_DOWN: Die_State, D_DOWN: Die_State,
                W_UP: Die_State, A_UP: Die_State, S_UP: Die_State, D_UP: Die_State,
                DOWN_DOWN: Die_State, RIGHT_DOWN: Die_State, UP_DOWN: Die_State, LEFT_DOWN: Die_State,
                Die: Die_State}
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
        self.Die_count = 0
        self.Shake = False
        self.Shake_num = 0
        self.nowPos = 0
        self.now_floor = 1

    def next_floor(self, num):
        self.x = 800 // 2
        self.y = 600 // 2
        self.cur_state = IdleState
        self.velocity_x = 0
        self.velocity_y = 0
        self.nowPos = num

    def get_bb(self):
        return self.x - self.size_x // 2, self.y - self.size_y // 2, self.x + self.size_x // 2, self.y + self.size_y // 2

    def add_event(self, event):
        self.event_que.insert(0, event)

    def collision_obs(self):
        for Obs in game_world.Obs_objects():
            if isinstance(Obs, Obstacle.Obstacle_Rock) or isinstance(Obs, Tile.Tile_f):
                if collision.collide(self, Obs):
                    for all in game_world.Isaac_objects():
                        all.x -= all.Accel * all.velocity_x * game_framework.frame_time
                        all.y -= all.Accel * all.velocity_y * game_framework.frame_time
            if isinstance(Obs, Tile.Tile_n):
                if collision.collide(self, Obs):
                    if self.now_floor == 1:
                        game_world.remove_object(Obs)
                        game_framework.change_state(stage2_set_up)
                        self.now_floor = 2

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

        # 문과 충돌
        for door in game_world.Door_objects():
            if collision.collide(door, self):
                if server.Floor_1[self.nowPos]:
                    if self.y <= 100:
                        for me in game_world.Isaac_objects():
                            me.y += 450
                            me.x = 800 // 2
                            me.nowPos += 4
                    elif self.y >= 500:
                        for me in game_world.Isaac_objects():
                            me.y -= 450
                            me.x = 800 // 2
                            me.nowPos -= 4
                    elif self.x <= 100:
                        for me in game_world.Isaac_objects():
                            me.x += 650
                            if isinstance(me, Isaac_head):
                                me.y = (600 // 2) + 25
                            else:
                                me.y = 600 // 2
                            me.nowPos -= 1
                    elif self.x >= 700:
                        for me in game_world.Isaac_objects():
                            me.x -= 650
                            if isinstance(me, Isaac_head):
                                me.y = (600 // 2) + 25
                            else:
                                me.y = 600 // 2
                            me.nowPos += 1
            if server.Floor_2[self.nowPos]:
                if self.y <= 100:
                    for me in game_world.Isaac_objects():
                        me.y += 450
                        me.x = 800 // 2
                        me.nowPos += 6
                elif self.y >= 500:
                    for me in game_world.Isaac_objects():
                        me.y -= 450
                        me.x = 800 // 2
                        me.nowPos -= 6
                elif self.x <= 100:
                    for me in game_world.Isaac_objects():
                        me.x += 650
                        if isinstance(me, Isaac_head):
                            me.y = (600 // 2) + 25
                        else:
                            me.y = 600 // 2
                        me.nowPos -= 1
                elif self.x >= 700:
                    for me in game_world.Isaac_objects():
                        me.x -= 650
                        if isinstance(me, Isaac_head):
                            me.y = (600 // 2) + 25
                        else:
                            me.y = 600 // 2
                        me.nowPos += 1
        # 몹과 충돌
        for mob in game_world.Mob_objects():
            if not self.invincibility:
                if collision.up_collide(self, mob) or collision.down_collide(self, mob) or collision.left_collide(
                        self, mob) or \
                        collision.right_collide(self, mob) or collision.collide(self, mob):
                    for all in game_world.Isaac_objects():
                        all.invincibility = True
                        all.life -= 1
                    if collision.up_collide(self, mob):
                        for all in game_world.Isaac_objects():
                            all.y += RUN_SPEED_PPS // 3
                    elif collision.down_collide(self, mob):
                        for all in game_world.Isaac_objects():
                            all.y -= RUN_SPEED_PPS // 3
                    elif collision.left_collide(self, mob):
                        for all in game_world.Isaac_objects():
                            all.x -= RUN_SPEED_PPS // 3
                    else:
                        for all in game_world.Isaac_objects():
                            all.x += RUN_SPEED_PPS // 3
        # 몹의 눈물과의 충돌
        for tear in game_world.Mob_Tear_objects():
            if collision.collide(self, tear):
                game_world.remove_object(tear)
                if not self.invincibility:
                    for all in game_world.Isaac_objects():
                        all.invincibility = True
                        all.life -= 1

    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())
        #fill here

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
