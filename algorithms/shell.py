import pygame
from buttons.general import general_btn


def shell_sort(lines, line_width, window, bg_color, sorting_button, sorting_button_text, sound):
    n = len(lines)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = lines[i]
            j = i
            while j >= gap and lines[j - gap].height > temp.height:
                lines[j] = lines[j - gap]
                lines[j].x = (j + 1) * line_width
                update_display(lines, window, bg_color, line_width, sorting_button, sorting_button_text, sound,
                               current_index=j)
                j -= gap
            lines[j] = temp
            lines[j].x = (j + 1) * line_width
            update_display(lines, window, bg_color, line_width, sorting_button, sorting_button_text, sound,
                           current_index=j)
        gap //= 2





def update_display(arr, window, bg_color, line_width, sorting_button, sorting_button_text, sound, current_index=None):
    window.fill(bg_color)
    for k, line in enumerate(arr):
        line.x = (k + 1) * line_width
        is_selected = (k == current_index)
        line.draw(window, is_selected=is_selected)
    general_btn(window, sorting_button, sorting_button_text, (255, 0, 0))
    pygame.display.update()
    sound.play()
    pygame.time.delay(10)


# To use heap_sort
