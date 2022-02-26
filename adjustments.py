import pygame
import sys
from bullet import Bullets
from alien import Alien
import time
from sql import work_with_sqlite
from statistics import Statistics


def events(screen,
           weapon,
           bullets):
    """обрабатываем события
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            # двигаемся вправо
            if event.key == pygame.K_RIGHT:
                weapon.moving_to_right = True
            elif event.key == pygame.K_LEFT:
                weapon.moving_to_left = True
            elif event.key == pygame.K_SPACE:
                newbullet = Bullets(screen,
                                    weapon)
                bullets.add(newbullet)
        elif event.type == pygame.KEYUP:
            # тоже вправо
            if event.key == pygame.K_RIGHT:
                weapon.moving_to_right = False
            elif event.key == pygame.K_LEFT:
                weapon.moving_to_left = False


def updating(back_gr,
             screen,
             stats,
             scr,
             weapon,
             aliens,
             bullets):
    """обновляем экранчик
    """
    # work_with_sqlite("score.sqlite").write(str(stats))
    screen.fill(back_gr)
    scr.showing_scr()
    for bullet in bullets.sprites():
        bullet.drawing_bullet()
    weapon.drawing()
    aliens.draw(screen)
    pygame.display.flip()


def death_weapon(stats,
                 screen,
                 scr,
                 weapon,
                 aliens,
                 bullets):
    """говорим, когда умирает пушка
    """
    if stats.weapons_we_have > 0:
        stats.weapons_we_have -= 1

        # тут у него отнимаются жизки
        # еще у него отнимаются очки, чтобы всем игрокам в игре было комфортно

        aliens.empty()
        bullets.empty()
        stack_of_alien(screen,
                       aliens)
        weapon.resistance()
        stats.score = 0
        time.sleep(1)
        # создаем новую армию, очищая пули и пришельцев, еще устанавливаем делэй
    else:
        stats.running = False
        sys.exit()


def ali_checking(stats,
                 screen,
                 scr,
                 weapon,
                 aliens,
                 bullets):
    """чекаем, если пришкльцы не коснулись пушшшшки, но прошли его стороной и жошли до края карты,
     а это нам не очень то и нужно, тем самфм я подключаею к этому методу метод death_weapon,
     чтобы очистить карту, и даже если одинг пришелец пройдет, то все обновится
     """
    screen_rect = screen.get_rect()
    for i in aliens.sprites():
        if i.rect.bottom >= screen_rect.bottom:
            death_weapon(stats,
                         screen,
                         scr,
                         weapon,
                         aliens,
                         bullets)
            break


def killing_bullets(screen,
                    stats,
                    scr,
                    aliens,
                    bullets):
    """тут говорим что вот пуля достигла пришельцев и его и пришельцев нужно убрать, а также если мы выиграли,
     то пули очищаются и идет переход к методу stack_of_alien
     """
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    coll = pygame.sprite.groupcollide(bullets,
                                      aliens,
                                      True,
                                      True)
    # для доработок
    # pygame.font.init()
    # self.surface = pygame.display.set_mode((width, height))
    # pygame.display.set_caption(caption)
    # self.clock = pygame.time.Clock()
    # self.keydown_handlers = defaultdict(list)
    # self.keyup_handlers = defaultdict(list)
    # self.mouse_handlers = []

    # прибавляем очки
    if coll:
        for aliens in coll.values():
            stats.score += 1 * len(aliens)
        scr.pic_scr()

    if len(aliens) == 0:
        bullets.empty()
        stack_of_alien(screen,
                       aliens)
        stats.score = 0

        # all_sprites = pygame.sprite.Group()
        # all_sprites.add(PT1)
        # all_sprites.add(P1)

        # platforms = pygame.sprite.Group()
        # platforms.add(PT1)


def updating_position_a(stats,
                        screen,
                        scr,
                        weapon,
                        aliens,
                        bullets):
    """просто обновление позиции пришельцев
    """
    aliens.update()
    if pygame.sprite.spritecollideany(weapon,
                                      aliens):
        death_weapon(stats,
                     screen,
                     scr,
                     weapon,
                     aliens,
                     bullets)
    ali_checking(stats,
                 screen,
                 scr,
                 weapon,
                 aliens,
                 bullets)

    # elif event.type == pygame.KEYDOWN:
    # for handler in self.keydown_handlers[event.key]:
    # handler(event.key)
    # elif event.type == pygame.KEYUP:
    # for handler in self.keydown_handlers[event.key]:
    # handler(event.key)
    # elif event.type in (pygame.MOUSEBUTTONDOWN,
    # pygame.MOUSEBUTTONUP,
    # pygame.MOUSEMOTION):
    # for handler in self.mouse_handlers:
    # handler(event.type, event.pos)


def stack_of_alien(screen,
                   aliens):
    """тут сама армия пришельцев создается, сначала создаем его по x-у, а потом по у-ку,
     и просто проходимся фориком по этому количеству
     """
    alieen = Alien(screen)
    alien_wdth = alieen.rect.width
    amount_of_alix = int((700 - 2 * alien_wdth)
                         / alien_wdth)
    alien_height = alieen.rect.height
    amount_of_aliy = int((720 - 100 - 2 * alien_height)
                         / alien_height)

    # тут создаем пришельцев
    for j in range(amount_of_aliy - 1):
        for i in range(amount_of_alix):
            alieen = Alien(screen)
            alieen.x = alien_wdth \
                       + (alien_wdth * i)
            alieen.y = alien_height \
                       + (alien_height * j)
            alieen.rect.x = alieen.x
            alieen.rect.y = alieen.rect.height \
                            + alieen.rect.height * j
            aliens.add(alieen)
