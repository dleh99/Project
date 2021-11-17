import random
from pico2d import *
import game_world
import game_framework
import random

PIXEL_PER_METER = (1.0 / 0.033)     # 1px = 3.3cm
ROCK_REAL_SIZE_LENGHT_M = 1.5            # 돌 가로 크기 1.5m
ROCK_REAL_SIZE_RAW_M = 1.5               # 돌 세로 크기 1.5m
ROCK_PIXEL_SIZE_LENGHT = ROCK_REAL_SIZE_LENGHT_M * PIXEL_PER_METER      # 픽셀로 했을 때 길이
ROCK_PIXEL_SIZE_RAW = ROCK_REAL_SIZE_RAW_M * PIXEL_PER_METER


class Obstacle_Rock:
    image = None

    def __init__(self):
        if Obstacle_Rock.image == None:
            Obstacle_Rock.image = load_image('Obstacle_1.png')
        self.x, self.y = 100, 100
        self.pixel_x = ROCK_REAL_SIZE_LENGHT_M
        self.pixel_y = ROCK_PIXEL_SIZE_RAW
        self.size_x = 120
        self.size_y = 124

    def get_bb(self):
        return self.x - ROCK_PIXEL_SIZE_LENGHT // 2, self.y - ROCK_PIXEL_SIZE_RAW // 2,\
               self.x + ROCK_PIXEL_SIZE_LENGHT // 2, self.y + ROCK_PIXEL_SIZE_RAW // 2

    def draw(self):
        self.image.clip_draw(0, 0, self.size_x, self.size_y, self.x, self.y, ROCK_PIXEL_SIZE_LENGHT, ROCK_PIXEL_SIZE_RAW)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

