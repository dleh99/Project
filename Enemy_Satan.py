from pico2d import *
import game_world
import game_framework
import random

from Enemy_Tear import Enemy_tear

PIXEL_PER_METER = (1.0 / 0.033)     # 1px = 3.3cm

SATAN_REAL_SIZE_LENGHT_M = 2.0            # 적 가로 크기 2m
SATAN_REAL_SIZE_RAW_M = 2.0               # 적 세로 크기 2m
SATAN_PIXEL_SIZE_LENGHT = SATAN_REAL_SIZE_LENGHT_M * PIXEL_PER_METER      # 픽셀로 했을 때 길이
SATAN_PIXEL_SIZE_RAW = SATAN_REAL_SIZE_RAW_M * PIXEL_PER_METER

SPIDER_SPEED_MPS = (75.0 / 10.8)       # 50m = 3초 > 주인공보다 1.5배 빠름
SPIDER_SPEED_PPS = PIXEL_PER_METER * SPIDER_SPEED_MPS

ACTION_PER_TIME = 1.0 / 0.166         # 1초에 6번 움직임
FRAMES_PER_ACTION = 2

class Satan:
    image = None

    def __init__(self):
        if Satan.image == None:
            Satan.image = load_image('Satan.png')
        self.x, self.y, self.velocity = 800 // 2, 30, SPIDER_SPEED_PPS
        self.frame = 0
        self.pixel_x = SATAN_PIXEL_SIZE_LENGHT
        self.pixel_y = SATAN_PIXEL_SIZE_RAW
        self.size_x = 46
        self.size_y = 31
        self.switch = False
        self.reload = False
        self.attackcount = 0
        self.hp = 100

    def get_bb(self):
        return self.x - SATAN_PIXEL_SIZE_LENGHT // 2, self.y - SATAN_PIXEL_SIZE_RAW // 2,\
               self.x + SATAN_PIXEL_SIZE_LENGHT // 2, self.y + SATAN_PIXEL_SIZE_RAW // 2

    def draw(self):
        self.image.clip_draw(self.frame * self.size_x, 0, self.size_x, self.size_y, self.x, self.y, SATAN_PIXEL_SIZE_LENGHT, SATAN_PIXEL_SIZE_RAW)
        draw_rectangle(*self.get_bb())

    def update(self):
        if self.switch:
            self.x -= self.velocity * game_framework.frame_time
            if self.x <= 30 + SATAN_PIXEL_SIZE_LENGHT // 2:
                self.switch = False
        else:
            self.x += self.velocity * game_framework.frame_time
            if self.x >= 800 - 30 - SATAN_PIXEL_SIZE_LENGHT // 2:
                self.switch = True

        self.attackcount += game_framework.frame_time
        if self.attackcount >= 3:
            self.frame = 1
        if self.attackcount >= 4:
            self.frame = 2
            if not self.reload:
                tears = [Enemy_tear(self.x, self.y + 10, (i + 1)) for i in range(3)]
                game_world.add_objects(tears, 7)
                self.reload = True
        if self.attackcount >= 5:
            self.frame = 0
            self.attackcount = 0
            self.reload = False


