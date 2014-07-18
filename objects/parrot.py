"""game about a helicopter"""
import pygame
from objects.parrotvertex import get_parrot, get_bomb
from objects.baseobj import BaseObj
from core.utils import vector_div, vector_add


class Parrot(BaseObj):
    """Parrot that player controls"""
    def __init__(self, resolution):
        self.blade_length = 50
        self.blade_width = 10
        self.pin_height = 10
        self.pin_width = 5
        self.house_width = 35
        self.house_height = 40
        BaseObj.__init__(self, self._get_parrot(0), (255, 0, 0))
        self.ctrlup = False
        self.ctrldown = False
        self.up_pwr = 200.0
        self.down_pwr = 100.0
        self.do_bomb = False
        screen_mid = vector_div(resolution, 2)
        self.loc_translate(screen_mid)
        self.blade_clr = (100, 100, 100)
        self.pin_clr = (0, 0, 0)
        self.house_clr = (200, 10, 10)

    def get_height(self):
        """total height of helicopter"""
        return self.house_height+self.pin_height

    def update(self, delta_time, distance_traveled):
        """updates helicopter physics etc"""
        self.update_points(self._get_parrot(distance_traveled))
        if self.ctrlup:
            self.loc_translate((0.0, delta_time*-self.up_pwr))
        if self.ctrldown:
            self.loc_translate((0.0, delta_time*self.down_pwr))

    def control(self, event):
        """ takes event from pygame and controls parrot"""
        if event.type == pygame.KEYUP:
            self._set_dir(event.key, False)
            self._set_bomb_trigger(event.key, False)
        elif event.type == pygame.KEYDOWN:
            self._set_dir(event.key, True)
            self._set_bomb_trigger(event.key, True)

    def new_bomb(self):
        """player has launched new bomb? if so returns new bomb else None"""
        if self.do_bomb:
            self.do_bomb = False
            bomb = Bomb()
            helicopter_offset = (self.blade_width/2, self.get_height()*2+1)
            bomb_position = vector_add(self.position, helicopter_offset)
            bomb.loc_translate(bomb_position)
            return bomb
        return None

    def _set_dir(self, key, value):
        """steering"""
        if key == pygame.K_w:
            self.ctrlup = value
        elif key == pygame.K_s:
            self.ctrldown = value

    def _set_bomb_trigger(self, key, value):
        """handle bomb dropping"""
        if key == pygame.K_SPACE:
            self.do_bomb = value

    def _get_parrot(self, distance_traveled):
        """gets parrot at distance_traveled  - distance traveled"""
        return get_parrot(self.blade_length, self.blade_width, self.pin_height,
                          self.pin_width, self.house_width, self.house_height,
                          distance_traveled)

    def draw(self, screen):
        """draws the helicopter on screen"""
        blade, pin, house = self.points
        pygame.draw.polygon(screen, self.house_clr, house)
        pygame.draw.polygon(screen, self.pin_clr, pin)
        pygame.draw.polygon(screen, self.blade_clr, blade)


class Bomb(BaseObj):
    """Bomb that player drops"""
    def __init__(self):
        self.tail_length = 10
        self.base_length = 20
        self.tail_width = 10
        self.tip_width = 5
        self.base_width = 5
        self.tip_length = 10
        BaseObj.__init__(self,
                         get_bomb(self.tail_length, self.base_length,
                                  self.tail_width,
                                  self.tip_width,
                                  self.base_width,
                                  self.tip_length,),
                         (0, 0, 0))

    def get_width(self):
        """width of bomb"""
        return self.tip_width+self.base_width+self.tail_width

    def get_height(self):
        """height of bomb"""
        return self.tip_length+self.base_length+self.tail_length
