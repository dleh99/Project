import random
from pico2d import *
import game_world
import game_framework
import random
import server
import collision
import Isaac_Body

PIXEL_PER_METER = (1.0 / 0.033)     # 1px = 3.3cm
ROCK_REAL_SIZE_LENGHT_M = 1.5            # 돌 가로 크기 1.5m
ROCK_REAL_SIZE_RAW_M = 1.5               # 돌 세로 크기 1.5m
ROCK_PIXEL_SIZE_LENGHT = ROCK_REAL_SIZE_LENGHT_M * PIXEL_PER_METER      # 픽셀로 했을 때 길이
ROCK_PIXEL_SIZE_RAW = ROCK_REAL_SIZE_RAW_M * PIXEL_PER_METER

STING_REAL_SIZE_LENGHT_M = 2.5           # 가시 가로 크기 2.5m
STING_REAL_SIZE_RAW_M = 2.5              # 가시 세로 크기 2.5m
STING_PIXEL_SIZE_LENGHT = STING_REAL_SIZE_LENGHT_M * PIXEL_PER_METER
STING_PIXEL_SIZE_RAW = STING_REAL_SIZE_RAW_M * PIXEL_PER_METER


class Obstacle_Rock:
    image = None

    def __init__(self, x, y):
        if Obstacle_Rock.image == None:
            Obstacle_Rock.image = load_image('Obstacle_1.png')
        self.x, self.y = x, y
        self.pixel_x = ROCK_PIXEL_SIZE_LENGHT
        self.pixel_y = ROCK_PIXEL_SIZE_RAW
        self.size_x = 120
        self.size_y = 124

    def get_bb(self):
        return self.x - self.pixel_x // 2, self.y - self.pixel_y // 2,\
               self.x + self.pixel_x // 2, self.y + self.pixel_y // 2

    def draw(self):
        self.image.clip_draw(0, 0, self.size_x, self.size_y, self.x, self.y, self.pixel_x, self.pixel_y)
        draw_rectangle(*self.get_bb())

    def update(self):
        # print(self.pixel_x, self.pixel_y)
        for tear in game_world.Tear_objects():
            if collision.collide(tear, self):
                game_world.remove_object(tear)
        for enemy_tear in game_world.Mob_Tear_objects():
            if collision.collide(enemy_tear, self):
                game_world.remove_object(enemy_tear)

class Obstacle_Sting:
    image = None

    def __init__(self, x, y, num):
        if Obstacle_Sting.image == None:
            Obstacle_Sting.image = load_image('Obs_Son.png')
        self.x, self.y = x, y
        self.pixel_x = STING_PIXEL_SIZE_LENGHT
        self.pixel_y = STING_PIXEL_SIZE_RAW
        self.size_x = 100
        self.size_y = 100
        self.isOn = True
        self.On_Timer = num

    def get_bb(self):
        return self.x - self.pixel_x // 2, self.y - self.pixel_y // 2, \
               self.x + self.pixel_x // 2, self.y + self.pixel_y // 2

    def draw(self):
        self.image.clip_draw(0, 0, self.size_x, self.size_y, self.x, self.y, self.pixel_x, self.pixel_y)
        draw_rectangle(*self.get_bb())

    def update(self):
        # print(self.pixel_x, self.pixel_y)
        self.On_Timer += game_framework.frame_time
        if 0.0 <= self.On_Timer < 2.0:
            self.isOn = True
        if 2.0 <= self.On_Timer < 4.0:
            self.isOn = False
        if self.On_Timer >= 4.0:
            self.On_Timer = 0.0
        if self.isOn:
            self.image = load_image('Obs_Son.png')
            for isaac in game_world.Isaac_objects():
                if isinstance(isaac, Isaac_Body.Isaac_body):
                    if not isaac.invincibility:
                        if collision.up_collide(isaac, self) or collision.down_collide(isaac, self) or\
                                collision.left_collide(isaac, self) or collision.right_collide(isaac, self) or collision.collide(isaac, self):
                            for all in game_world.Isaac_objects():
                                all.invincibility = True
                                all.life -= 1
                            if collision.up_collide(isaac, self):
                                for all in game_world.Isaac_objects():
                                    all.y += Isaac_Body.RUN_SPEED_PPS // 3
                            elif collision.down_collide(isaac, self):
                                for all in game_world.Isaac_objects():
                                    all.y -= Isaac_Body.RUN_SPEED_PPS // 3
                            elif collision.left_collide(isaac, self):
                                for all in game_world.Isaac_objects():
                                    all.x -= Isaac_Body.RUN_SPEED_PPS // 3
                            else:
                                for all in game_world.Isaac_objects():
                                    all.x += Isaac_Body.RUN_SPEED_PPS // 3
        else:
            self.image = load_image('Obs_Soff.png')

