import game_framework
from pico2d import *

import game_world
import title_state
import server


name = "Rank_state"
image = None
first_font = None
font = None


def enter():
    global image, font, first_font
    with open('Rank.json', 'r') as f:
        server.Rank = json.load(f)
    first_font = load_font('ENCR10B.TTF', 90)
    font = load_font('ENCR10B.TTF', 40)
    image = load_image('Rank_page.png')


def exit():
    global image
    del(image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_world.clear()
                game_framework.change_state(title_state)


def draw():
    clear_canvas()
    image.draw(400, 300)
    first_font.draw(130, 510, 'Isaac Rank', (0, 0, 0))
    for k in range(len(server.Rank)):
        if k == 0:
            font.draw(100, 350 - 90 * (k - 1), '%dst : %0.f < My best Friend!!' % (k + 1, server.Rank[k]), (75, 0, 130))
        elif k == 1:
            font.draw(100, 350 - 90 * (k - 1), '%dnd : %0.f' % (k + 1, server.Rank[k]), (47, 79, 79))
        elif k == 2:
            font.draw(100, 350 - 90 * (k - 1), '%drd : %0.f' % (k + 1, server.Rank[k]), (47, 79, 79))
        elif k <= 4:
            font.draw(100, 350 - 90 * (k - 1), '%dst : %0.f' % (k + 1, server.Rank[k]), (47, 79, 79))
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass