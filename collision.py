def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def up_collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    a_middle_Down = (a.x, bottom_a)
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    if left_b < a_middle_Down[0] < right_b and bottom_b < a_middle_Down[1] < top_b: return True
    else: return False


def down_collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    a_middle_Up = (a.x, top_a)
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    if left_b < a_middle_Up[0] < right_b and bottom_b < a_middle_Up[1] < top_b: return True
    else: return False

def left_collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    a_middle_right = (right_a, a.y)
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    if left_b < a_middle_right[0] < right_b and bottom_b < a_middle_right[1] < top_b:
        return True
    else:
        return False

def right_collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    a_middle_left = (left_a, a.y)
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    if left_b < a_middle_left[0] < right_b and bottom_b < a_middle_left[1] < top_b:
        return True
    else:
        return False


def left_up_collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    a_middle_Down = (a.x, bottom_a)
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    if left_b < left_a < right_b < a_middle_Down[0] and bottom_b < top_a < top_b: return True
    else: return False