import random
from pico2d import *
import game_world
import game_framework
import random

PIXEL_PER_METER = (1.0 / 0.033)     # 1px = 3.3cm
Item_REAL_SIZE_LENGHT_M = 1.5            # 아이템 가로 크기 1.5m
Item_REAL_SIZE_RAW_M = 1.5               # 아이템 세로 크기 1.5m
Item_PIXEL_SIZE_LENGHT = Item_REAL_SIZE_LENGHT_M * PIXEL_PER_METER      # 픽셀로 했을 때 길이
Item_PIXEL_SIZE_RAW = Item_REAL_SIZE_RAW_M * PIXEL_PER_METER


class Item_clasic:
    image = None

    def __init__(self):
        if Item_clasic.image == None:
            Item_clasic.image = load_image('Hp_item.png')
        self.x, self.y = 800 // 2, 600 // 2
        self.pixel_x = Item_PIXEL_SIZE_LENGHT
        self.pixel_y = Item_PIXEL_SIZE_RAW
        self.size_x = 100
        self.size_y = 100
        self.isUp = False

    def get_bb(self):
        return self.x - Item_PIXEL_SIZE_LENGHT // 2, self.y - Item_PIXEL_SIZE_RAW // 2,\
               self.x + Item_PIXEL_SIZE_LENGHT // 2, self.y + Item_PIXEL_SIZE_RAW // 2

    def draw(self):
        self.image.clip_draw(0, 0, self.size_x, self.size_y, self.x, self.y, Item_PIXEL_SIZE_LENGHT, Item_PIXEL_SIZE_RAW)
        draw_rectangle(*self.get_bb())

    def update(self):
        if self.isUp:
            self.y += 0.1
            if self.y >= (600 // 2) + 10:
                self.isUp = False
        else:
            self.y -= 0.1
            if self.y <= (600 // 2) - 10:
                self.isUp = True

