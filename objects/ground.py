""" DAMN GIRL !"""
from objects.baseobj import BaseObj
from objects.groundvertex import get_terrain


class Ground(BaseObj):
    """Parrot that player controls"""
    def __init__(self, resolution,
                 top_spacing, itter_width=10):
        self.top_spacing = top_spacing
        self.itter_width = itter_width
        BaseObj.__init__(self, self._get_terrain(0, resolution), (10, 100, 20))

    def update_ground(self, distance, resolution):
        """updates ground -- in some way"""
        self.points = self._get_terrain(distance, resolution)

    def _get_terrain(self, distance, resolution):
        """easy method for getting terrain with all local-grown vars"""
        return get_terrain(self.top_spacing, resolution, self.itter_width,
                           distance)
