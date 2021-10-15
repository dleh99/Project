from pico2d import *
import os

Head_Lenght = 45
Head_Raw = 42
Body_Lenght = 29
Body_Raw = 25

frame = 0

GamePlay = True

def handle_events():
    global GamePlay

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            GamePlay = False

open_canvas()
#==============================================================
os.chdir('d:/2DGP/Project/Sprite/Isaac')


class Isaac_Body:
    def __init__(self):
        self.image = load_image('Isaac_Body.png')
        self.frame = 0
        self.x = 400
        self.y = 300
        self.direction = 0                      # 0 = 가만히, 1 = 왼쪽, 2 = 오른쪽, 3 = 위쪽, 4 = 밑쪽

    def update(self):
        if self.direction == 0:
            self.frame = 0
        else:
            self.frame = (self.frame + 1) % 10

    def draw(self):
        self.image.clip_draw(self.frame * Body_Lenght, 0, Body_Lenght, Body_Raw, self.x, self.y)


Issac_Body = Isaac_Body()


class Isaac_Head:
    def __init__(self):
        self.image = load_image('Isaac_Head.png')
        self.frame = 0
        self.x = Issac_Body.x
        self.y = Issac_Body.y + Body_Raw


    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0 * Head_Lenght, 0, Head_Lenght, Head_Raw, self.x, self.y)


Issac_Head = Isaac_Head()

#==============================================================
while GamePlay:
    Issac_Body.update()
    Issac_Head.update()

    clear_canvas()
    Issac_Body.draw()
    Issac_Head.draw()
    update_canvas()

    handle_events()
    delay(0.05)

close_canvas()

