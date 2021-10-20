import os

from pico2d import *
import math
import random

Head_Lenght = 45
Head_Raw = 42
Body_Lenght = 29
Body_Raw = 25
Tear_Size = 10
Red_Spider_Lenght = 110
Red_spider_Raw = 80
Tile_Size = 100

frame = 0

GamePlay = True

open_canvas()

def Tile_Image_Define():
    for i in range(48):
        if Tiles[i].x == 0:
            Tiles[i].image = load_image('tile_4.png')
        if Tiles[i].x == 7:
            Tiles[i].image = load_image('tile_5.png')
        if Tiles[i].y == 0:
            if Tiles[i].x == 0:
                Tiles[i].image = load_image('tile_7.png')
            elif Tiles[i].x == 7:
                Tiles[i].image = load_image('tile_8.png')
            else:
                Tiles[i].image = load_image('tile_3.png')
        if Tiles[i].y == 5:
            if Tiles[i].x == 0:
                Tiles[i].image = load_image('tile_6.png')
            elif Tiles[i].x == 7:
                Tiles[i].image = load_image('tile_9.png')
            else:
                Tiles[i].image = load_image('tile_2.png')


def Tear_Crush(x, y):
    if x <= 0 + 30 or x >= 800 - 30 or y <= 0 + 30 or y >= 600 - 30:
        return True
    return False


def Tear_Count(i):
    for count in range(5):
        if Issac_Tear[count].isView == False:
            Issac_Tear[count].isView = True
            Issac_Tear[count].x = Issac_Head.x
            Issac_Tear[count].y = Issac_Head.y
            Issac_Tear[count].direction = i
            Issac_Tear[count].acceleration = 0
            break


def Chase_Issac():
    for i in range(3):
        Red_spider[i].x += Red_spider[i].DirectionX * abs(Red_spider[i].x - Issac_Body.x) / Red_spider[i].speed
        Red_spider[i].y += Red_spider[i].DirectionY * abs(Red_spider[i].y - Issac_Body.y) / Red_spider[i].speed


def handle_events():
    global GamePlay

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            GamePlay = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                GamePlay = False

            if event.key == SDLK_a:
                Issac_Body.Left = True
            elif event.key == SDLK_d:
                Issac_Body.Right = True
            elif event.key == SDLK_w:
                Issac_Body.Up = True
            elif event.key == SDLK_s:
                Issac_Body.Down = True

            if event.key == SDLK_LEFT:
                Issac_Head.frame = 7
                Tear_Count(1)
            elif event.key == SDLK_RIGHT:
                Issac_Head.frame = 3
                Tear_Count(2)
            elif event.key == SDLK_UP:
                Issac_Head.frame = 5
                Tear_Count(3)
            elif event.key == SDLK_DOWN:
                Issac_Head.frame = 1
                Tear_Count(4)
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_a:
                Issac_Body.Left = False
            elif event.key == SDLK_d:
                Issac_Body.Right = False
            elif event.key == SDLK_w:
                Issac_Body.Up = False
            elif event.key == SDLK_s:
                Issac_Body.Down = False
        if event.key == SDLK_LEFT:
            Issac_Head.frame = 6
        elif event.key == SDLK_RIGHT:
            Issac_Head.frame = 2
        elif event.key == SDLK_UP:
            Issac_Head.frame = 4
        elif event.key == SDLK_DOWN:
            Issac_Head.frame = 0

#==============================================================
os.chdir('d:/2DGP/Project/Sprite')


class Isaac_Body:
    def __init__(self):
        self.image = load_image('Isaac_Body_Full.png')
        self.frame = 0
        self.x = 400
        self.y = 300
        self.Left, self.Right, self.Up, self.Down = False, False, False, False
        self.life = 3

    def update(self):
        if self.Left == False and self.Right == False and self.Up == False and self.Down == False:
            self.frame = 0
        else:
            self.frame = (self.frame + 1) % 10

            if self.Left:
                self.x -= 10
            if self.Right:
                self.x += 10
            if self.Up:
                self.y += 10
            if self.Down:
                self.y -= 10

            if self.x < 30:
                self.x += 10
            elif self.x > 770:
                self.x -= 10
            if self.y < 30:
                self.y += 10
            elif self.y > 570:
                self.y -= 10

    def draw(self):
        if self.Left == False and self.Right == False and self.Up == False and self.Down == False:
            self.image.clip_draw(self.frame * Body_Lenght, 50, Body_Lenght, Body_Raw, self.x,
                                 self.y)
        elif self.Left:
            self.image.clip_draw(self.frame * Body_Lenght, 0 * 25, Body_Lenght, Body_Raw, self.x, self.y)
        elif self.Right:
            self.image.clip_draw(self.frame * Body_Lenght, 1 * 25, Body_Lenght, Body_Raw, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * Body_Lenght, 2 * 25, Body_Lenght, Body_Raw, self.x, self.y)


