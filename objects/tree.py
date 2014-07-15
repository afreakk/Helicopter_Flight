"""vertexxzz fr tree"""
from core.utils import translate, get_square
import pygame
import random


def get_rand_tree(x_pos, y_pos):
    """returns a random tree, at x-y position"""
    max_width = random.randint(50, 100)
    min_width = random.randint(5, 10)
    itter_width = random.randint(5, 20)
    itter_height = random.randint(5, 20)
    random_tree = Tree(max_width, min_width, itter_width,
                       itter_height)
    random_tree.loc_translate(x_pos, y_pos)
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
        translate(0, -itter_height, height_chunk)
        points.append(height_chunk)
        next_width = max_width - itter_width
        return get_tree_vx(next_width, min_width, itter_width,
                           itter_height, points, start_iter_height)
    else:
        bottom = get_square(max_width*2, start_iter_height)
        translate(0, -start_iter_height, bottom)
        points.append(bottom)
        return points


class Tree(object):
    """Parrot that player controls"""
    branch_color = (0, 255, 0)
    bottom_color = (139, 69, 19)

    def __init__(self, max_width=50, min_width=10,
                 itter_width=10, itter_height=10):
        self.points = get_tree_vx(max_width, min_width,
                                  itter_width, itter_height)
        self.bottom = self.points[-1:]
        self.branches = self.points[:-1]

        self.max_width = max_width

    def draw(self, screen):
        """draws the helicopter on screen"""
        for branch_points in self.branches:
            pygame.draw.polygon(screen, Tree.branch_color, branch_points)
        for bottom_points in self.bottom:
            pygame.draw.polygon(screen, Tree.bottom_color, bottom_points)

    def loc_translate(self, x_velocity, y_velocity):
        """local self.points translate"""
        for branch_points in self.branches:
            translate(x_velocity, y_velocity, branch_points)
        for bottom_points in self.bottom:
            translate(x_velocity, y_velocity, bottom_points)
