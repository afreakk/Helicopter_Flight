"""manages BOMBS!"""


class BombManager(object):
    """manages bombs"""
    def __init__(self):
        self.bombs = []

    def draw_bombs(self, screen):
        """draws bombs in list"""
        for bomb in self.bombs:
            bomb.draw(screen)

    def add_bomb(self, bomb):
        """adds bomb to list"""
        self.bombs.append(bomb)
