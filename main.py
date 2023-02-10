from parametrs import *
from Levels.level_1 import start_level_1
from Levels.level_2 import start_level_2
from Levels.level_3 import start_level_3
from Levels.level_4 import start_level_4

# игровое окно
pygame.init()  # запуск pygame
pygame.mixer.init()  # запуск работы звука
pygame.display.set_caption("Моя первая игра")  # заголовок
# pygame.display.set_icon(icon)

# start_level_1()
# start_level_2()
#start_level_3()
start_level_4()