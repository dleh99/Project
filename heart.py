from pico2d import *
import game_world
import game_framework

class Isaac_heart:
    image = None

    def __init__(self, x = 400, y = 300):
        if Isaac_heart.image == None:
            Isaac_heart.image = load_image('heart.png')
        self.x, self.y = x * 50, y

    def get_bb(self):
        pass

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
        # fill here for draw


