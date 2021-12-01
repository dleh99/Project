import server
import game_world
from Door import *
from Tile import *


def make_Map(txt):
    f = open(txt)
    for i in range(7):
        server.tile.append(f.readline())
    f.close()

    for line in range(6):
        for n in range(8):
            if server.tile[line][n] == '1':
                game_world.add_object(Tile_1(line, n), server.Background_num)
            elif server.tile[line][n] == '2':
                game_world.add_object(Tile_2(line, n), server.Background_num)
            elif server.tile[line][n] == '3':
                game_world.add_object(Tile_3(line, n), server.Background_num)
            elif server.tile[line][n] == '4':
                game_world.add_object(Tile_4(line, n), server.Background_num)
            elif server.tile[line][n] == '5':
                game_world.add_object(Tile_5(line, n), server.Background_num)
            elif server.tile[line][n] == '6':
                game_world.add_object(Tile_6(line, n), server.Background_num)
            elif server.tile[line][n] == '7':
                game_world.add_object(Tile_7(line, n), server.Background_num)
            elif server.tile[line][n] == '8':
                game_world.add_object(Tile_8(line, n), server.Background_num)
            elif server.tile[line][n] == '9':
                game_world.add_object(Tile_9(line, n), server.Background_num)
            elif server.tile[line][n] == 'f':
                game_world.add_object(Tile_f(line, n), server.Obs_num)

    for i in range(len(server.tile[6])):
        if server.tile[6][i] == '1':
            server.doors.append(Door_Down(800 // 2, 18))
            game_world.add_objects(server.doors, server.Door_num)
        elif server.tile[6][i] == '2':
            server.doors.append(Door_right(800 - 18, 600 // 2))
            game_world.add_objects(server.doors, server.Door_num)
        elif server.tile[6][i] == '3':
            server.doors.append(Door_Up(800 // 2, 600 - 18))
            game_world.add_objects(server.doors, server.Door_num)
        elif server.tile[6][i] == '4':
            server.doors.append(Door_left(18, 600 // 2))
            game_world.add_objects(server.doors, server.Door_num)