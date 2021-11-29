from pico2d import *
import game_world
import game_framework
import server

class Tile:
    def __init__(self, x, y, image):
        self.x, self.y = x, y
        self.image = load_image(image)
        self.size_x = 30
        self.size_y = 100
        server.Tile_1 = load_image('tile_1.png')
        server.Tile_2 = load_image('tile_2.png')
        server.Tile_3 = load_image('tile_3.png')
        server.Tile_4 = load_image('tile_4.png')
        server.Tile_5 = load_image('tile_5.png')
        server.Tile_6 = load_image('tile_6.png')
        server.Tile_7 = load_image('tile_7.png')
        server.Tile_8 = load_image('tile_8.png')
        server.Tile_9 = load_image('tile_9.png')

    def get_bb(self):
        pass

    def draw(self):
        for line in range(6):
            for n in range(8):
                if server.tile[line][n] == '1':
                    server.Tile_1.clip_draw(0, 0, 100, 100, n * 100 + 50, (5 - line) * 100 + 50)
                elif server.tile[line][n] == '2':
                    server.Tile_2.clip_draw(0, 0, 100, 100, n * 100 + 50, (5 - line) * 100 + 50)
                elif server.tile[line][n] == '3':
                    server.Tile_3.clip_draw(0, 0, 100, 100, n * 100 + 50, (5 - line) * 100 + 50)
                elif server.tile[line][n] == '4':
                    server.Tile_4.clip_draw(0, 0, 100, 100, n * 100 + 50, (5 - line) * 100 + 50)
                elif server.tile[line][n] == '5':
                    server.Tile_5.clip_draw(0, 0, 100, 100, n * 100 + 50, (5 - line) * 100 + 50)
                elif server.tile[line][n] == '6':
                    server.Tile_6.clip_draw(0, 0, 100, 100, n * 100 + 50, (5 - line) * 100 + 50)
                elif server.tile[line][n] == '7':
                    server.Tile_7.clip_draw(0, 0, 100, 100, n * 100 + 50, (5 - line) * 100 + 50)
                elif server.tile[line][n] == '8':
                    server.Tile_8.clip_draw(0, 0, 100, 100, n * 100 + 50, (5 - line) * 100 + 50)
                elif server.tile[line][n] == '9':
                    server.Tile_9.clip_draw(0, 0, 100, 100, n * 100 + 50, (5 - line) * 100 + 50)

    def update(self):
        pass

