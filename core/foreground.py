"""foreground"""
from objects.tree import get_rand_tree
from core.utils import any_x_below
from Queue import Queue


class ForgeGround(object):
    """foregrond class"""
    def __init__(self, screen_width, screen_height):
        self.trees = Queue()
        x_pos = 0
        while x_pos < screen_width:
            another_tree = get_rand_tree(x_pos, screen_height)
            self.trees.put(another_tree)
            x_pos += 100

    def draw(self, screen):
        """draws all object in foreground object list"""
        for obj in list(self.trees.queue):
            obj.draw(screen)

    def move(self, distance):
        """updates all objz in foreground list"""
        for obj in self.trees.queue:
            obj.loc_translate(distance, 0)

    def update_positions(self, screen_width, screen_height):
        """handles tree movement, so it doesnt go out of scene etc"""
        self._keep_within_scene(screen_width, screen_height)

    def _keep_within_scene(self, screen_width, screen_height):
        """looks after trees and keeps them within scene"""
        bottom_tree = self.trees.queue[0]
        if any_x_below(bottom_tree.points, -bottom_tree.max_width*2):
            self.trees.put(self.trees.get())
            bottom_tree.loc_translate(screen_width+bottom_tree.max_width*2, 0)
