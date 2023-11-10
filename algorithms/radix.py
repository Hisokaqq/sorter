import pygame
from buttons.general import general_btn

def counting_sort_for_radix(lines, exp, window, bg_color, line_width, sorting_button, sorting_button_text, sound):
    n = len(lines)
    output = [None] * n
    count = [0] * 10

    # Store count of occurrences in count[]
    for i in range(n):
        index = lines[i].height // exp
        count[index % 10] += 1

    # Change count[i] so that count[i] contains actual position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = lines[i].height // exp
        output[count[index % 10] - 1] = lines[i]
        count[index % 10] -= 1
        i -= 1

    # Copying the output array to lines, so that lines contains sorted numbers
    for i in range(len(lines)):
        lines[i] = output[i]
        lines[i].x = (i + 1) * line_width  # Adjust the x position of each line
        update_display(lines, window, bg_color, line_width, sorting_button, sorting_button_text, sound, current_index=i)

def radix_sort(lines, line_width, window, bg_color, sorting_button, sorting_button_text, sound):
    # Find the maximum number to know the number of digits
    max_height = max(line.height for line in lines)

    # Do counting sort for every digit. Note that instead of passing digit number, exp is passed.
    # exp is 10^i where i is current digit number
    exp = 1
    while max_height / exp > 1:
        counting_sort_for_radix(lines, exp, window, bg_color, line_width, sorting_button, sorting_button_text, sound)
        exp *= 10


def update_display(lines, window, bg_color, line_width, sorting_button, sorting_button_text, sound, current_index=None):
    window.fill(bg_color)
    for k, line in enumerate(lines):
        is_selected = (k == current_index)
        line.draw(window, is_selected=is_selected)
    general_btn(window, sorting_button, sorting_button_text, (255, 0, 0))
    pygame.display.update()
    sound.play()
    pygame.time.delay(20)
