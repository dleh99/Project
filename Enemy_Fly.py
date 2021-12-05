import random
from pico2d import *
import game_world
import game_framework
import random
import server
import collision

PIXEL_PER_METER = (1.0 / 0.033)     # 1px = 3.3cm

Fly_REAL_SIZE_LENGHT_M = 1.0            # 적 가로 크기 1.0m
Fly_REAL_SIZE_RAW_M = 1.0               # 적 세로 크기 1m
Fly_PIXEL_SIZE_LENGHT = Fly_REAL_SIZE_LENGHT_M * PIXEL_PER_METER      # 픽셀로 했을 때 길이
Fly_PIXEL_SIZE_RAW = Fly_REAL_SIZE_RAW_M * PIXEL_PER_METER

Fly_SPEED_MPS = (50.0 / 10.8)       # 50m = 3초 > 주인공보다 1.0배 빠름
Fly_SPEED_PPS = PIXEL_PER_METER * Fly_SPEED_MPS

ACTION_PER_TIME = 1.0 / 0.05         # 1초에 20번 움직임
FRAMES_PER_ACTION = 2

class Fly:
    image = None

    def __init__(self):
        if Fly.image == None:
            Fly.image = load_image('Fly.png')
        self.x, self.y, self.velocity = random.randint(100, 700), random.randint(100, 500), Fly_SPEED_PPS
        self.frame = 0
        self.pixel_x = Fly_PIXEL_SIZE_LENGHT
        self.pixel_y = Fly_PIXEL_SIZE_RAW
        self.size_x = 110
        self.size_y = 80
        self.hp = 30
        self.dir = random.random() * 2 * math.pi

    def get_bb(self):
        return self.x - Fly_PIXEL_SIZE_LENGHT // 2, self.y - Fly_PIXEL_SIZE_RAW // 2,\
               self.x + Fly_PIXEL_SIZE_LENGHT // 2, self.y + Fly_PIXEL_SIZE_RAW // 2

    def draw(self):
        self.image.clip_draw(int(self.frame) * self.size_x, 0, self.size_x, self.size_y, self.x, self.y, Fly_PIXEL_SIZE_LENGHT, Fly_PIXEL_SIZE_RAW)
        draw_rectangle(*self.get_bb())
        # fill here for draw

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2

        self.dir = math.atan2(server.isaac_body.y - self.y, server.isaac_body.x - self.x)
        self.x += self.velocity * math.cos(self.dir) * game_framework.frame_time
        self.y += self.velocity * math.sin(self.dir) * game_framework.frame_time
        self.x = clamp(self.pixel_x // 2, self.x, 800 - self.pixel_x // 2)
        self.y = clamp(self.pixel_y // 2, self.y, 600 - (self.pixel_y // 2))
        # 눈물과 충돌 체크
        for tear in game_world.Tear_objects():
            if collision.collide(self, tear):
                game_world.remove_object(tear)
                self.hp -= tear.power
                if self.hp <= 0:
                    game_world.remove_object(self)


