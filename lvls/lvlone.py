"""here goes lvl one stuff"""
from core.gravity import Gravity
from objects.treehandler import TreeHandler
from objects.bombmgr import BombManager
from objects.ground import Ground
from objects.parrot import Parrot
from objects.grass import GrassHandler


class LevelOne(object):
    """First level"""
    def __init__(self, resolution):
        self.parrot = Parrot(resolution)
        self.gravity = Gravity(100)
        self.gravity.add_object(self.parrot)
        self.ground_handlers = {}
        self.ground_handlers["tree"] = TreeHandler(resolution)
        self.ground_handlers["grass"] = GrassHandler(resolution)
        self.ground = Ground(resolution, resolution[0]/1.5, resolution[1]/1.5)
        self.bomb_mgr = BombManager()
        self.distance_traveled = 0.0

    def update(self, delta_time, resolution):
        """logic update for objects in this level/scene"""
        self.gravity.update(delta_time)
        distance_velocity = delta_time*200
        for hnd in self.ground_handlers:
            self.ground_handlers[hnd].move(distance_velocity*-1)
        self.distance_traveled += distance_velocity
        self.parrot.update(delta_time, self.distance_traveled)
        for hnd in self.ground_handlers:
            self.ground_handlers[hnd].update(resolution, self.ground.points[0],
                                             delta_time)
        self.ground.update_ground(self.distance_traveled, resolution)
        self._handle_bombing()

    def draw(self, screen):
        """ draws object in this level/scene"""
        self.parrot.draw(screen)
        self.bomb_mgr.draw_bombs(screen)
        self.ground_handlers["tree"].draw(screen)
        self.ground.draw(screen)
        self.ground_handlers["grass"].draw(screen)

    def dispatch_event(self, event):
        """handles event for this level"""
        self.parrot.control(event)

    def _handle_bombing(self):
        """handles bomb dropping and adds to bomb manager and gravity"""
        bomb = self.parrot.new_bomb()
        if bomb is not None:
            self.gravity.add_object(bomb)
            self.bomb_mgr.add_bomb(bomb)
