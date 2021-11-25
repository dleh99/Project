from pico2d import *
import game_world
import game_framework

class Tile:
    def __init__(self, x, y, image):
        self.x, self.y = x, y
        self.image = load_image(image)
        self.size_x = 30
        self.size_y = 100

    def get_bb(self):
        pass

    def draw(self):
        pass

    def update(self):
        pass

