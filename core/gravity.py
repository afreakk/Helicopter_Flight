"""gravity"""


class Gravity(object):
    """gravity class , one instance per universe"""
    def __init__(self, strength):
        self.objects = []
        self.strength = strength

    def update(self, delta_time):
        """updates universe by delta_time"""
        time_power = delta_time*self.strength
        for obj in self.objects:
            obj.loc_translate((0, time_power))

    def add_object(self, parrot):
        """adds parrot to universe"""
        self.objects.append(parrot)
