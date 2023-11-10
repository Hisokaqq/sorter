import pygame
from buttons.general import general_btn

def merge_sort(lines, line_width, window, bg_color, sort_button, sort_button_text, sound):
    merge_sort_helper(lines, line_width, window, bg_color, sort_button, sort_button_text, sound, 0, len(lines) - 1)

def merge_sort_helper(lines, line_width, window, bg_color, sort_button, sort_button_text, sound, start, end):
    if start < end:
        mid = (start + end) // 2

        merge_sort_helper(lines, line_width, window, bg_color, sort_button, sort_button_text, sound, start, mid)
        merge_sort_helper(lines, line_width, window, bg_color, sort_button, sort_button_text, sound, mid + 1, end)

        merge(lines, line_width, window, bg_color, sort_button, sort_button_text, sound, start, mid, end)

def merge(lines, line_width, window, bg_color, sort_button, sort_button_text, sound, start, mid, end):
    left_half = lines[start:mid + 1]
    right_half = lines[mid + 1:end + 1]

    left_index = right_index = 0
    merge_index = start

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index].height <= right_half[right_index].height:
            lines[merge_index] = left_half[left_index]
            left_index += 1
        else:
            lines[merge_index] = right_half[right_index]
            right_index += 1
        merge_index += 1

    while left_index < len(left_half):
        lines[merge_index] = left_half[left_index]
        left_index += 1
        merge_index += 1

    while right_index < len(right_half):
        lines[merge_index] = right_half[right_index]
        right_index += 1
        merge_index += 1

    # Update the positions of lines
    for k, line in enumerate(lines[start:end + 1]):
        line.x = (start + k + 1) * line_width

    # Redraw the window
    window.fill(bg_color)
    for k, line in enumerate(lines):
        line.draw(window, is_selected=(start <= k <= end))
    general_btn(window, sort_button, sort_button_text, (255, 0, 0))
    pygame.display.update()

    # Add a delay to visualize the sorting process
    pygame.time.delay(100)  # Adjust the delay time (in milliseconds) as needed

    # Play sound
    sound.play()

# Call the merge_sort function instead of bubble_sort