"""game about a helicopter"""
import pygame
from core.utils import translate
from objects.parrotvertex import get_parrot


class Parrot(object):
    """Parrot that player controls"""
    def __init__(self):
        self.points = get_parrot()
        self.color = (255, 255, 255)
        self.ctrlup = False
        self.ctrldown = False
        self.up_pwr = 200.0
        self.down_pwr = 100.0
        self.loc_translate(350, 250)

    def draw(self, screen):
        """draws the helicopter on screen"""
        for points in self.points:
            pygame.draw.polygon(screen, self.color, points)

    def update(self, delta_time):
        """updates helicopter physics etc"""
        if self.ctrlup:
            self.loc_translate(0.0, delta_time*-self.up_pwr)
        if self.ctrldown:
            self.loc_translate(0.0, delta_time*self.down_pwr)

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

    def loc_translate(self, x_velocity, y_velocity):
        """local self.points translate"""
        for points in self.points:
            translate(x_velocity, y_velocity, points)
