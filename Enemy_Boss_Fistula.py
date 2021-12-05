import random
from pico2d import *
import game_world
import game_framework
import random
import server
import collision

PIXEL_PER_METER = (1.0 / 0.033)     # 1px = 3.3cm

FISTULA_REAL_SIZE_LENGHT_M = 6.0            # 적 가로 크기 6m
FISTULA_REAL_SIZE_RAW_M = 6.0               # 적 세로 크기 6m
FISTULA_PIXEL_SIZE_LENGHT = FISTULA_REAL_SIZE_LENGHT_M * PIXEL_PER_METER      # 픽셀로 했을 때 길이
FISTULA_PIXEL_SIZE_RAW = FISTULA_REAL_SIZE_RAW_M * PIXEL_PER_METER

FISTULA_Pase_1_SPEED_MPS = (50.0 / 10.8)       # 50m = 3초 > 주인공보다 1.0배 빠름
FISTULA_Pase_1_SPEED_PPS = PIXEL_PER_METER * FISTULA_Pase_1_SPEED_MPS

ACTION_PER_TIME = 1.0 / 0.166         # 1초에 6번 움직임
FRAMES_PER_ACTION = 2

class Fistula_pase_1:
    image = None

    def __init__(self):
        if Fistula_pase_1.image == None:
            Fistula_pase_1.image = load_image('Fistula 1.png')
        self.x, self.y, self.velocity = random.randint(100, 700), random.randint(100, 500), FISTULA_Pase_1_SPEED_PPS
        self.frame = 0
        self.pixel_x = FISTULA_PIXEL_SIZE_LENGHT
        self.pixel_y = FISTULA_PIXEL_SIZE_RAW
        self.size_x = 80
        self.size_y = 80
        self.hp = 150
        self.dir = 2
        self.timer = 0

    def get_bb(self):
        return self.x - self.pixel_x // 2, self.y - self.pixel_y // 2,\
               self.x + self.pixel_x // 2, self.y + self.pixel_y // 2

    def draw(self):
        self.image.clip_draw(int(self.frame) * self.size_x, 0, self.size_x, self.size_y, self.x, self.y, self.pixel_x, self.pixel_y)
        draw_rectangle(*self.get_bb())
        # fill here for draw

    def update(self):
        self.timer += game_framework.frame_time

        if self.timer % 10 == 0:
            self.timer = 0
            self.velocity *= 1.2
        if self.dir == 1:
            self.x -= self.velocity * game_framework.frame_time
            self.y += self.velocity * game_framework.frame_time
            if self.x <= 30 + self.pixel_x // 2:
                self.dir = 2
            if self.y >= 570 - self.pixel_y // 2:
                self.dir = 4
        elif self.dir == 2:
            self.x += self.velocity * game_framework.frame_time
            self.y += self.velocity * game_framework.frame_time
            if self.x >= 770 - self.pixel_x // 2:
                self.dir = 1
            if self.y >= 570 - self.pixel_y // 2:
                self.dir = 3
        elif self.dir == 3:
            self.x += self.velocity * game_framework.frame_time
            self.y -= self.velocity * game_framework.frame_time
            if self.x >= 770 - self.pixel_x // 2:
                self.dir = 4
            if self.y <= 30 + self.pixel_y // 2:
                self.dir = 2
        elif self.dir == 4:
            self.x -= self.velocity * game_framework.frame_time
            self.y -= self.velocity * game_framework.frame_time
            if self.x <= 30 + self.pixel_x // 2:
                self.dir = 3
            if self.y <= 30 + self.pixel_y // 2:
                self.dir = 1

        # 눈물과 충돌 체크
        for tear in game_world.Tear_objects():
            if collision.collide(self, tear):
                game_world.remove_object(tear)
                self.hp -= tear.power
                if self.hp <= 0:
                    game_world.remove_object(self)

class Fistula_pase_2(Fistula_pase_1):
    image = None

    def __init__(self):
        if Fistula_pase_1.image == None:
            Fistula_pase_1.image = load_image('Fistula 2.png')
        self.x, self.y, self.velocity = random.randint(100, 700), random.randint(100, 500), FISTULA_Pase_1_SPEED_PPS
        self.frame = 0
        self.pixel_x = FISTULA_PIXEL_SIZE_LENGHT
        self.pixel_y = FISTULA_PIXEL_SIZE_RAW
        self.size_x = 80
        self.size_y = 80
        self.hp = 150
        self.dir = 2
        self.timer = 0

    def get_bb(self):
        return self.x - self.pixel_x // 2, self.y - self.pixel_y // 2,\
               self.x + self.pixel_x // 2, self.y + self.pixel_y // 2

    def draw(self):
        self.image.clip_draw(int(self.frame) * self.size_x, 0, self.size_x, self.size_y, self.x, self.y, self.pixel_x, self.pixel_y)
        draw_rectangle(*self.get_bb())
        # fill here for draw

    def update(self):
        self.timer += game_framework.frame_time

        if self.timer % 10 == 0:
            self.timer = 0
            self.velocity *= 1.2
        if self.dir == 1:
            self.x -= self.velocity * game_framework.frame_time
            self.y += self.velocity * game_framework.frame_time
            if self.x <= 30 + self.pixel_x // 2:
                self.dir = 2
            if self.y >= 570 - self.pixel_y // 2:
                self.dir = 4
        elif self.dir == 2:
            self.x += self.velocity * game_framework.frame_time
            self.y += self.velocity * game_framework.frame_time
            if self.x >= 770 - self.pixel_x // 2:
                self.dir = 1
            if self.y >= 570 - self.pixel_y // 2:
                self.dir = 3
        elif self.dir == 3:
            self.x += self.velocity * game_framework.frame_time
            self.y -= self.velocity * game_framework.frame_time
            if self.x >= 770 - self.pixel_x // 2:
                self.dir = 4
            if self.y <= 30 + self.pixel_y // 2:
                self.dir = 2
        elif self.dir == 4:
            self.x -= self.velocity * game_framework.frame_time
            self.y -= self.velocity * game_framework.frame_time
            if self.x <= 30 + self.pixel_x // 2:
                self.dir = 3
            if self.y <= 30 + self.pixel_y // 2:
                self.dir = 1

        # 눈물과 충돌 체크
        for tear in game_world.Tear_objects():
            if collision.collide(self, tear):
                game_world.remove_object(tear)
                self.hp -= tear.power
                if self.hp <= 0:
                    game_world.remove_object(self)