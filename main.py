from parametrs import *
from Levels.level_1 import start_level_1
from Levels.level_2 import start_level_2

# игровое окно
pygame.init()  # запуск pygame
pygame.mixer.init()  # запуск работы звука
pygame.display.set_caption("Моя первая игра")  # заголовок
# pygame.display.set_icon(icon)

start_level_1()
# первый уровень
start_level_2() # запуск 2 уровня