Issac_Body = Isaac_Body()


class Isaac_Head:
    def __init__(self):
        self.image = load_image('Isaac_Head.png')
        self.frame = 0
        self.x = Issac_Body.x
        self.y = Issac_Body.y + Body_Raw

    def update(self):
        self.x = Issac_Body.x
        self.y = Issac_Body.y + Body_Raw

    def draw(self):
        self.image.clip_draw(self.frame * Head_Lenght, 0, Head_Lenght, Head_Raw, self.x, self.y)


class Isaac_Tear:
    def __init__(self):
        self.image = load_image('Isaac_Tear.png')
        self.x = Issac_Head.x
        self.y = Issac_Head.y
        self.isView = False
        self.direction = 0              # 1 = 왼쪽, 2 = 오른쪽, 3 = 위, 4 = 아래
        self.acceleration = 0

    def update(self):
        if self.direction == 1:
            self.x -= 15 + self.acceleration
        elif self.direction == 2:
            self.x += 15 + self.acceleration
        elif self.direction == 3:
            self.y += 15 + self.acceleration
        elif self.direction == 4:
            self.y -= 15 + self.acceleration

        if Tear_Crush(self.x, self.y):
            self.isView = False
        if self.acceleration < -15:
            self.isView = False

        self.acceleration -= 0.4

    def draw(self):
        if self.isView:
            self.image.clip_draw(0, 0, Tear_Size, Tear_Size, self.x, self.y, 15, 15)


class Red_Spider_obj:
    def __init__(self):
        self.x = random.randint(100, 600)
        self.y = random.randint(100, 600)
        self.image = load_image('red_spider.png')
        self.frame = 0
        self.speed = random.randint(10, 20)
        self.DirectionX = 1
        self.DirectionY = 1
        self.ChaseTime = 0

    def update(self):
        self.frame = (self.frame + 1) % 8
        if self.x > Issac_Body.x:
            self.DirectionX = -1
        else:
            self.DirectionX = 1
        if self.y > Issac_Body.y:
            self.DirectionY = -1
        else:
            self.DirectionY = 1

        if self.ChaseTime == 4:
            self.ChaseTime = 0
            Chase_Issac()

        self.ChaseTime += 1

    def draw(self):
        self.image.clip_draw(self.frame * Red_Spider_Lenght, 0, Red_Spider_Lenght, Red_spider_Raw, self.x, self.y, 55, 40)

class Tile:
    def __init__(self):
        self.x = 1
        self.y = 1
        self.image = load_image('tile_1.png')

    def Draw(self):
        self.image.clip_draw(0, 0, Tile_Size, Tile_Size, self.x * 100 + 50, self.y * 100 + 50)


Issac_Head = Isaac_Head()
Issac_Tear = [Isaac_Tear() for i in range(0, 5)]
Red_spider = [Red_Spider_obj() for i in range(0, 3)]
Tiles = [Tile() for i in range(0, 48)]
Heart = load_image('Heart.png')

for i in range(0, 48):
    Tiles[i].x = i % 8
    Tiles[i].y = i // 8
    Tile_Image_Define()


#==============================================================
while GamePlay:
    Issac_Body.update()
    Issac_Head.update()
    for i in range(5):
        Issac_Tear[i].update()
    for i in range(3):
        Red_spider[i].update()

    clear_canvas()
    for i in range(48):
        Tiles[i].Draw()
    Issac_Body.draw()
    Issac_Head.draw()
    for i in range(5):
        Issac_Tear[i].draw()
    for i in range(3):
        Red_spider[i].draw()
    for i in range(Issac_Body.life):
        Heart.clip_draw(0, 0, 50, 50, 30 * i + 30, 560, 30, 30)
    update_canvas()

    handle_events()
    delay(0.05)

close_canvas()
