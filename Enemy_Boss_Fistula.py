import random
from pico2d import *
import game_world
import game_framework
import random
import server
import collision

PIXEL_PER_METER = (1.0 / 0.033)     # 1px = 3.3cm

FISTULA_REAL_SIZE_LENGHT_M = 6.0            # 적 가로 크기 6m
FISTULA_REAL_SIZE_RAW_M = 6.0               # 적 세로 크기 6m
FISTULA_PIXEL_SIZE_LENGHT = FISTULA_REAL_SIZE_LENGHT_M * PIXEL_PER_METER      # 픽셀로 했을 때 길이
FISTULA_PIXEL_SIZE_RAW = FISTULA_REAL_SIZE_RAW_M * PIXEL_PER_METER

FISTULA_Pase_1_SPEED_MPS = (50.0 / 10.8)       # 50m = 3초 > 주인공보다 1.0배 빠름
FISTULA_Pase_1_SPEED_PPS = PIXEL_PER_METER * FISTULA_Pase_1_SPEED_MPS
FISTULA_Pase_2_SPEED_MPS = (60.0 / 10.8)       # 50m = 3초 > 주인공보다 1.2배 빠름
FISTULA_Pase_2_SPEED_PPS = PIXEL_PER_METER * FISTULA_Pase_2_SPEED_MPS
FISTULA_Pase_3_SPEED_MPS = (70.0 / 10.8)       # 50m = 3초 > 주인공보다 1.4배 빠름
FISTULA_Pase_3_SPEED_PPS = PIXEL_PER_METER * FISTULA_Pase_3_SPEED_MPS
FISTULA_Pase_4_SPEED_MPS = (80.0 / 10.8)       # 50m = 3초 > 주인공보다 1.6배 빠름
FISTULA_Pase_4_SPEED_PPS = PIXEL_PER_METER * FISTULA_Pase_4_SPEED_MPS

ACTION_PER_TIME = 1.0 / 0.166         # 1초에 6번 움직임
FRAMES_PER_ACTION = 2

class Fistula_pase_1:
    image = None

    def __init__(self):
        if Fistula_pase_1.image == None:
            Fistula_pase_1.image = load_image('Fistula 1.png')
        self.x, self.y, self.velocity = 800 // 2, 600 // 2, FISTULA_Pase_1_SPEED_PPS
        self.frame = 0
        self.pixel_x = FISTULA_PIXEL_SIZE_LENGHT
        self.pixel_y = FISTULA_PIXEL_SIZE_RAW
        self.size_x = 80
        self.size_y = 80
        self.hp = 10
        self.dir = 2
        self.timer = 0
        self.score = 100
        self.death_sound = load_wav('big_enemy_death.wav')
        self.death_sound.set_volume(50)

    def get_bb(self):
        return self.x - self.pixel_x // 2, self.y - self.pixel_y // 2,\
               self.x + self.pixel_x // 2, self.y + self.pixel_y // 2

    def death(self):
        self.death_sound.play()

    def draw(self):
        self.image.clip_draw(int(self.frame) * self.size_x, 0, self.size_x, self.size_y, self.x, self.y, self.pixel_x, self.pixel_y)
        # draw_rectangle(*self.get_bb())
        # fill here for draw

    def update(self):
        self.timer += game_framework.frame_time

        if self.timer % 10 == 0:
            self.timer = 0
            self.velocity *= 1.2
        if self.dir == 1:
            self.x -= self.velocity * game_framework.frame_time
            self.y += self.velocity * game_framework.frame_time
            if self.x <= 30 + self.pixel_x // 2:
                self.dir = 2
            if self.y >= 570 - self.pixel_y // 2:
                self.dir = 4
        elif self.dir == 2:
            self.x += self.velocity * game_framework.frame_time
            self.y += self.velocity * game_framework.frame_time
            if self.x >= 770 - self.pixel_x // 2:
                self.dir = 1
            if self.y >= 570 - self.pixel_y // 2:
                self.dir = 3
        elif self.dir == 3:
            self.x += self.velocity * game_framework.frame_time
            self.y -= self.velocity * game_framework.frame_time
            if self.x >= 770 - self.pixel_x // 2:
                self.dir = 4
            if self.y <= 30 + self.pixel_y // 2:
                self.dir = 2
        elif self.dir == 4:
            self.x -= self.velocity * game_framework.frame_time
            self.y -= self.velocity * game_framework.frame_time
            if self.x <= 30 + self.pixel_x // 2:
                self.dir = 3
            if self.y <= 30 + self.pixel_y // 2:
                self.dir = 1

        # 눈물과 충돌 체크
        for tear in game_world.Tear_objects():
            if collision.collide(self, tear):
                game_world.remove_object(tear)
                self.hp -= tear.power
                if self.hp <= 0:
                    self.death()
                    server.isaac_head.Score += self.score
                    game_world.remove_object(self)
                    if not self.dir == 4:
                        server.boss = [Fistula_pase_2(self.x, self.y, self.dir + i) for i in range(2)]
                        game_world.add_objects(server.boss, server.Mob_num)
                    else:
                        server.boss = [Fistula_pase_2(self.x, self.y, self.dir), Fistula_pase_2(self.x, self.y, 1)]
                        game_world.add_objects(server.boss, server.Mob_num)

