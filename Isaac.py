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
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_a:
                Issac_Body.direction = 1
            elif event.key == SDLK_d:
                Issac_Body.direction = 2
            elif event.key == SDLK_w:
                Issac_Body.direction = 3
            elif event.key == SDLK_s:
                Issac_Body.direction = 4

            if event.key == SDLK_LEFT:
                Issac_Head.frame = 7
            elif event.key == SDLK_RIGHT:
                Issac_Head.frame = 3
            elif event.key == SDLK_UP:
                Issac_Head.frame = 5
            elif event.key == SDLK_DOWN:
                Issac_Head.frame = 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_a or SDLK_d or SDLK_w or SDLK_s:
                Issac_Body.direction = 0
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
        self.direction = 0                      # 0 = 가만히, 1 = 왼쪽, 2 = 오른쪽, 3 = 위쪽, 4 = 밑쪽

    def update(self):
        if self.direction == 0:
            self.frame = 0
        else:
            self.frame = (self.frame + 1) % 10
            if self.direction == 1:
                self.x -= 7
            elif self.direction == 2:
                self.x += 7
            elif self.direction == 3:
                self.y += 7
            elif self.direction == 4:
                self.y -= 7

    def draw(self):
        if self.direction == 0:
            self.image.clip_draw(self.frame * Body_Lenght, 50, Body_Lenght, Body_Raw, self.x,
                                 self.y)
        elif self.direction != 4:
            self.image.clip_draw(self.frame * Body_Lenght, (self.direction - 1) * 25, Body_Lenght, Body_Raw, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * Body_Lenght, (self.direction - 2) * 25, Body_Lenght, Body_Raw, self.x,
                                 self.y)


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

