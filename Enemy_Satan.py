from pico2d import *
import game_world
import game_framework
import random

PIXEL_PER_METER = (1.0 / 0.033)     # 1px = 3.3cm

SATAN_REAL_SIZE_LENGHT_M = 1.5            # 적 가로 크기 1.5m
SATAN_REAL_SIZE_RAW_M = 1.5               # 적 세로 크기 1.5m
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
        self.x, self.y, self.velocity = random.randint(100, 700), random.randint(100, 500), SPIDER_SPEED_PPS
        self.frame = 0
        self.pixel_x = SATAN_PIXEL_SIZE_LENGHT
        self.pixel_y = SATAN_PIXEL_SIZE_RAW
        self.size_x = 46
        self.size_y = 31
        self.switch = False
        self.hp = 100

    def get_bb(self):
        return self.x - SATAN_PIXEL_SIZE_LENGHT // 2, self.y - SATAN_PIXEL_SIZE_RAW // 2,\
               self.x + SATAN_PIXEL_SIZE_LENGHT // 2, self.y + SATAN_PIXEL_SIZE_RAW // 2

    def draw(self):
        self.image.clip_draw(int(self.frame) * self.size_x, 0, self.size_x, self.size_y, self.x, self.y, SATAN_PIXEL_SIZE_LENGHT, SATAN_PIXEL_SIZE_RAW)
        draw_rectangle(*self.get_bb())
        # fill here for draw

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

