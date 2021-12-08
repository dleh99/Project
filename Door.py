from pico2d import *
import game_world
import game_framework

PIXEL_PER_METER = (1.0 / 0.033)     # 1px = 3.3cm

DOOR_REAL_SIZE_LENGHT_M = 0.99            # 문 가로 크기 99cm
DOOR_REAL_SIZE_RAW_M = 3.3               # 문 세로 크기 3.3m
DOOR_PIXEL_SIZE_LENGHT = DOOR_REAL_SIZE_LENGHT_M * PIXEL_PER_METER      # 픽셀로 했을 때 길이
DOOR_PIXEL_SIZE_RAW = DOOR_REAL_SIZE_RAW_M * PIXEL_PER_METER

class Door_left:
    image = None
    def __init__(self, x, y):
        self.x, self.y = x, y
        if Door_left.image == None:
            Door_left.image = load_image('Door_6.png')
        self.pixel_x = DOOR_PIXEL_SIZE_LENGHT
        self.pixel_y = DOOR_PIXEL_SIZE_RAW
        self.size_x = 30
        self.size_y = 100

    def get_bb(self):
        return self.x - DOOR_PIXEL_SIZE_LENGHT // 2, self.y - DOOR_PIXEL_SIZE_RAW // 2,\
               self.x + DOOR_PIXEL_SIZE_LENGHT // 2, self.y + DOOR_PIXEL_SIZE_RAW // 2

    def draw(self):
        self.image.clip_draw(0 , 0, self.size_x, self.size_y, self.x, self.y, DOOR_PIXEL_SIZE_LENGHT, DOOR_PIXEL_SIZE_RAW)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass


class Door_right(Door_left):
    image = None
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.size_x = 30
        self.size_y = 100
        if Door_right.image == None:
            Door_right.image = load_image('Door_5.png')


class Door_Up:
    image = None
    def __init__(self, x, y):
        self.x, self.y = x, y
        if Door_Up.image == None:
            Door_Up.image = load_image('Door_8.png')
        self.pixel_x = DOOR_PIXEL_SIZE_RAW
        self.pixel_y = DOOR_PIXEL_SIZE_LENGHT
        self.size_x = 100
        self.size_y = 30

    def get_bb(self):
        return self.x - DOOR_PIXEL_SIZE_RAW // 2, self.y - DOOR_PIXEL_SIZE_LENGHT // 2, \
               self.x + DOOR_PIXEL_SIZE_RAW // 2, self.y + DOOR_PIXEL_SIZE_LENGHT // 2

    def draw(self):
        self.image.clip_draw(0, 0, self.size_x, self.size_y, self.x, self.y, DOOR_PIXEL_SIZE_RAW,
                             DOOR_PIXEL_SIZE_LENGHT)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass


class Door_Down(Door_Up):
    image = None
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.size_x = 100
        self.size_y = 30
        if Door_Down.image == None:
            Door_Down.image = load_image('Door_7.png')


class Gold_Left(Door_left):
    image = None
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.size_x = 30
        self.size_y = 100
        if Gold_Left.image == None:
            Gold_Left.image = load_image('Door_G6.png')


class Gold_Right(Door_left):
    image = None
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.size_x = 30
        self.size_y = 100
        if Gold_Right.image == None:
            Gold_Right.image = load_image('Door_G5.png')


class Gold_Up(Door_Up):
    image = None
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.size_x = 100
        self.size_y = 30
        if Gold_Up.image == None:
            Gold_Up.image = load_image('Door_G8.png')


class Gold_Down(Door_Up):
    image = None
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.size_x = 100
        self.size_y = 30
        if Gold_Down.image == None:
            Gold_Down.image = load_image('Door_G7.png')