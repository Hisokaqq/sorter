import pygame


def checker_review(window, lines, sound):
    for k, line in enumerate(lines):
        sound.play()

        line.draw(window, True)
        pygame.time.delay(30)
        pygame.display.update()
