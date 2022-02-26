import pygame.font
from weapon import Weapon
from pygame.sprite import Group
from sql import work_with_sqlite


class Scores():
    """очки
    """

    def __init__(self,
                 screen,
                 stats):
        """инициализируем подсчет
        """
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_clr = (33,
                         149,
                         243)
        self.font = pygame.font.SysFont(None,
                                        34)
        self.pic_scr()
        self.image_weapon()

    def pic_scr(self):
        """где и как будет находиться очки
        """
        if self.stats.score > work_with_sqlite("score.sqlite").take_record():
            work_with_sqlite("score.sqlite").write(self.stats.score)
        self.img_scr = self.font.render(str(self.stats.score),
                                        True,
                                        self.text_clr,
                                        (0,
                                         0,
                                         0))
        self.score_rect = self.img_scr.get_rect()
        self.score_rect.right = self.screen_rect.right - 30
        self.score_rect.top = 20

        f2 = pygame.font.SysFont('serif',
                                 32)
        self.text2 = f2.render("Рекорд" + str(work_with_sqlite("score.sqlite").take_record()), False,
                               (0,
                                0,
                                255))

        """это для большего фпс в игре, но к сожалению она еще не работает,
         работатем над ним в усердном режиме"""
        # self.handle_events()
        # self.update()
        # self.draw()

        # pygame.display.update()
        # self.clock.tick(self.frame_rate)
        # pygame.display.update()

    def showing_scr(self):
        self.screen.blit(self.img_scr,
                         self.score_rect)
        self.screen.blit(self.text2,
                         (5, 5))
        # self.weapons.draw(self.screen

    def image_weapon(self):
        """рисунок жизней пушки, к сожалению в доработке
        """
        self.weapons = Group()
        for j in range(self.stats.weapons_we_have):
            weapon = Weapon(self.screen)
            weapon.rect.x = 15 + j * weapon.rect.width
            weapon.rect.y = 20
            self.weapons.add(weapon)
