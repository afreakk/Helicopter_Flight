"""vertexxzz fr parrot"""
from core.utils import translate
from core.geometry import get_square, get_circle
from math import sin, cos


def get_blades(blade_width, blade_length, dist_traveld):
    """for getting bladez"""
    dist_traveld /= 12.5
    top_blade = [(i*sin(dist_traveld), i*cos(dist_traveld))
                 for i in range(-blade_length, blade_length)]
    bottom_blade = [x for x in reversed(top_blade)]
    translate((0, blade_width), bottom_blade)
    return top_blade+bottom_blade


def get_parrot(blade_length=50, blade_width=10,
               pin_height=10, pin_width=5,
               house_width=35, house_height=40,
               dist_traveld=0):
    """gets geometry vertex for parrot helicopeter"""
    blade = get_blades(blade_width, blade_length, dist_traveld)

    pin = get_square(pin_width, pin_height)
    translate((0, blade_width + pin_height), pin)

    house = get_circle(house_width, 100)
    translate((0, blade_width + pin_height + house_height), house)
    return [blade, pin, house]


def get_bomb(tail_length=10,
             base_length=20,
             tail_width=10,
             angle_width=5,
             base_width=5,
             tip_length=10):
    """gets geometry vertexz for bomb that helicopter drops"""
    top_bomb = [(0, 0),
                (tail_length, tail_width),
                (tail_length+base_length, tail_width),
                (tail_length+base_length+tip_length, tail_width+angle_width),
                (tail_length+base_length+tip_length, tail_width+angle_width+base_width)]
    top_bomb = [(x[0]*-1, x[1]) for x in top_bomb]
    bot_bomb = [(x[0], x[1]*-1) for x in top_bomb]
    bot_bomb.reverse()
    bomb = top_bomb + bot_bomb
    return [bomb]
