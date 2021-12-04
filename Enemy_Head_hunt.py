from pico2d import *
import game_world
import game_framework
import server
import collision
from Enemy_Tear import Enemy_tear

PIXEL_PER_METER = (1.0 / 0.033)     # 1px = 3.3cm

Head_REAL_SIZE_LENGHT_M = 1.5            # 적 가로 크기 1.5m
Head_REAL_SIZE_RAW_M = 1.5               # 적 세로 크기 1.5m
Head_PIXEL_SIZE_LENGHT = Head_REAL_SIZE_LENGHT_M * PIXEL_PER_METER      # 픽셀로 했을 때 길이
Head_PIXEL_SIZE_RAW = Head_REAL_SIZE_RAW_M * PIXEL_PER_METER

# 이 적은 움직이지 않음
# SPIDER_SPEED_MPS = (75.0 / 10.8)       # 50m = 3초 > 주인공보다 1.5배 빠름
# SPIDER_SPEED_PPS = PIXEL_PER_METER * SPIDER_SPEED_MPS

# 이 적은 프레임이 있는데 평상시에는 움직이지 않음
# ACTION_PER_TIME = 1.0 / 0.166         # 1초에 6번 움직임
# FRAMES_PER_ACTION = 2

class Head_hunt:
    image = None

    def __init__(self, dir = 1):
        if Head_hunt.image == None:
            Head_hunt.image = load_image('Head_hunt.png')
        if dir == 0 or dir == 1:
            self.dir = 1
            self.y = 30
            if dir == 0:
                self.x = 800 // 4
            else:
                self.x = 800 * 3 // 4
        elif dir == 2 or dir == 3:
            self.dir = 2
            self.x = 800 - 30
            if dir == 2:
                self.y = 600 // 4
            else:
                self.y = 600 * 3 // 4
        elif dir == 4 or dir == 5:
            self.dir = 3
            self.y = 600 - 30
            if dir == 4:
                self.x = 800 * 3 // 4
            else:
                self.x = 800 // 4
        elif dir == 6 or dir == 7:
            self.dir = 4
            self.x = 30
            if dir == 6:
                self.y = 600 * 3 // 4
            else:
                self.y = 600 // 4
        self.frame = 0
        self.pixel_x = Head_PIXEL_SIZE_LENGHT
        self.pixel_y = Head_PIXEL_SIZE_RAW
        self.size_x = 32
        self.size_y = 32
        self.hp = 50
        self.Shake = True
        self.Shake_num = 0
        self.reload = False
        self.attack_count = 0

    def get_bb(self):
        return self.x - self.pixel_x // 2, self.y - self.pixel_y // 2,\
               self.x + self.pixel_x // 2, self.y + self.pixel_y // 2

    def draw(self):
        self.image.clip_draw(int(self.frame) * self.size_x, 0, self.size_x, self.size_y, self.x, self.y, self.pixel_x, self.pixel_y)
        draw_rectangle(*self.get_bb())
        # fill here for draw

    def update(self):
        # 눈물과 충돌 체크
        for tear in game_world.Tear_objects():
            if collision.collide(self, tear):
                game_world.remove_object(tear)
                self.hp -= tear.power
                if self.hp <= 0:
                    game_world.remove_object(self)
        if self.Shake:
            self.Shake_num += 1
            self.x += 0.1
            if self.Shake_num == 10:
                self.Shake_num = 0
                self.Shake = False
        else:
            self.Shake_num += 1
            self.x -= 0.1
            if self.Shake_num == 10:
                self.Shake_num = 0
                self.Shake = True

        if server.isaac_head.x - server.isaac_head.size_x <= self.x <= server.isaac_head.x + server.isaac_head.size_x \
                or server.isaac_head.y - server.isaac_head.size_y <= self.y <= server.isaac_head.y + server.isaac_head.size_y:
            self.frame = 1
            if not self.reload:
                if self.dir == 1:
                    tears = Enemy_tear(self.x, self.y + 10, 2)
                    game_world.add_object(tears, server.Mob_Tear_num)
                elif self.dir == 2:
                    tears = Enemy_tear(self.x - 10, self.y, 8)
                    game_world.add_object(tears, server.Mob_Tear_num)
                elif self.dir == 3:
                    tears = Enemy_tear(self.x, self.y - 10, 6)
                    game_world.add_object(tears, server.Mob_Tear_num)
                elif self.dir == 4:
                    tears = Enemy_tear(self.x + 10, self.y, 4)
                    game_world.add_object(tears, server.Mob_Tear_num)
                self.reload = True

        if self.reload:
            self.attack_count += game_framework.frame_time
            if self.attack_count >= 0.05:
                self.frame = 2
            if self.attack_count >= 0.5:
                self.frame = 0
            if self.attack_count >= 2:
                self.reload = False
                self.attack_count = 0





