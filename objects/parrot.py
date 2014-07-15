"""game about a helicopter"""
import pygame
from objects.parrotvertex import get_parrot
from objects.baseobj import BaseObj
from core.utils import vector_div


class Parrot(BaseObj):
    """Parrot that player controls"""
    def __init__(self, resolution):
        BaseObj.__init__(self, get_parrot())
        self.color = (255, 255, 255)
        self.ctrlup = False
        self.ctrldown = False
        self.up_pwr = 200.0
        self.down_pwr = 100.0
        screen_mid = vector_div(resolution, 2)
        self.loc_translate(screen_mid)

    def draw(self, screen):
        """draws the helicopter on screen"""
        for points in self.points:
            pygame.draw.polygon(screen, self.color, points)

    def update(self, delta_time):
        """updates helicopter physics etc"""
        if self.ctrlup:
            self.loc_translate((0.0, delta_time*-self.up_pwr))
        if self.ctrldown:
            self.loc_translate((0.0, delta_time*self.down_pwr))

    def control(self, event):
        """ takes event from pygame and controls parrot"""
        if event.type == pygame.KEYUP:
            self._set_dir(event.key, False)
        elif event.type == pygame.KEYDOWN:
            self._set_dir(event.key, True)

    def _set_dir(self, key, value):
        """steering"""
        if key == pygame.K_w:
            self.ctrlup = value
        elif key == pygame.K_s:
            self.ctrldown = value
