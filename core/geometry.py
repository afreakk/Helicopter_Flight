"""Simple shapes :) """


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
