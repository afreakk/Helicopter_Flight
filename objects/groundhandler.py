"""Handlez trees"""
from core.utils import any_x_below
from objects.groundhelp import ground_catch_obj
from Queue import Queue


class GroundObjHandler(object):
    """puts trees on ground """
    def __init__(self, resolution,
                 sample_width, y_offset, seizure_limit=20):
        self.seizure_limit = seizure_limit
        self.sample_width = sample_width
        self.y_offset = y_offset
        self.objects = Queue()
        self._place_objs(resolution)

    def draw(self, screen):
        """draws treez in queue"""
        for obj in self.objects.queue:
            obj.draw(screen)

    def move(self, distance):
        """moves all objz in list by universally accepted distance"""
        for obj in self.objects.queue:
            obj.loc_translate((distance, 0))

    def update(self, resolution, ground_points, delta_time):
        """handles objects movement, so it doesnt go out of scene etc"""
        self._keep_within_scene(resolution)
        for tree in self.objects.queue:
            ground_catch_obj(tree, ground_points, self.sample_width,
                             self.seizure_limit, self.y_offset)

    def _keep_within_scene(self, resolution):
        """looks after objects and keeps them within scene"""
        bot_obj = self.objects.queue[0]
        obj_wdth = bot_obj.max_width*2
        if any_x_below(bot_obj.points, -obj_wdth):
            self._place_new_obj(resolution)
            self._keep_within_scene(resolution)

    def _place_objs(self, (screen_width, screen_height)):
        """placez out trees for first time"""
        raise Exception("def _place_objs(self, (screen_width, screen_height)):\
                         NOT IMPLEMENTED")

    def _place_new_obj(self, resolution):
        """placez out trees for first time"""
        raise Exception("def _place_objs(self, (screen_width, screen_height)):\
                         NOT IMPLEMENTED")