class Fistula_pase_2(Fistula_pase_1):
    image = None

    def __init__(self, x, y, dir):
        if Fistula_pase_2.image == None:
            Fistula_pase_2.image = load_image('Fistula 2.png')
        self.x, self.y, self.velocity = x, y, FISTULA_Pase_2_SPEED_PPS
        self.frame = 0
        self.pixel_x = FISTULA_PIXEL_SIZE_LENGHT // 2
        self.pixel_y = FISTULA_PIXEL_SIZE_RAW // 2
        self.size_x = 45
        self.size_y = 45
        self.hp = 10
        self.dir = dir
        self.timer = 0
        self.score = 80
        self.death_sound = load_wav('big_enemy_death.wav')
        self.death_sound.set_volume(50)

    def update(self):
        self.timer += game_framework.frame_time

        if self.timer % 10 == 0:
            self.timer = 0
            self.velocity *= 1.2
        if self.dir == 1:
            self.x -= self.velocity * game_framework.frame_time
            self.y += self.velocity * game_framework.frame_time
            if self.x <= 30 + self.pixel_x // 2:
                self.dir = 2
            if self.y >= 570 - self.pixel_y // 2:
                self.dir = 4
        elif self.dir == 2:
            self.x += self.velocity * game_framework.frame_time
            self.y += self.velocity * game_framework.frame_time
            if self.x >= 770 - self.pixel_x // 2:
                self.dir = 1
            if self.y >= 570 - self.pixel_y // 2:
                self.dir = 3
        elif self.dir == 3:
            self.x += self.velocity * game_framework.frame_time
            self.y -= self.velocity * game_framework.frame_time
            if self.x >= 770 - self.pixel_x // 2:
                self.dir = 4
            if self.y <= 30 + self.pixel_y // 2:
                self.dir = 2
        elif self.dir == 4:
            self.x -= self.velocity * game_framework.frame_time
            self.y -= self.velocity * game_framework.frame_time
            if self.x <= 30 + self.pixel_x // 2:
                self.dir = 3
            if self.y <= 30 + self.pixel_y // 2:
                self.dir = 1

        # 눈물과 충돌 체크
        for tear in game_world.Tear_objects():
            if collision.collide(self, tear):
                game_world.remove_object(tear)
                self.hp -= tear.power
                if self.hp <= 0:
                    self.death()
                    server.isaac_head.Score += self.score
                    game_world.remove_object(self)
                    if not self.dir == 4:
                        server.boss = [Fistula_pase_3(self.x, self.y, self.dir + i) for i in range(2)]
                        game_world.add_objects(server.boss, server.Mob_num)
                    else:
                        server.boss = [Fistula_pase_3(self.x, self.y, self.dir), Fistula_pase_3(self.x, self.y, 1)]
                        game_world.add_objects(server.boss, server.Mob_num)

