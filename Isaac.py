import os

from pico2d import *

Head_Lenght = 45
Head_Raw = 42
Body_Lenght = 29
Body_Raw = 25
Tear_Size = 10

frame = 0

GamePlay = True


def Tear_Crush(x, y):
    if x <= 0 or x >= 800 or y <= 0 or y >= 600:
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

open_canvas()
#==============================================================
os.chdir('d:/2DGP/Project/Sprite/Isaac')


class Isaac_Body:
    def __init__(self):
        self.image = load_image('Isaac_Body_Full.png')
        self.frame = 0
        self.x = 400
        self.y = 300
        self.Left, self.Right, self.Up, self.Down = False, False, False, False

    def update(self):
        if self.Left == False and self.Right == False and self.Up == False and self.Down == False:
            self.frame = 0
        else:
            self.frame = (self.frame + 1) % 10
            if self.Left:
                self.x -= 7
            if self.Right:
                self.x += 7
            if self.Up:
                self.y += 7
            if self.Down:
                self.y -= 7

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


Issac_Head = Isaac_Head()
Issac_Tear = [Isaac_Tear() for i in range(5)]

#==============================================================
while GamePlay:
    Issac_Body.update()
    Issac_Head.update()
    for i in range(5):
        Issac_Tear[i].update()

    clear_canvas()
    Issac_Body.draw()
    Issac_Head.draw()
    for i in range(5):
        Issac_Tear[i].draw()
    update_canvas()

    handle_events()
    delay(0.05)

close_canvas()

