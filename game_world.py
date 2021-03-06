import pickle
# layer 0: Background Objects
# layer 1: Obstacle Objects
# layer 2: Door Objects
# layer 3: Item Objects
# layer 4: Mob Objects
# layer 5: Tear Objects
# layer 6: Mob Tear Objects
# layer 7: 주인공 Objects
# layer 8:
import server

objects = [[], [], [], [], [], [], [], [], []]


def add_object(o, layer):
    objects[layer].append(o)


def add_objects(l, layer):
    objects[layer] += l


def remove_object(o):
    for i in range(len(objects)):
        if o in objects[i]:
            objects[i].remove(o)
            del o
            break

def clear():
    for o in all_objects():
        del o
    for l in objects:
        l.clear()

def destroy():
    clear()
    objects.clear()


def all_objects():
    for i in range(len(objects)):
        for o in objects[i]:
            yield o

def Background_objects():
    for o in objects[0]:
        yield o

def Obs_objects():
    for o in objects[1]:
        yield o

def Door_objects():
    for o in objects[2]:
        yield o

def Item_objects():
    for o in objects[3]:
        yield o

def Mob_objects():
    for o in objects[4]:
        yield o

def Tear_objects():
    for o in objects[5]:
        yield o

def Mob_Tear_objects():
    for o in objects[6]:
        yield o

def Isaac_objects():
    for o in objects[7]:
        yield o

def save_item():
    with open('item.sav', 'wb') as f:
        pickle.dump(objects[4], f)

def load_item():
    global objects

    with open('item.sav', 'rb') as f:
        objects[4] = pickle.load(f)

    server.item = objects[4]
