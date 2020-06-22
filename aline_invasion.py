
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from buttom import Button

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(screen,"Play")
    a_ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()
    stats = GameStats(ai_settings)
    gf.create_fleet(ai_settings,screen,aliens,a_ship)

#循环主体
    while True:
        gf.check_events(ai_settings, screen,aliens, stats, play_button, a_ship, bullets)
        if stats.game_active:
            a_ship.update()
            gf.update_bullets(ai_settings,screen,aliens,a_ship,bullets,)
            gf.update_aliens(ai_settings, stats, screen,a_ship,aliens,bullets)
        gf.update_screen(ai_settings, screen, stats, a_ship, bullets, aliens,play_button)


run_game()