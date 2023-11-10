import pygame
from buttons.general import general_btn

def insertion_sort(lines, line_width, window, bg_color, sort_button, sort_button_text, sound):
    for i in range(1, len(lines)):
        sound.play()
        key = lines[i]
        j = i - 1
        while j >= 0 and lines[j].height > key.height:
            lines[j + 1] = lines[j]
            j -= 1
        lines[j + 1] = key

        # Update the x positions of the lines
        for k, line in enumerate(lines):
            line.x = (k + 1) * line_width

        # Delay the program to slow down the sorting process
        pygame.time.delay(30)  # Pause for 30 milliseconds

        # Draw the lines
        window.fill(bg_color)
        for k, line in enumerate(lines):
            line.draw(window, is_selected=k == j + 1)
        # Draw the sort button
        general_btn(window, sort_button, sort_button_text, (255, 0, 0))
        pygame.display.update()



