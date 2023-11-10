import pygame
from buttons.general import general_btn

def selection_sort(lines, line_width, window, bg_color, sort_button, sort_button_text, sound):
    for i in range(len(lines)):
        sound.play()
        min_index = i
        for j in range(i+1, len(lines)):
            if lines[j].height < lines[min_index].height:
                min_index = j
        if min_index != i:
            # Swap the positions of the two lines
            lines[i], lines[min_index] = lines[min_index], lines[i]
            # Update the x positions of the lines
            for k, line in enumerate(lines):
                line.x = (k + 1) * line_width
            # Delay the program to slow down the sorting process
            pygame.time.delay(30)  # Pause for 30 milliseconds
            # Draw the lines
            window.fill(bg_color)
            for k, line in enumerate(lines):
                line.draw(window, is_selected=k == i or k == min_index)
            # Draw the sort button
            general_btn(window, sort_button, sort_button_text, (255, 0, 0))
            pygame.display.update()