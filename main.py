"""Entry point for parrot--game"""
import pygame
import sys
from objects.parrot import Parrot
from core.gravity import Gravity
from core.foreground import ForgeGround


def get_deltatime(clock):
    """gets delta time"""
    mill_sec = clock.tick()
    return mill_sec / 1000.0


def main():
    """Entry point"""
    pygame.init()
    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Racketeeeeerz")
    clock = pygame.time.Clock()
    running = True
    parrot = Parrot()
    gravity = Gravity(100)
    gravity.add_parrot(parrot)
    fore_ground = ForgeGround(width, height)
    while running:
        delta_time = get_deltatime(clock)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            parrot.control(event)
        parrot.update(delta_time)
        gravity.update(delta_time)
        screen.fill((0, 0, 255))
        parrot.draw(screen)
        fore_ground.draw(screen)
        pygame.display.flip()
        fore_ground.move(delta_time*-2000)
        fore_ground.update_positions(width, height)

if __name__ == '__main__':
    sys.exit(main())