class Fistula_pase_3(Fistula_pase_1):
    image = None

    def __init__(self, x, y, dir):
        if Fistula_pase_3.image == None:
            Fistula_pase_3.image = load_image('Fistula 3.png')
        self.x, self.y, self.velocity = x, y, FISTULA_Pase_3_SPEED_PPS
        self.frame = 0
        self.pixel_x = FISTULA_PIXEL_SIZE_LENGHT // 4
        self.pixel_y = FISTULA_PIXEL_SIZE_RAW // 4
        self.size_x = 40
        self.size_y = 40
        self.hp = 10
        self.dir = dir
        self.timer = 0
        self.score = 50
        self.death_sound = load_wav('big_enemy_death.wav')
        self.death_sound.set_volume(50)

    def update(self):
        self.timer += game_framework.frame_time

        if self.timer % 10 == 0:
            self.timer = 0
            self.velocity *= 1.2
        if self.dir == 1:
            self.x -= self.velocity * game_framework.frame_time
            self.y += self.velocity * game_framework.frame_time
            if self.x <= 30 + self.pixel_x // 2:
                self.dir = 2
            if self.y >= 570 - self.pixel_y // 2:
                self.dir = 4
        elif self.dir == 2:
            self.x += self.velocity * game_framework.frame_time
            self.y += self.velocity * game_framework.frame_time
            if self.x >= 770 - self.pixel_x // 2:
                self.dir = 1
            if self.y >= 570 - self.pixel_y // 2:
                self.dir = 3
        elif self.dir == 3:
            self.x += self.velocity * game_framework.frame_time
            self.y -= self.velocity * game_framework.frame_time
            if self.x >= 770 - self.pixel_x // 2:
                self.dir = 4
            if self.y <= 30 + self.pixel_y // 2:
                self.dir = 2
        elif self.dir == 4:
            self.x -= self.velocity * game_framework.frame_time
            self.y -= self.velocity * game_framework.frame_time
            if self.x <= 30 + self.pixel_x // 2:
                self.dir = 3
            if self.y <= 30 + self.pixel_y // 2:
                self.dir = 1

        # 눈물과 충돌 체크
        for tear in game_world.Tear_objects():
            if collision.collide(self, tear):
                game_world.remove_object(tear)
                self.hp -= tear.power
                if self.hp <= 0:
                    self.death()
                    server.isaac_head.Score += self.score
                    if not self.dir == 4:
                        server.boss = [Fistula_pase_4(self.x, self.y, self.dir + i) for i in range(2)]
                        game_world.add_objects(server.boss, server.Mob_num)
                    else:
                        server.boss = [Fistula_pase_4(self.x, self.y, self.dir), Fistula_pase_4(self.x, self.y, 1)]
                        game_world.add_objects(server.boss, server.Mob_num)
                    game_world.remove_object(self)


class Fistula_pase_4(Fistula_pase_1):
    image = None

    def __init__(self, x, y, dir):
        if Fistula_pase_4.image == None:
            Fistula_pase_4.image = load_image('Fistula 4.png')
        self.x, self.y, self.velocity = x, y, FISTULA_Pase_4_SPEED_PPS
        self.frame = 0
        self.pixel_x = FISTULA_PIXEL_SIZE_LENGHT // 8
        self.pixel_y = FISTULA_PIXEL_SIZE_RAW // 8
        self.size_x = 30
        self.size_y = 30
        self.hp = 10
        self.dir = dir
        self.timer = 0
        self.score = 30
        self.death_sound = load_wav('big_enemy_death.wav')
        self.death_sound.set_volume(50)

    def update(self):
        self.timer += game_framework.frame_time

        if self.timer % 10 == 0:
            self.timer = 0
            self.velocity *= 1.2
        if self.dir == 1:
            self.x -= self.velocity * game_framework.frame_time
            self.y += self.velocity * game_framework.frame_time
            if self.x <= 30 + self.pixel_x // 2:
                self.dir = 2
            if self.y >= 570 - self.pixel_y // 2:
                self.dir = 4
        elif self.dir == 2:
            self.x += self.velocity * game_framework.frame_time
            self.y += self.velocity * game_framework.frame_time
            if self.x >= 770 - self.pixel_x // 2:
                self.dir = 1
            if self.y >= 570 - self.pixel_y // 2:
                self.dir = 3
        elif self.dir == 3:
            self.x += self.velocity * game_framework.frame_time
            self.y -= self.velocity * game_framework.frame_time
            if self.x >= 770 - self.pixel_x // 2:
                self.dir = 4
            if self.y <= 30 + self.pixel_y // 2:
                self.dir = 2
        elif self.dir == 4:
            self.x -= self.velocity * game_framework.frame_time
            self.y -= self.velocity * game_framework.frame_time
            if self.x <= 30 + self.pixel_x // 2:
                self.dir = 3
            if self.y <= 30 + self.pixel_y // 2:
                self.dir = 1

        # 눈물과 충돌 체크
        for tear in game_world.Tear_objects():
            if collision.collide(self, tear):
                game_world.remove_object(tear)
                self.hp -= tear.power
                if self.hp <= 0:
                    self.death()
                    server.isaac_head.Score += self.score
                    game_world.remove_object(self)