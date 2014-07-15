"""Simple shapes :) """


def get_square(width, height):
    """return arrray of square vertexZ"""
    return [(-width, -height),
            (+width, -height),
            (+width, +height),
            (-width, +height)]
