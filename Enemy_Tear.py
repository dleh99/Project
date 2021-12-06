import random
from pico2d import *
import game_world
import game_framework

PIXEL_PER_METER = (1.0 / 0.033)     # 1px = 33cm
TEAR_SPEED_MPS = (50.0 / 4.32)       # 50m = 3초 > 주인공보다 약 2.5배 빠름
TEAR_SPEED_PPS = PIXEL_PER_METER * TEAR_SPEED_MPS

class Enemy_tear:
    image = None

    def __init__(self, x = 400, y = 300, dir = 1):
        if Enemy_tear.image == None:
            Enemy_tear.image = load_image('Enemy_Tear.png')
        self.x, self.y, self.velocity, self.dir = x, y, TEAR_SPEED_PPS, dir

    def get_bb(self):
        return self.x - 8, self.y - 8, self.x + 8, self.y + 8

    def draw(self):
        self.image.clip_draw(0, 0, 10, 10, self.x, self.y, 16, 16)
        draw_rectangle(*self.get_bb())

    def update(self):
        if self.dir == 1:
            self.x -= self.velocity * game_framework.frame_time
            self.y += self.velocity * game_framework.frame_time
        elif self.dir == 2:
            self.y += self.velocity * game_framework.frame_time
        elif self.dir == 3:
            self.x += self.velocity * game_framework.frame_time
            self.y += self.velocity * game_framework.frame_time
        elif self.dir == 4:
            self.x += self.velocity * game_framework.frame_time
        elif self.dir == 5:
            self.x += self.velocity * game_framework.frame_time
            self.y -= self.velocity * game_framework.frame_time
        elif self.dir == 6:
            self.y -= self.velocity * game_framework.frame_time
        elif self.dir == 7:
            self.x -= self.velocity * game_framework.frame_time
            self.y -= self.velocity * game_framework.frame_time
        elif self.dir == 8:
            self.x -= self.velocity * game_framework.frame_time
        self.velocity -= 0.5
        if self.velocity <= 0.0:
            game_world.remove_object(self)
        if self.x - 35 <= 0 or self.x + 35 >= 800 or self.y - 35 <= 0 or self.y + 35 >= 600:
            game_world.remove_object(self)


