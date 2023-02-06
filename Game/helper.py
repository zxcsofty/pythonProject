from Game.parametrs import *

font_game = pygame.font.match_font('Arial', True, True)
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_game, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


