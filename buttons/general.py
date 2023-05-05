import pygame


def general_btn(window, rect, text, color):
    pygame.draw.rect(window,color , rect)
    window.blit(text, (rect.centerx - text.get_width() / 2,
                       rect.centery - text.get_height() / 2))
