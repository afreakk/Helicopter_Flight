"""base obj for translate etc"""
from core.utils import translate, vector_add
import pygame


class BaseObj(object):
    """base_object,, father of all movement"""
    def __init__(self, points, color=(255, 0, 255)):
        self.points = points
        self.position = (0, 0)
        self.color = color

    def loc_translate(self, velocity):
        """local self.points translate"""
        self.position = vector_add(self.position, velocity)
        for point_batch in self.points:
            translate(velocity, point_batch)

    def loc_set_pos(self, new_pos):
        """sets position of tree"""
        total = (-self.position[0]+new_pos[0], -self.position[1]+new_pos[1])
        for point_batch in self.points:
            translate(total, point_batch)
        self.position = new_pos

    def draw(self, screen):
        """draws the helicopter on screen"""
        for points in self.points:
            pygame.draw.polygon(screen, self.color, points)
