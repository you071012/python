import pygame
from src.game.settings import Settings
from src.game.ship import Ship
from src.game import game_function as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()

    settings = Settings()

    # 设置屏幕大小
    screen = pygame.display.set_mode(size=(settings.screen_width,settings.screen_height))
    #设置主题
    pygame.display.set_caption("Alien Invasion")

    #创建一艘飞船
    ship = Ship(screen)


    while True:
        gf.check_events(ship)
        ship.update()
        gf.upd_screen(settings, screen, ship)

run_game()