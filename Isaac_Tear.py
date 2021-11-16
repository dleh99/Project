import random
from pico2d import *
import game_world
import game_framework

class Isaac_tear:
    image = None

    def __init__(self):
        if Isaac_tear.image == None:
            Isaac_tear.image = load_image('Isaac_Tear.png')
        self.x, self.y, self.velocity = random.randint(0, 1600-1), 60, 0

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())
        # fill here for draw

    def update(self):
        self.x += self.velocity * game_framework.frame_time

    #fill here for def stop
    def stop(self):
        self.fall_speed = 0

