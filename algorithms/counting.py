import pygame
from buttons.general import general_btn


def counting_sort(lines, window, bg_color, line_width, sorting_button, sorting_button_text, sound):
    max_height = max(line.height for line in lines)  # Find the maximum height
    count = [0] * (max_height + 1)

    # Store the count of each height
    for line in lines:
        count[line.height] += 1

    # Change count[i] so that it now contains actual position of this height in output array
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Build the output line array
    output = [None] * len(lines)
    for line in reversed(lines):
        output[count[line.height] - 1] = line
        count[line.height] -= 1
        update_display(output, window, bg_color, line_width, sorting_button, sorting_button_text, sound)

    # Copy the output array to lines, so that lines now contains sorted lines
    for i, line in enumerate(output):
        lines[i] = line
        lines[i].x = (i + 1) * line_width  # Adjust the x position of each line



def update_display(arr, window, bg_color, line_width, sorting_button, sorting_button_text, sound):
    window.fill(bg_color)
    for k, line in enumerate(arr):
        if line:
            line.x = (k + 1) * line_width
            line.draw(window)
    general_btn(window, sorting_button, sorting_button_text, (255, 0, 0))
    pygame.display.update()
    sound.play()
    pygame.time.delay(20)

