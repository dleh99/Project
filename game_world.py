
# layer 0: Background Objects
# layer 1: 주인공 Objects
# layer 2: Tear Objects
# layer 3: Mob Objects
# layer 4: Obstacle Objects
objects = [[], [], [], [], []]


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

def Isaac_objects():
    for o in objects[1]:
        yield o

def Tear_objects():
    for o in objects[2]:
        yield o


def Mob_objects():
    for o in objects[3]:
        yield o

def Obs_objects():
    for o in objects[4]:
        yield o

