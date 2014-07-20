"""grass etc"""
from objects.baseobj import BaseObj
from core.utils import translate_indexes, vector_div
from core.geometry import get_square
from objects.groundhandler import GroundObjHandler
from math import sin, cos


class GrassHandler(GroundObjHandler):
    """handles all the grassses"""
    def __init__(self, resolution, itter_width=25,
                 sample_width=1, y_offset=0):
        self.itter_width = itter_width
        self.width = 1
        self.height = 7.5
        GroundObjHandler.__init__(self, resolution, sample_width, y_offset)

    def _place_objs(self, (screen_width, screen_height)):
        """places out the grasses on screen"""
        for x_pos in xrange(0, screen_width, self.itter_width):
            self.objects.put(Grass((x_pos, 0), self.width, self.height))

    def _place_new_obj(self, (screen_width, screen_height)):
        """removes grass at bottom of que, places new grass at top to\
           the right of screen"""
        old_tree = self.objects.get()
        new_x = (-old_tree.position[0]) + old_tree.max_width*2 + screen_width
        another_tree = Grass((new_x, screen_height), self.width, self.height)
        self.objects.put(another_tree)

    def update(self, resolution, ground_points, delta_time):
        """overrides GroundObjHandler.update"""
        GroundObjHandler.update(self, resolution, ground_points, delta_time)
        for obj in self.objects.queue:
            obj.update(delta_time)


class Grass(BaseObj):
    """grass straw and its attributes"""
    def __init__(self, pos, width, height):
        BaseObj.__init__(self, [get_square(width, height)], (10, 255, 20), pos)
        self.max_width = width
        self.top_idx = [0, 1]
        self.velocity = (0.0, 0.0)
        self.sin_val = 0.0
        self.speed = 7.5

    def update(self, delta_time):
        """updates animation of grass"""
        self.velocity = (sin(self.sin_val), cos(self.sin_val))
        self.sin_val += delta_time*self.speed
        translate_indexes(self.velocity, self.points[0], self.top_idx)
