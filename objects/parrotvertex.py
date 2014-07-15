"""vertexxzz fr parrot"""
from core.utils import translate
from core.geometry import get_square


def get_parrot(blade_width=50, blade_height=10,
               pin_height=10, pin_width=5,
               house_width=35, house_height=40):
    """gets geometry vertex for parrot helicopeter"""
    blade = get_square(blade_width, blade_height)

    pin = get_square(pin_width, pin_height)
    translate((0, blade_height + pin_height), pin)

    house = get_square(house_width, house_height)
    translate((0, blade_height + pin_height + house_height), house)
    return [blade, pin, house]


def get_bomb():
    """gets geometry vertexz for bomb that helicopter drops"""
    tail_length = 10
    base_length = 20
    tail_width = 10
    angle_width = 5
    base_width = 5
    tip_length = 10
    top_bomb = [(0, 0), (tail_length, tail_width),
                (tail_length+base_length, tail_width),
                (tail_length+base_length+tip_length, tail_width+angle_width),
                (tail_length+base_length+tip_length, tail_width+angle_width+base_width)]
    top_bomb = [(x[0]*-1, x[1]) for x in top_bomb]
    bot_bomb = [(x[0], x[1]*-1) for x in top_bomb]
    bot_bomb.reverse()
    bomb = top_bomb + bot_bomb
    return [bomb]
