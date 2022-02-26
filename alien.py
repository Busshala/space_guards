import pygame


class Alien(pygame.sprite.Sprite):
    """пришельцы
    """

    def __init__(self,
                 screen):
        """инициализация пришельцев
        """
        super(Alien, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('pictures/alien.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """рисуем пришельца
        """
        self.screen.blit(self.image,
                         self.rect)

    def update(self):
        """перемещение
        """
        self.y += 0.1
        self.rect.y = self.y
