import os
import game_framework
from pico2d import *
from Isaac_Tear import Isaac_tear
import server
import collision

from Isaac_Tear import Isaac_tear
from Item import *

import game_world

os.chdir('d:/2DGP/Project/Sprite')

PIXEL_PER_METER = (1.0 / 0.033) # 1px = 3.3 cm
RUN_SPEED_MPS = 60.0 / 10.8     # 60m per 10.8 sec
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
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
        if event == DOWN_DOWN:
            head.dir = 1
            head.fire_tear()
        elif event == RIGHT_DOWN:
            head.dir = 2
            head.fire_tear()
        elif event == UP_DOWN:
            head.dir = 3
            head.fire_tear()
        elif event == LEFT_DOWN:
            head.dir = 4
            head.fire_tear()

    def do(head):
        head.frame = (head.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        if head.life <= 0:
            head.add_event(Die)

    def draw(head):
        if head.life > 0:
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
        if event == DOWN_DOWN:
            head.dir = 1
            head.fire_tear()
        elif event == RIGHT_DOWN:
            head.dir = 2
            head.fire_tear()
        elif event == UP_DOWN:
            head.dir = 3
            head.fire_tear()
        elif event == LEFT_DOWN:
            head.dir = 4
            head.fire_tear()

    def do(head):
        head.x += head.Accel * head.velocity_x * game_framework.frame_time
        head.y += head.Accel * head.velocity_y * game_framework.frame_time
        head.x = clamp(30 + head.size_x // 2, head.x, 800 - 30 - head.size_x // 2)
        head.y = clamp(30 + head.size_y // 2 + 17, head.y, 600 - 30 - head.size_y // 2)
        if head.life <= 0:
            head.add_event(Die)

    def draw(head):
        if head.life > 0:
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
        if event == DOWN_DOWN:
            head.dir = 1
            head.fire_tear()
        elif event == RIGHT_DOWN:
            head.dir = 2
            head.fire_tear()
        elif event == UP_DOWN:
            head.dir = 3
            head.fire_tear()
        elif event == LEFT_DOWN:
            head.dir = 4
            head.fire_tear()

    def do(head):
        head.x += head.Accel * head.velocity_x * game_framework.frame_time
        head.y += head.Accel * head.velocity_y * game_framework.frame_time
        head.x = clamp(30 + head.size_x // 2, head.x, 800 - 30 - head.size_x // 2)
        head.y = clamp(30 + head.size_y // 2 + 17, head.y, 600 - 30 - head.size_y // 2)
        if head.life <= 0:
            head.add_event(Die)

    def draw(head):
        if head.life > 0:
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
        if event == DOWN_DOWN:
            head.dir = 1
            head.fire_tear()
        elif event == RIGHT_DOWN:
            head.dir = 2
            head.fire_tear()
        elif event == UP_DOWN:
            head.dir = 3
            head.fire_tear()
        elif event == LEFT_DOWN:
            head.dir = 4
            head.fire_tear()

    def do(head):
        head.x += head.Accel * head.velocity_x * game_framework.frame_time
        head.y += head.Accel * head.velocity_y * game_framework.frame_time
        head.x = clamp(30 + head.size_x // 2, head.x, 800 - 30 - head.size_x // 2)
        head.y = clamp(30 +head.size_y // 2 + 17, head.y, 600 - 30 - head.size_y // 2)
        if head.life <= 0:
            head.add_event(Die)

    def draw(head):
        if head.life > 0:
            if head.dir == 1:
                head.image.clip_draw(0 * head.size_x, 0, head.size_x, head.size_y, head.x, head.y)
            elif head.dir == 2:
                head.image.clip_draw(2 * head.size_x, 0, head.size_x, head.size_y, head.x, head.y)
            elif head.dir == 3:
                head.image.clip_draw(4 * head.size_x, 0, head.size_x, head.size_y, head.x, head.y)
            elif head.dir == 4:
                head.image.clip_draw(6 * head.size_x, 0, head.size_x, head.size_y, head.x, head.y)

class Die_State:

    def enter(body, event):
        body.velocity_x = 0
        body.velocity_y = 0
        body.invincibility = True
        body.dead()

    def exit(body, event):
        pass

    def do(body):
        body.invincibilitycount = 0

    def draw(body):
        pass

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

class Isaac_head:

    def __init__(self):
        self.image = load_image('Isaac_Head.png')
        self.Time_font = load_font('ENCR10B.TTF', 30)
        self.Score_font = load_font('ENCR10B.TTF', 20)
        self.dir = 1                # 1 = ??????, 2 = ?????????, 3 = ???, 4 = ??????
        self.frame = 0
        self.velocity_x = 0
        self.velocity_y = 0
        self.Accel = 2.0
        self.x = 800 // 2
        self.y = 600 // 2 + 25
        self.size_x = 45
        self.size_y = 42
        self.life = 1
        self.invincibility = True
        self.invincibilitycount = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.Heart = load_image('heart.png')
        self.nowPos = 0
        self.delay_num = 0
        self.item_delay = 0
        self.power = 10
        self.start_time = get_time()
        self.Score = 100
        self.now_floor = 1
        self.dead_sound = load_wav('Isaac_dead.wav')
        self.hurt_sound = load_wav('Isaac_hurt.wav')
        self.tear_sound = load_wav('tear_fire.wav')
        self.open_door = load_wav('door_open.wav')
        self.dead_sound.set_volume(50)
        self.tear_sound.set_volume(100)
        self.hurt_sound.set_volume(30)
        self.open_door.set_volume(50)

    def get_bb(self):
        return self.x - self.size_x // 2, self.y - self.size_y // 2, self.x + self.size_x // 2, self.y + self.size_y // 2

    def open(self):
        self.open_door.play()

    def dead(self):
        self.dead_sound.play()

    def hurt(self):
        self.hurt_sound.play()

    def next_floor(self, num):
        self.x = 800 // 2
        self.y = 600 // 2 + 25
        self.cur_state = IdleState
        self.velocity_x = 0
        self.velocity_y = 0
        self.nowPos = num

    def fire_tear(self):
        if self.delay_num + self.item_delay >= 150:
            self.delay_num = 0
            self.tear_sound.play()
            tear = Isaac_tear(self.x, self.y, self.dir, self.power)
            game_world.add_object(tear, server.Tear_num)


    def add_event(self, event):
        self.event_que.insert(0, event)


    def update(self):
        if self.life <= 0:
            self.image = None
        # ?????? ?????? ????????? ?????? ?????????
        self.delay_num += 1
        if self.nowPos == 1:
            if self.invincibility:
                self.invincibilitycount += 1
                if self.invincibilitycount == 1000:
                    self.invincibility = False
                    self.invincibilitycount = 0
        else:
            self.invincibility = True
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)
        # print(self.now_floor, self.nowPos, server.isaac_body.now_floor, server.isaac_body.nowPos)

        # ?????? ??????
        for door in game_world.Door_objects():
            if collision.collide(door, self):
                if self.now_floor == 1:
                    if server.Floor_1[self.nowPos]:
                        self.open()
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
                elif self.now_floor == 2:
                    if server.Floor_2[self.nowPos]:
                        self.open()
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
        # ?????? ??????                    
        for mob in game_world.Mob_objects():
            if not self.invincibility:
                if collision.up_collide(self, mob) or collision.down_collide(self, mob) or collision.left_collide(
                        self, mob) or \
                        collision.right_collide(self, mob) or collision.collide(self, mob):
                    self.hurt()
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
        # ?????? ???????????? ??????                    
        for tear in game_world.Mob_Tear_objects():
            if collision.collide(self, tear):
                game_world.remove_object(tear)
                self.hurt()
                if not self.invincibility:
                    for all in game_world.Isaac_objects():
                        all.invincibility = True
                        all.life -= 1

    def draw(self):
        self.cur_state.draw(self)
        for i in range(self.life):
            self.Heart.clip_draw(0, 0, 50, 50, 30 * i + 30, 560, 30, 30)
        # draw_rectangle(*self.get_bb())
        self.Time_font.draw((800 // 2) - 105, 600 - 30, 'Time : %3.2f' % (get_time() - self.start_time), (255, 255, 255))
        self.Score_font.draw((800 // 2) - 60, 600 - 60, 'Score : %0.f' % (- get_time() + self.start_time + self.Score), (255, 255, 255))
        #fill here


    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
