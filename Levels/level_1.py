import time
import pygame
from helper import *
from parametrs import *
from sprites import Player, Coin

screen = pygame.display.set_mode((WIDTH, HEIGHT))  # размер дисплея
clock = pygame.time.Clock()  # переменная для работы с частотой кадров

# группы спрайтов
players_sprites = pygame.sprite.Group()  # создаю группу спрайтов
player = Player()  # создаю спрайт героя
players_sprites.add(player)  # добавляю спрайт в группу

items_sprites = pygame.sprite.Group()  # группа спрайтов для предметов для сбора
coin = Coin()  # создадим монетку
items_sprites.add(coin)  # добавим монетку к группе спрайтов

def start_level_1():
    running = True  # переменная для запуска игрового цикла
    pause = True
    score = 0

    while running:  # запуск игрового цикла
        # контроль FPS
        clock.tick(FPS)

        # обновление спрайтов
        players_sprites.update()

        # отрисовка
        screen.blit(bg, (0, 0))
        players_sprites.draw(screen)  # отрисовка персонажа на экране
        items_sprites.draw(screen)  # отрисовка монетки на экране
        draw_text(screen, f'Счёт:{str(score)}', 50, WIDTH / 2, 10)

        # обработка событий
        # проверка на сбор монет
        if pygame.sprite.spritecollide(player, items_sprites, False):
            score += 1
            items_sprites.update()

        for event in pygame.event.get():
            # проверка на закрытие игры
            if event.type == pygame.QUIT:
                running = False
            # проверка на нажатие клавиш
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.direction = "LEFT"
                if event.key == pygame.K_w:
                    player.direction = "TOP"
                if event.key == pygame.K_d:
                    player.direction = "RIGHT"
                if event.key == pygame.K_s:
                    player.direction = "BOTTOM"

        if score >= 10:
            draw_text(screen, f'Уровень пройден', 100, WIDTH / 2, HEIGHT / 2)
            pygame.display.flip()
            time.sleep(5)
            running = False
        else:
            if pause == True:
                draw_text(screen, f'Уровень 1', 100, WIDTH / 2, HEIGHT / 2)
                # после отрисовки, переворачиваем экран
                pygame.display.flip()
                time.sleep(1)
                pause = False
            else:
                pygame.display.flip()

