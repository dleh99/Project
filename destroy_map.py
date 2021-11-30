import game_world
import server

def destroy():
    for door in game_world.Door_objects():
        game_world.remove_object(door)
    for ob in game_world.Obs_objects():
        game_world.remove_object(ob)
    for tile in game_world.Background_objects():
        game_world.remove_object(tile)