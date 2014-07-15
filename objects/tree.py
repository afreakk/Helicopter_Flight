"""vertexxzz fr tree"""
from core.utils import translate, get_square
from objects.baseobj import BaseObj
import pygame
import random


def get_rand_tree(position):
    """returns a random tree, at x-y position"""
    max_width = random.randint(50, 100)
    min_width = random.randint(5, 10)
    itter_width = random.randint(5, 20)
    itter_height = random.randint(5, 20)
    random_tree = Tree(max_width, min_width, itter_width,
                       itter_height)
    random_tree.loc_translate(position)
    return random_tree


def get_tree_vx(max_width, min_width, itter_width, itter_height,
                points=[], start_iter_height=None):
    """recursive tree builder"""
    if start_iter_height is None:
        start_iter_height = itter_height
        # reset list, at begining of every outside of function function call.
        points = []
    if max_width > min_width:
        itter_height += start_iter_height*2
        height_chunk = get_square(max_width, start_iter_height)
        translate((0, -itter_height), height_chunk)
        points.append(height_chunk)
        next_width = max_width - itter_width
        return get_tree_vx(next_width, min_width, itter_width,
                           itter_height, points, start_iter_height)
    else:
        bottom = get_square(max_width*2, start_iter_height)
        translate((0, -start_iter_height), bottom)
        points.append(bottom)
        return points


def rand_branch_color():
    """color for branchezz, greenish"""
    red = random.randint(0, 30)
    green = random.randint(200, 255)
    blue = random.randint(0, 30)
    return (red, green, blue)


def rand_bottom_color():
    """color for bottom of tree, brownsih"""
    red = random.randint(120, 160)
    green = random.randint(50, 90)
    blue = random.randint(0, 40)
    return (red, green, blue)


class Tree(BaseObj):
    """Parrot that player controls"""
    def __init__(self, max_width=50, min_width=10,
                 itter_width=10, itter_height=10):
        BaseObj.__init__(self, get_tree_vx(max_width, min_width,
                                           itter_width, itter_height))
        self.bottom = self.points[-1:]
        self.branches = self.points[:-1]

        self.max_width = max_width
        self.branch_color = rand_branch_color()
        self.bottom_color = rand_bottom_color()

    def draw(self, screen):
        """draws the helicopter on screen"""
        for branch_points in self.branches:
            pygame.draw.polygon(screen, self.branch_color, branch_points)
        for bottom_points in self.bottom:
            pygame.draw.polygon(screen, self.bottom_color, bottom_points)
