"""vertexxzz fr parrot"""
from core.utils import translate, get_square


def get_parrot():
    """gets geometry vertex for parrot helicopeter"""
    blade_width = 50
    blade_height = 10
    blade = get_square(blade_width, blade_height)

    pin_height = 10
    pin_width = 5
    pin = get_square(pin_width, pin_height)
    translate(0, blade_height + pin_height, pin)

    house_width = 35
    house_height = 40
    house = get_square(house_width, house_height)
    translate(0, blade_height + pin_height + house_height, house)
    return [blade, pin, house]
