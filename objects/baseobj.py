"""base obj for translate etc"""
from core.utils import translate, vector_add
import pygame


class BaseObj(object):
    """base_object,, father of all movement"""
    def __init__(self, points, color=(255, 0, 255), pos=(0, 0)):
        self.points = points
        self.position = pos
        self.color = color
        if pos != (0, 0):
            self.loc_translate(self.position, True)

    def loc_translate(self, velocity, discreet=False):
        """local self.points translate"""
        if discreet is False:
            self.position = vector_add(self.position, velocity)
        for point_batch in self.points:
            translate(velocity, point_batch)

    def loc_set_pos(self, new_pos):
        """sets position of object"""
        total = (-self.position[0]+new_pos[0], -self.position[1]+new_pos[1])
        for point_batch in self.points:
            translate(total, point_batch)
        self.position = new_pos

    def draw(self, screen):
        """draws the object on screen"""
        for points in self.points:
            pygame.draw.polygon(screen, self.color, points)

    def update_points(self, local_points):
        """updates geometry of object, and positions it back to old pos"""
        self.points = local_points
        self.loc_translate(self.position, True)
