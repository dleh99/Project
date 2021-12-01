import random
from pico2d import *
import game_world
import game_framework
import random
import server
import collision

PIXEL_PER_METER = (1.0 / 0.033)     # 1px = 3.3cm

SPIDER_REAL_SIZE_LENGHT_M = 1.1            # 적 가로 크기 1.1m
SPIDER_REAL_SIZE_RAW_M = 1.0               # 적 세로 크기 1m
SPIDER_PIXEL_SIZE_LENGHT = SPIDER_REAL_SIZE_LENGHT_M * PIXEL_PER_METER      # 픽셀로 했을 때 길이
SPIDER_PIXEL_SIZE_RAW = SPIDER_REAL_SIZE_RAW_M * PIXEL_PER_METER

SPIDER_SPEED_MPS = (75.0 / 10.8)       # 50m = 3초 > 주인공보다 1.5배 빠름
SPIDER_SPEED_PPS = PIXEL_PER_METER * SPIDER_SPEED_MPS

ACTION_PER_TIME = 1.0 / 0.166         # 1초에 6번 움직임
FRAMES_PER_ACTION = 2

class Red_Spider:
    image = None

    def __init__(self):
        if Red_Spider.image == None:
            Red_Spider.image = load_image('red_spider.png')
        self.x, self.y, self.velocity = random.randint(100, 700), random.randint(100, 500), SPIDER_SPEED_PPS
        self.frame = 0
        self.pixel_x = SPIDER_PIXEL_SIZE_LENGHT
        self.pixel_y = SPIDER_PIXEL_SIZE_RAW
        self.size_x = 110
        self.size_y = 80
        self.hp = 50

    def get_bb(self):
        return self.x - SPIDER_PIXEL_SIZE_LENGHT // 2, self.y - SPIDER_PIXEL_SIZE_RAW // 2,\
               self.x + SPIDER_PIXEL_SIZE_LENGHT // 2, self.y + SPIDER_PIXEL_SIZE_RAW // 2

    def draw(self):
        self.image.clip_draw(int(self.frame) * self.size_x, 0, self.size_x, self.size_y, self.x, self.y, SPIDER_PIXEL_SIZE_LENGHT, SPIDER_PIXEL_SIZE_RAW)
        draw_rectangle(*self.get_bb())
        # fill here for draw

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        # 눈물과 충돌 체크
        for tear in game_world.Tear_objects():
            if collision.collide(self, tear):
                game_world.remove_object(tear)
                self.hp -= tear.power
                if self.hp <= 0:
                    game_world.remove_object(self)

        for isaac in game_world.Isaac_objects():
            if abs(isaac.x - self.x) > 100:
                self.x += (isaac.x - self.x) / 1000
            else:
                self.x += (isaac.x - self.x) / 400
            if abs(isaac.y - self.y) > 100:
                self.y += (isaac.y - self.y) / 1000
            else:
                self.y += (isaac.y - self.y) / 400
            self.x = clamp(self.pixel_x // 2, self.x, 800 - self.pixel_x // 2)
            self.y = clamp(self.pixel_y // 2, self.y, 600 - (self.pixel_y // 2))


