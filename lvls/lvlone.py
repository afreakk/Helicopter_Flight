"""here goes lvl one stuff"""
from core.gravity import Gravity
from objects.treehandler import TreeHandler
from objects.bombmgr import BombManager
from objects.ground import Ground
from objects.parrot import Parrot


class LevelOne(object):
    """First level"""
    def __init__(self, resolution):
        self.parrot = Parrot(resolution)
        self.gravity = Gravity(100)
        self.gravity.add_object(self.parrot)
        self.tree_handler = TreeHandler(resolution)
        self.bomb_mgr = BombManager()
        self.ground = Ground(resolution, resolution[0]/1.5)
        self.distance_traveled = 0.0

    def update(self, delta_time, resolution):
        """logic update for objects in this level/scene"""
        self.gravity.update(delta_time)
        self.parrot.update(delta_time)
        distance_velocity = delta_time*200
        self.tree_handler.move(distance_velocity*-1)
        self.distance_traveled += distance_velocity
        self.tree_handler.update(resolution, self.ground.points[0])
        self.ground.update_ground(self.distance_traveled, resolution)
        self._handle_bombing()

    def draw(self, screen):
        """ draws object in this level/scene"""
        self.parrot.draw(screen)
        self.bomb_mgr.draw_bombs(screen)
        self.tree_handler.draw(screen)
        self.ground.draw(screen)

    def dispatch_event(self, event):
        """handles event for this level"""
        self.parrot.control(event)

    def _handle_bombing(self):
        """handles bomb dropping and adds to bomb manager and gravity"""
        bomb = self.parrot.new_bomb()
        if bomb is not None:
            self.gravity.add_object(bomb)
            self.bomb_mgr.add_bomb(bomb)
