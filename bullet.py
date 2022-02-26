import pygame


class Bullets(pygame.sprite.Sprite):
    def __init__(self,
                 screen,
                 weapon):
        """инициализация пули
        """
        super(Bullets, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0,
                                0,
                                2,
                                14)
        self.clr = 33, \
                   149, \
                   243
        self.spd = 4
        self.rect.centerx = weapon.rect.centerx
        self.rect.top = weapon.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """обнова пули брат
        """
        self.y -= self.spd
        self.rect.y = self.y

    def drawing_bullet(self):
        """рисуем пулю лол
        """
        pygame.draw.rect(self.screen,
                         self.clr,
                         self.rect)
