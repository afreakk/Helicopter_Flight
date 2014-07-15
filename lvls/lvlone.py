"""here goes lvl one stuff"""
from objects.parrot import Parrot
from core.gravity import Gravity
from core.foreground import ForgeGround


class LevelOne(object):
    """First level"""
    def __init__(self, resolution):
        self.parrot = Parrot(resolution)
        self.gravity = Gravity(100)
        self.gravity.add_parrot(self.parrot)
        self.fore_ground = ForgeGround(resolution)

    def update(self, delta_time, resolution):
        """logic update for objects in this level/scene"""
        self.parrot.update(delta_time)
        self.gravity.update(delta_time)
        self.fore_ground.move(delta_time*-200)
        self.fore_ground.update_positions(resolution)

    def draw(self, screen):
        """ draws object in this level/scene"""
        self.parrot.draw(screen)
        self.fore_ground.draw(screen)

    def dispatch_event(self, event):
        """handles event for this level"""
        self.parrot.control(event)
