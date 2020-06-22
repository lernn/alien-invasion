import sys
import pygame
from bullet import Bulluet
from alien import Alien
from time import sleep

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings,screen, aliens,stats, play_button, ship,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 注意quit大小写的用法区别
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,aliens,ship,stats,bullets,play_button,mouse_x,mouse_y)


def check_play_button(ai_settings,screen,aliens,ship,stats, bullets, play_button, mouse_x, mouse_y):
    botton_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if botton_clicked and not stats.game_active:
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings,screen,aliens,ship)
        ship.center_ship()


def update_screen(ai_settings,screen, stats, a_ship, bullets, aliens, play_button):  #如何确定重构后的函数需要哪些参数
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    a_ship.blitme()
    aliens.draw(screen)
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()


def update_bullets(ai_setting,screen,aliens,ship,bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_setting,screen,aliens,ship)


def fire_bullet(ai_settings,screen,ship,bullets):
    if len(bullets) < ai_settings.bullets_num:
        new_bullet = Bulluet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def get_num_x(ai_settings,alien_width):
    alien_num_x = int((ai_settings.screen_width - 2 * alien_width) / (2 * alien_width))
    return alien_num_x


def get_num_y(ai_settings,aline_height,ship_height):
    alien_num_y = int((ai_settings.screen_height - 3 * aline_height - ship_height ) / (2 * aline_height))
    return alien_num_y


def creat_alien(ai_settings, screen,aliens,alien_num_x,alien_num_y):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width + alien_num_x * 2 * alien_width
    alien.y = alien_height + alien_num_y * 2 * alien_height
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)


def create_fleet(ai_settings,screen,aliens,ship):
    alien = Alien(ai_settings, screen)
    alien_num_x = get_num_x(ai_settings,alien.rect.width)
    alien_num_y = get_num_y(ai_settings, alien.rect.height,ship.rect.height)
    for alien_numy in range(alien_num_y):
        for alien_numx in range(alien_num_x):
            creat_alien(ai_settings,screen,aliens,alien_numx,alien_numy)


def change_fleet_direction(ai_setting,aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_setting.fleet_drop_speed
    ai_setting.fleet_direction *= -1


def check_fleet_edges(ai_setting,aliens):
    for alien in aliens.sprites():
        if alien.check_edge():
            change_fleet_direction(ai_setting,aliens)
            break


def check_aliens_bottom(ai_settings, game_stats, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, game_stats, screen, ship, aliens, bullets)
            break


def update_aliens(ai_setting, game_stats, screen, ship, aliens, bullets):#为什么能直接更新所有alien
    # if game_stats.ship_left > 0:
        check_fleet_edges(ai_setting, aliens)
        aliens.update()
        check_aliens_bottom(ai_setting,game_stats,screen,ship,aliens,bullets)
        if pygame.sprite.spritecollideany(ship, aliens):
            ship_hit(ai_setting, game_stats, screen, ship, aliens, bullets)
    # else:
    #     game_stats.game_active = False


def ship_hit(ai_settings,game_stats,screen,ship,aliens,bullets):
    aliens.empty()
    bullets.empty()
    create_fleet(ai_settings, screen, aliens, ship)
    ship.center_ship()
    sleep(0.5)
    if game_stats.ship_left > 0:
        game_stats.ship_left -= 1
    else:
        game_stats.game_active = False
        pygame.mouse.set_visible(True)







