from pico2d import *
import game_world
import game_framework

PIXEL_PER_METER = (1.0 / 0.033)     # 1px = 3.3cm

DOOR_REAL_SIZE_LENGHT_M = 3.3            # 문 가로 크기 3.3m
DOOR_REAL_SIZE_RAW_M = 0.99               # 문 세로 크기 99m
DOOR_PIXEL_SIZE_LENGHT = DOOR_REAL_SIZE_LENGHT_M * PIXEL_PER_METER      # 픽셀로 했을 때 길이
DOOR_PIXEL_SIZE_RAW = DOOR_REAL_SIZE_RAW_M * PIXEL_PER_METER

class Door_ud:
    def __init__(self, x, y, image):
        self.x, self.y = x, y
        self.image = load_image(image)
        self.pixel_x = DOOR_PIXEL_SIZE_LENGHT
        self.pixel_y = DOOR_PIXEL_SIZE_RAW
        self.size_x = 100
        self.size_y = 30

    def get_bb(self):
        return self.x - DOOR_PIXEL_SIZE_LENGHT // 2, self.y - DOOR_PIXEL_SIZE_RAW // 2,\
               self.x + DOOR_PIXEL_SIZE_LENGHT // 2, self.y + DOOR_PIXEL_SIZE_RAW // 2

    def draw(self):
        self.image.clip_draw(0 , 0, self.size_x, self.size_y, self.x, self.y, DOOR_PIXEL_SIZE_LENGHT, DOOR_PIXEL_SIZE_RAW)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

