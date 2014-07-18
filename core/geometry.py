"""Simple shapes :) """
from math import sin, cos, pi


def get_square(width, height):
    """return arrray of square vertexZ"""
    return [(-width, -height),
            (+width, -height),
            (+width, +height),
            (-width, +height)]


def get_tree_square(width, height, ratio):
    """return arrray of square vertexZ"""
    return [(-width/ratio, -height),
            (+width/ratio, -height),
            (+width, +height),
            (-width, +height)]


def get_circle(radius, points):
    """return array of circle vertexz"""
    x_f = lambda x: sin((x/float(points))*(pi*2))*radius
    y_f = lambda y: cos((y/float(points))*(pi*2))*radius
    return [(x_f(i), y_f(i)) for i in range(points)]
