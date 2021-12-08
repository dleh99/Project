import random
from pico2d import *
import game_world
import game_framework
import random
import collision
import server

PIXEL_PER_METER = (1.0 / 0.033)          # 1px = 3.3cm
Item_REAL_SIZE_LENGHT_M = 1.5            # 아이템 가로 크기 1.5m
Item_REAL_SIZE_RAW_M = 1.5               # 아이템 세로 크기 1.5m
Item_PIXEL_SIZE_LENGHT = Item_REAL_SIZE_LENGHT_M * PIXEL_PER_METER      # 픽셀로 했을 때 길이
Item_PIXEL_SIZE_RAW = Item_REAL_SIZE_RAW_M * PIXEL_PER_METER


class Item_Heal:
    image = None

    def __init__(self):
        if Item_Heal.image == None:
            Item_Heal.image = load_image('Hp_item.png')
        self.x, self.y = 800 // 2, 600 // 2
        self.pixel_x = Item_PIXEL_SIZE_LENGHT
        self.pixel_y = Item_PIXEL_SIZE_RAW
        self.size_x = 100
        self.size_y = 100
        self.isUp = False
        self.isVisualize = True
        self.Sermon_font = load_font('ENCR10B.TTF', 20)
        self.Sermon_count = 0
        self.item_sound = load_wav('item_sound.wav')
        self.item_sound.set_volume(50)

    def get_bb(self):
        return self.x - Item_PIXEL_SIZE_LENGHT // 2, self.y - Item_PIXEL_SIZE_RAW // 2,\
               self.x + Item_PIXEL_SIZE_LENGHT // 2, self.y + Item_PIXEL_SIZE_RAW // 2

    def Item_sound(self):
        self.item_sound.play()

    def draw(self):
        if self.isVisualize:
            self.image.clip_draw(0, 0, self.size_x, self.size_y, self.x, self.y, Item_PIXEL_SIZE_LENGHT, Item_PIXEL_SIZE_RAW)
            # draw_rectangle(*self.get_bb())
        else:
            self.Sermon_font.draw(server.isaac_head.x - 50, server.isaac_head.y + 30, 'Health Up',
                                (255, 255, 255))

    def update(self):
        if self.isUp:
            self.y += 0.1
            if self.y >= (600 // 2) + 10:
                self.isUp = False
        else:
            self.y -= 0.1
            if self.y <= (600 // 2) - 10:
                self.isUp = True

        if self.isVisualize:
            for isaac in game_world.Isaac_objects():
                if collision.collide(isaac, self):
                    self.Item_sound()
                    self.isVisualize = False
                    if server.isaac_head.now_floor == 1:
                        server.Floor_1_item[server.isaac_head.nowPos] = True
                    elif server.isaac_head.now_floor == 2:
                        server.Floor_2_item[server.isaac_head.nowPos] = True
                    for all in game_world.Isaac_objects():
                        all.life += 3
        else:
            self.Sermon_count += game_framework.frame_time
            if self.Sermon_count >= 3.0:
                game_world.remove_object(self)
                server.item = None

    def __getstate__(self):
        state = {'Vis': self.isVisualize}
        return state

    def __setstate__(self, state):
        self.__init__()
        self.__dict__.update(state)

class Item_Speed_injector(Item_Heal):
    image = None

    def __init__(self):
        if Item_Speed_injector.image == None:
            Item_Speed_injector.image = load_image('Speed_item.png')
        self.x, self.y = 800 // 2, 600 // 2
        self.pixel_x = Item_PIXEL_SIZE_LENGHT
        self.pixel_y = Item_PIXEL_SIZE_RAW
        self.size_x = 100
        self.size_y = 100
        self.isUp = False
        self.isVisualize = True
        self.Sermon_font = load_font('ENCR10B.TTF', 20)
        self.Sermon_count = 0
        self.item_sound = load_wav('item_sound.wav')
        self.item_sound.set_volume(50)

    def draw(self):
        if self.isVisualize:
            self.image.clip_draw(0, 0, self.size_x, self.size_y, self.x, self.y, Item_PIXEL_SIZE_LENGHT, Item_PIXEL_SIZE_RAW)
            # draw_rectangle(*self.get_bb())
        else:
            self.Sermon_font.draw(server.isaac_head.x - 50, server.isaac_head.y + 30, 'Speed Up',
                                (255, 255, 255))

    def update(self):
        if self.isUp:
            self.y += 0.1
            if self.y >= (600 // 2) + 10:
                self.isUp = False
        else:
            self.y -= 0.1
            if self.y <= (600 // 2) - 10:
                self.isUp = True

        if self.isVisualize:
            for isaac in game_world.Isaac_objects():
                if collision.collide(isaac, self):
                    self.isVisualize = False
                    self.Item_sound()
                    if server.isaac_head.now_floor == 1:
                        server.Floor_1_item[server.isaac_head.nowPos] = True
                    elif server.isaac_head.now_floor == 2:
                        server.Floor_2_item[server.isaac_head.nowPos] = True
                    for all in game_world.Isaac_objects():
                        all.Accel += 0.5
        else:
            self.Sermon_count += game_framework.frame_time
            if self.Sermon_count >= 3.0:
                game_world.remove_object(self)
                server.item = None

class Item_Steven(Item_Heal):
    image = None

    def __init__(self):
        if Item_Steven.image == None:
            Item_Steven.image = load_image('Steven.png')
        self.x, self.y = 800 // 2, 600 // 2
        self.pixel_x = Item_PIXEL_SIZE_LENGHT
        self.pixel_y = Item_PIXEL_SIZE_RAW
        self.size_x = 100
        self.size_y = 100
        self.isUp = False
        self.isVisualize = True
        self.Sermon_font = load_font('ENCR10B.TTF', 20)
        self.Sermon_count = 0
        self.item_sound = load_wav('item_sound.wav')
        self.item_sound.set_volume(50)

    def draw(self):
        if self.isVisualize:
            self.image.clip_draw(0, 0, self.size_x, self.size_y, self.x, self.y, Item_PIXEL_SIZE_LENGHT,
                                 Item_PIXEL_SIZE_RAW)
            # draw_rectangle(*self.get_bb())
        else:
            self.Sermon_font.draw(server.isaac_head.x - 50, server.isaac_head.y + 30, 'Power Up',
                                  (255, 255, 255))

    def update(self):
        if self.isUp:
            self.y += 0.1
            if self.y >= (600 // 2) + 10:
                self.isUp = False
        else:
            self.y -= 0.1
            if self.y <= (600 // 2) - 10:
                self.isUp = True

        if self.isVisualize:
            for isaac in game_world.Isaac_objects():
                if collision.collide(isaac, self):
                    self.isVisualize = False
                    self.Item_sound()
                    if server.isaac_head.now_floor == 1:
                        server.Floor_1_item[server.isaac_head.nowPos] = True
                    elif server.isaac_head.now_floor == 2:
                        server.Floor_2_item[server.isaac_head.nowPos] = True
                    server.isaac_head.power += 5
        else:
            self.Sermon_count += game_framework.frame_time
            if self.Sermon_count >= 3.0:
                game_world.remove_object(self)
                server.item = None

class Item_Onion(Item_Heal):
    image = None

    def __init__(self):
        if Item_Onion.image == None:
            Item_Onion.image = load_image('Onion.png')
        self.x, self.y = 800 // 2, 600 // 2
        self.pixel_x = Item_PIXEL_SIZE_LENGHT
        self.pixel_y = Item_PIXEL_SIZE_RAW
        self.size_x = 30
        self.size_y = 30
        self.isUp = False
        self.isVisualize = True
        self.Sermon_font = load_font('ENCR10B.TTF', 20)
        self.Sermon_count = 0
        self.item_sound = load_wav('item_sound.wav')
        self.item_sound.set_volume(50)

    def draw(self):
        if self.isVisualize:
            self.image.clip_draw(0, 0, self.size_x, self.size_y, self.x, self.y, Item_PIXEL_SIZE_LENGHT,
                                 Item_PIXEL_SIZE_RAW)
            # draw_rectangle(*self.get_bb())
        else:
            self.Sermon_font.draw(server.isaac_head.x - 50, server.isaac_head.y + 30, 'Tears Up',
                                  (255, 255, 255))

    def update(self):
        if self.isUp:
            self.y += 0.1
            if self.y >= (600 // 2) + 10:
                self.isUp = False
        else:
            self.y -= 0.1
            if self.y <= (600 // 2) - 10:
                self.isUp = True

        if self.isVisualize:
            for isaac in game_world.Isaac_objects():
                if collision.collide(isaac, self):
                    self.isVisualize = False
                    self.Item_sound()
                    if server.isaac_head.now_floor == 1:
                        server.Floor_1_item[server.isaac_head.nowPos] = True
                    elif server.isaac_head.now_floor == 2:
                        server.Floor_2_item[server.isaac_head.nowPos] = True
                    server.isaac_head.item_delay += 20
        else:
            self.Sermon_count += game_framework.frame_time
            if self.Sermon_count >= 3.0:
                game_world.remove_object(self)
                server.item = None