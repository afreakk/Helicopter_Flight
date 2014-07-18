"""Handlez trees"""
from objects.tree import get_rand_tree
from core.utils import any_x_below, almost_equal
from objects.groundhelp import ground_catch_obj
from Queue import Queue


class TreeHandler(object):
    """Handles trees :)"""
    def __init__(self, resolution,
                 sample_width=5, y_skew=10, seizure_limit=20):
        self.seizure_limit = seizure_limit
        self.sample_width = sample_width
        self.y_skew = y_skew

        self.trees = Queue()
        self._place_trees(resolution)

    def _place_trees(self, (screen_width, screen_height)):
        """placez out trees for first time"""
        x_pos = 0
        while x_pos < screen_width+100:
            another_tree = get_rand_tree((x_pos, screen_height))
            self.trees.put(another_tree)
            x_pos += 75

    def draw(self, screen):
        """draws treez in queue"""
        for obj in list(self.trees.queue):
            obj.draw(screen)

    def move(self, distance):
        """updates all objz in foreground list"""
        for obj in self.trees.queue:
            obj.loc_translate((distance, 0))

    def update(self, resolution, ground_points):
        """handles tree movement, so it doesnt go out of scene etc"""
        self._keep_within_scene(resolution)
        for tree in self.trees.queue:
            ground_catch_obj(tree, ground_points, self.sample_width,
                             self.seizure_limit, self.y_skew)

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
