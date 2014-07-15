"""foreground"""
from objects.tree import get_rand_tree
from core.utils import any_x_below, almost_equal
from Queue import Queue


class ForgeGround(object):
    """foregrond class"""
    def __init__(self, (screen_width, screen_height)):
        self.trees = Queue()
        x_pos = 0
        while x_pos < screen_width+100:
            another_tree = get_rand_tree((x_pos, screen_height))
            self.trees.put(another_tree)
            x_pos += 50

    def draw(self, screen):
        """draws all object in foreground object list"""
        for obj in list(self.trees.queue):
            obj.draw(screen)

    def move(self, distance):
        """updates all objz in foreground list"""
        for obj in self.trees.queue:
            obj.loc_translate((distance, 0))

    def update_positions(self, resolution):
        """handles tree movement, so it doesnt go out of scene etc"""
        self._keep_within_scene(resolution)

    def _keep_within_scene(self, resolution):
        """looks after trees and keeps them within scene"""
        bot_tree = self.trees.queue[0]
        tree_width = bot_tree.max_width*2
        if any_x_below(bot_tree.points, -tree_width):
            self._place_new_tree(resolution)
            self._keep_within_scene(resolution)

    def _place_new_tree(self, (screen_width, screen_height)):
        """removes tree at bottom of que, places new random tree at top to\
           the right of screen"""
        old_tree = self.trees.get()
        another_tree = get_rand_tree((0, screen_height))
        new_x = (-old_tree.position[0]) + old_tree.max_width*2 + screen_width
        for tree in self.trees.queue:
            while almost_equal(tree.position[0], new_x, tree.max_width):
                new_x += 1
        another_tree.loc_translate((new_x, 0))
        self.trees.put(another_tree)
