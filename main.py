import pygame
import adjustments
from weapon import Weapon
from pygame.sprite import Group
from statistics import Statistics
from rating import Scores
from sql import work_with_sqlite


def running():
    """сам холст (если так можно сказать)
    """
    pygame.init()
    screen = pygame.display.set_mode((700,
                                      720))
    pygame.display.set_caption("Space guard")
    back_gr = (0,
               0,
               0)
    weapon = Weapon(screen)
    bullets = Group()
    aliens = Group()
    adjustments.stack_of_alien(screen,
                               aliens)
    stats = Statistics()
    scr = Scores(screen,
                 stats)

    while True:
        # сами эвенты и все происходящее
        adjustments.events(screen,
                           weapon,
                           bullets)
        if stats.running:
            weapon.moving()
            adjustments.updating(back_gr,
                                 screen,
                                 stats,
                                 scr,
                                 weapon,
                                 aliens,
                                 bullets)
            adjustments.killing_bullets(screen,
                                        stats,
                                        scr,
                                        aliens,
                                        bullets)
            adjustments.updating_position_a(stats,
                                            screen,
                                            scr,
                                            weapon,
                                            aliens,
                                            bullets)


running()
