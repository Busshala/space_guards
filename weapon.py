import pygame
from pygame.sprite import Sprite


class Weapon(Sprite):

    def __init__(self,
                 screen):
        """инициализация пуууушшшшшки
        """
        super(Weapon, self).__init__()
        self.screen = screen
        self.picture = pygame.image.load('pictures/gun.png')
        self.rect = self.picture.get_rect()
        self.scr_rect = screen.get_rect()
        self.rect.centerx = self.scr_rect.centerx
        self.rect.bottom = self.scr_rect.bottom
        self.center = float(self.rect.centerx)
        self.moving_to_right = False
        self.moving_to_left = False

    def drawing(self):
        """рисуем пушшшшшку
        """
        self.screen.blit(self.picture,
                         self.rect)

    def moving(self):
        """движение пушшшшки
        """
        if self.moving_to_right and self.rect.right \
                < self.scr_rect.right + 10:
            self.center += 1.5
        if self.moving_to_left and self.rect.left > -10:
            self.center -= 1.5

        self.rect.centerx = self.center

    def resistance(self):
        """вы проиграли и появляется новая пушка лол капец ты геймер конечно
        """
        self.center = self.scr_rect.centerx
