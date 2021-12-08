from pico2d import *
import game_world
import game_framework
import random
import server
import collision

from Enemy_Tear import Enemy_tear

PIXEL_PER_METER = (1.0 / 0.033)     # 1px = 3.3cm

SATAN_REAL_SIZE_LENGHT_M = 2.0            # 적 가로 크기 2m
SATAN_REAL_SIZE_RAW_M = 2.0               # 적 세로 크기 2m
SATAN_PIXEL_SIZE_LENGHT = SATAN_REAL_SIZE_LENGHT_M * PIXEL_PER_METER      # 픽셀로 했을 때 길이
SATAN_PIXEL_SIZE_RAW = SATAN_REAL_SIZE_RAW_M * PIXEL_PER_METER

SPIDER_SPEED_MPS = (75.0 / 10.8)       # 50m = 3초 > 주인공보다 1.5배 빠름
SPIDER_SPEED_PPS = PIXEL_PER_METER * SPIDER_SPEED_MPS

ACTION_PER_TIME = 1.0 / 0.166         # 1초에 6번 움직임
FRAMES_PER_ACTION = 2

class Satan:
    image = None

    def __init__(self, direction):
        if Satan.image == None:
            Satan.image = load_image('Satan.png')
        if direction == 1:
            self.x, self.y, self.velocity = 800 // 2, 30, SPIDER_SPEED_PPS
            self.dir = 1
        elif direction == 2:
            self.x, self.y, self.velocity = 800 - 30, 600 // 2, SPIDER_SPEED_PPS
            self.dir = 2
        elif direction == 3:
            self.x, self.y, self.velocity = 800 // 2, 600 - 30, SPIDER_SPEED_PPS
            self.dir = 3
        elif direction == 4:
            self.x, self.y, self.velocity = 30, 600 // 2, SPIDER_SPEED_PPS
            self.dir = 4
        self.frame = 0
        self.pixel_x = SATAN_PIXEL_SIZE_LENGHT
        self.pixel_y = SATAN_PIXEL_SIZE_RAW
        self.size_x = 46
        self.size_y = 31
        self.switch = False
        self.reload = False
        self.reload2 = False
        self.attackcount = 0
        self.hp = 10
        self.score = 60

    def get_bb(self):
        return self.x - SATAN_PIXEL_SIZE_LENGHT // 2, self.y - SATAN_PIXEL_SIZE_RAW // 2,\
               self.x + SATAN_PIXEL_SIZE_LENGHT // 2, self.y + SATAN_PIXEL_SIZE_RAW // 2

    def draw(self):
        self.image.clip_draw(self.frame * self.size_x, 0, self.size_x, self.size_y, self.x, self.y, SATAN_PIXEL_SIZE_LENGHT, SATAN_PIXEL_SIZE_RAW)
        draw_rectangle(*self.get_bb())

    def update(self):
        if self.switch:
            if self.dir % 2 == 1:
                self.x -= self.velocity * game_framework.frame_time
                if self.x <= 30 + SATAN_PIXEL_SIZE_LENGHT // 2:
                    self.switch = False
            else:
                self.y -= self.velocity * game_framework.frame_time
                if self.y <= 30 + SATAN_PIXEL_SIZE_LENGHT // 2:
                    self.switch = False
        else:
            if self.dir % 2 == 1:
                self.x += self.velocity * game_framework.frame_time
                if self.x >= 800 - 30 - SATAN_PIXEL_SIZE_LENGHT // 2:
                    self.switch = True
            else:
                self.y += self.velocity * game_framework.frame_time
                if self.y >= 600 - 30 - SATAN_PIXEL_SIZE_LENGHT // 2:
                    self.switch = True

        self.attackcount += game_framework.frame_time
        if self.attackcount >= 2:
            self.frame = 1
        if self.attackcount >= 3:
            self.frame = 2
            if not self.reload:
                if self.dir == 1:
                    tears = [Enemy_tear(self.x, self.y + 10, (i % 8 + 1)) for i in range(3)]
                    game_world.add_objects(tears, server.Mob_Tear_num)
                elif self.dir == 2:
                    tears = [Enemy_tear(self.x - 10, self.y, (i % 8 + 1)) for i in range(6, 9)]
                    game_world.add_objects(tears, server.Mob_Tear_num)
                elif self.dir == 3:
                    tears = [Enemy_tear(self.x, self.y - 10, (i % 8 + 1)) for i in range(4, 7)]
                    game_world.add_objects(tears, server.Mob_Tear_num)
                elif self.dir == 4:
                    tears = [Enemy_tear(self.x + 10, self.y, (i % 8 + 1)) for i in range(2, 5)]
                    game_world.add_objects(tears, server.Mob_Tear_num)
                self.reload = True
        if self.attackcount >= 3.5:
            if not self.reload2:
                if self.dir == 1:
                    tears = [Enemy_tear(self.x, self.y + 10, (i % 8 + 1)) for i in range(3)]
                    game_world.add_objects(tears, server.Mob_Tear_num)
                elif self.dir == 2:
                    tears = [Enemy_tear(self.x - 10, self.y, (i % 8 + 1)) for i in range(6, 9)]
                    game_world.add_objects(tears, server.Mob_Tear_num)
                elif self.dir == 3:
                    tears = [Enemy_tear(self.x, self.y - 10, (i % 8 + 1)) for i in range(4, 7)]
                    game_world.add_objects(tears, server.Mob_Tear_num)
                elif self.dir == 4:
                    tears = [Enemy_tear(self.x + 10, self.y, (i % 8 + 1)) for i in range(2, 5)]
                    game_world.add_objects(tears, server.Mob_Tear_num)
                self.reload2 = True
        if self.attackcount >= 4:
            self.frame = 0
            self.attackcount = 0
            self.reload = False
            self.reload2 = False

        for tear in game_world.Tear_objects():
            if collision.collide(self, tear):
                game_world.remove_object(tear)
                self.hp -= tear.power
                if self.hp <= 0:
                    server.isaac_head.Score += self.score
                    game_world.remove_object(self)


