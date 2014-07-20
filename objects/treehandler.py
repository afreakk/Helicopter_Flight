"""Handlez trees"""
from objects.tree import get_rand_tree
from core.utils import almost_equal
from objects.groundhandler import GroundObjHandler


class TreeHandler(GroundObjHandler):
    """Handles trees :)"""
    def __init__(self, resolution,
                 sample_width=1, y_offset=10):
        GroundObjHandler.__init__(self, resolution, sample_width, y_offset)

    def _place_objs(self, (screen_width, screen_height)):
        """ overrides base .. placez out trees for first time"""
        for x_pos in xrange(0, screen_width+100, 75):
            self.objects.put(get_rand_tree((x_pos, screen_height)))

    def _place_new_obj(self, (screen_width, screen_height)):
        """ overrides base .. removes tree at bottom of que, places new random\
           tree at top to the right of screen"""
        old_tree = self.objects.get()
        another_tree = get_rand_tree((0, screen_height))
        new_x = (-old_tree.position[0]) + old_tree.max_width*2 + screen_width
        while almost_equal(self.objects.queue[0].position[0],
                           new_x, self.objects.queue[0].max_width):
            new_x += 1
        another_tree.loc_translate((new_x, 0))
        self.objects.put(another_tree)
