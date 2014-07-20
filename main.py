"""Entry point for parrot--game"""
import pygame
import sys
from core.utils import get_deltatime
from lvls.lvlone import LevelOne


class HelicopterGame(object):
    """Bottom of stack.. Top layer of this game"""
    def __init__(self, resolution):
        pygame.init()
        pygame.display.set_caption("Helicopter-Simulator:)")
        self.resolution = resolution
        self.screen = pygame.display.set_mode(self.resolution)
        self.clock = pygame.time.Clock()
        self.running = True
        self.lvl = None

    def handle_event(self):
        """Takes event and uses it for stuff"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            self.lvl.dispatch_event(event)
            print "FPS:", self.clock.get_fps()

    def update_level(self):
        """updates current level"""
        delta_time = get_deltatime(self.clock)
        self.lvl.update(delta_time, self.resolution)

    def draw_level(self):
        """draws current level"""
        self.screen.fill((0, 0, 255))
        self.lvl.draw(self.screen)
        pygame.display.flip()


def game_loop(app):
    """Main_game_loop"""
    while app.running:
        app.handle_event()
        app.update_level()
        app.draw_level()

if __name__ == '__main__':
    APP = HelicopterGame((800, 600))
    APP.lvl = LevelOne(APP.resolution)
    sys.exit(game_loop(APP))
