import os
from pico2d import *
import game_world
import game_framework
import server
import collision
import Isaac_Body

os.chdir('d:/2DGP/Project/Sprite')

class Tile_1:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        if Tile_1.image == None:
            Tile_1.image = load_image('tile_1.png')

    def get_bb(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 100, 100, self.y * 100 + 50, (5 - self.x) * 100 + 50)

    def update(self):
        pass


class Tile_2(Tile_1):
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        if Tile_2.image == None:
            Tile_2.image = load_image('tile_2.png')


class Tile_3(Tile_1):
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        if Tile_3.image == None:
            Tile_3.image = load_image('tile_3.png')


class Tile_4(Tile_1):
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        if Tile_4.image == None:
            Tile_4.image = load_image('tile_4.png')


class Tile_5(Tile_1):
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        if Tile_5.image == None:
            Tile_5.image = load_image('tile_5.png')


class Tile_6(Tile_1):
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        if Tile_6.image == None:
            Tile_6.image = load_image('tile_6.png')


class Tile_7(Tile_1):
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        if Tile_7.image == None:
            Tile_7.image = load_image('tile_7.png')


class Tile_8(Tile_1):
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        if Tile_8.image == None:
            Tile_8.image = load_image('tile_8.png')


class Tile_9(Tile_1):
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        if Tile_9.image == None:
            Tile_9.image = load_image('tile_9.png')


class Tile_f(Tile_1):
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        if Tile_f.image == None:
            Tile_f.image = load_image('tile_f.png')

    def get_bb(self):
        return (self.y * 100 + 50) - 80 // 2, ((5 - self.x) * 100 + 50) - 80 // 2, \
               (self.y * 100 + 50) + 80 // 2, ((5 - self.x) * 100 + 50) + 80 // 2

    def draw(self):
        self.image.clip_draw(0, 0, 100, 100, self.y * 100 + 50, (5 - self.x) * 100 + 50)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass


class Tile_n(Tile_1):
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        if Tile_n.image == None:
            Tile_n.image = load_image('tile_n.png')

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.image.clip_draw(0, 0, 100, 100, self.x, self.y, 100, 100)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass