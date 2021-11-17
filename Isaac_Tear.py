import random
from pico2d import *
import game_world
import game_framework

PIXEL_PER_METER = (1.0 / 0.033)     # 1px = 33cm
TEAR_SPEED_MPS = (50.0 / 3.0)       # 50m = 3초 > 주인공보다 약 3배 빠름
TEAR_SPEED_PPS = PIXEL_PER_METER * TEAR_SPEED_MPS

class Isaac_tear:
    image = None

    def __init__(self, x = 400, y = 300, dir = 1):
        if Isaac_tear.image == None:
            Isaac_tear.image = load_image('Isaac_Tear.png')
        self.x, self.y, self.velocity, self.dir = x, y, TEAR_SPEED_PPS, dir
        self.power = 10

    def get_bb(self):
        return self.x - 5, self.y - 5, self.x + 5, self.y + 5

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())
        # fill here for draw

    def update(self):
        if self.dir == 1:
            self.y -= self.velocity * game_framework.frame_time
        elif self.dir == 2:
            self.x += self.velocity * game_framework.frame_time
        elif self.dir == 3:
            self.y += self.velocity * game_framework.frame_time
        elif self.dir == 4:
            self.x -= self.velocity * game_framework.frame_time
        self.velocity -= 1.0
        if self.velocity <= 0.0:
            game_world.remove_object(self)
        if self.x - 5 <= 0 or self.x + 5 >= 800 or self.y - 5 <= 0 or self.y + 5 >= 600:
            game_world.remove_object(self)

    #fill here for def stop
    def stop(self):
        self.fall_speed = 0

