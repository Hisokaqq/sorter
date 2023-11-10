import pygame


def checker_review(window, bg_color, lines, sound):
    window.fill ( bg_color )
    for line in lines :
        line.draw ( window , is_selected=False )
    pygame.display.update ( )
    for k, line in enumerate(lines):
        sound.play()

        line.draw(window, True)
        pygame.time.delay(10)
        pygame.display.update()
