"""here goes lvl one stuff"""
from objects.parrot import Parrot
from core.gravity import Gravity
from core.foreground import ForgeGround
from objects.bombmgr import BombManager
from objects.ground import Ground


class LevelOne(object):
    """First level"""
    def __init__(self, resolution):
        self.parrot = Parrot(resolution)
        self.gravity = Gravity(100)
        self.gravity.add_object(self.parrot)
        self.fore_ground = ForgeGround(resolution)
        self.bomb_mgr = BombManager()
        self.ground = Ground(resolution, resolution[0]/1.5)
        self.distance_traveled = 0.0

    def update(self, delta_time, resolution):
        """logic update for objects in this level/scene"""
        self.parrot.update(delta_time)
        self.gravity.update(delta_time)
        distance_velocity = delta_time*200
        self.fore_ground.move(distance_velocity*-1)
        self.distance_traveled += distance_velocity
        self.fore_ground.update_positions(resolution, self.ground.points[0])
        self.ground.update_ground(self.distance_traveled, resolution)
        bomb = self.parrot.new_bomb()
        if bomb is not None:
            self.gravity.add_object(bomb)
            self.bomb_mgr.add_bomb(bomb)

    def draw(self, screen):
        """ draws object in this level/scene"""
        self.parrot.draw(screen)
        self.bomb_mgr.draw_bombs(screen)
        self.fore_ground.draw(screen)
        self.ground.draw(screen)

    def dispatch_event(self, event):
        """handles event for this level"""
        self.parrot.control(event)
