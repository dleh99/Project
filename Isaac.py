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
Isaac_Head = load_image('Isaac_Head.png')
Isaac_Body = load_image('Isaac_Body.png')
#==============================================================
while GamePlay:
    clear_canvas()
    Isaac_Body.clip_draw(frame * Body_Lenght, 0, Body_Lenght, Body_Raw, 400, 300)
    Isaac_Head.clip_draw(0 * Head_Lenght, 0, Head_Lenght, Head_Raw, 400, 300 + Body_Raw)
    update_canvas()
    frame = (frame + 1) % 10

    handle_events()
    delay(0.05)

close_canvas()

