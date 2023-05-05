import pygame

from additional.checker import checker_review
from buttons.general import general_btn



def simple_sort(lines, line_width, window, bg_color, sort_button, sort_button_text, sound):
    for i in range(len(lines)):
        sound.play()
        for j in range(len(lines) - 1 - i):
            if lines[j].height > lines[j + 1].height:
                # Swap the positions of the two lines
                lines[j], lines[j + 1] = lines[j + 1], lines[j]
                # Update the x positions of the lines
                for k, line in enumerate(lines):
                    line.x = (k + 1) * line_width
                # Delay the program to slow down the sorting process
                # pygame.time.delay(30)
                # Draw the lines
                window.fill(bg_color)
                for k, line in enumerate(lines):
                    line.draw(window, is_selected=k == j or k == j + 1)
                # Draw the sort button
                general_btn(window, sort_button, sort_button_text, (255, 0, 0))
                pygame.display.update()

    checker_review(window, lines, sound)
