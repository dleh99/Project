from Item import *
import server
import random
import game_world


def store(num):
    store_num = random.randint(0, num - 1) % num
    if store_num == 0:
        server.Floor_1_item_store[server.isaac_head.nowPos] = 1
        server.item = Item_Heal()
        game_world.add_object(server.item, server.Item_num)
    elif store_num == 1:
        server.Floor_1_item_store[server.isaac_head.nowPos] = 2
        server.item = Item_Speed_injector()
        game_world.add_object(server.item, server.Item_num)
    elif store_num == 2:
        server.Floor_1_item_store[server.isaac_head.nowPos] = 3
        server.item = Item_Steven()
        game_world.add_object(server.item, server.Item_num)
    elif store_num == 3:
        server.Floor_1_item_store[server.isaac_head.nowPos] = 4
        server.item = Item_Onion()
        game_world.add_object(server.item, server.Item_num)

def load(num):
    if num == 1:
        server.item = Item_Heal()
        game_world.add_object(server.item, server.Item_num)
    elif num == 2:
        server.item = Item_Speed_injector()
        game_world.add_object(server.item, server.Item_num)
    elif num == 3:
        server.item = Item_Steven()
        game_world.add_object(server.item, server.Item_num)
    elif num == 4:
        server.item = Item_Onion()
        game_world.add_object(server.item, server.Item_num)