import pygame
from buttons.general import general_btn

def quick_sort(arr, low, high, window, bg_color, line_width, sorting_button, sorting_button_text, sound):
    if low < high:
        pi = partition(arr, low, high, window, bg_color, line_width, sorting_button, sorting_button_text, sound)
        quick_sort(arr, low, pi - 1, window, bg_color, line_width, sorting_button, sorting_button_text, sound)
        quick_sort(arr, pi + 1, high, window, bg_color, line_width, sorting_button, sorting_button_text, sound)


def partition(arr, low, high, window, bg_color, line_width, sorting_button, sorting_button_text, sound):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j].height <= pivot.height:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            update_display(arr, window, bg_color, line_width, sorting_button, sorting_button_text, sound, i, j)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    update_display(arr, window, bg_color, line_width, sorting_button, sorting_button_text, sound, i + 1, high)
    return i + 1

def update_display(arr, window, bg_color, line_width, sorting_button, sorting_button_text, sound, index1, index2):
    window.fill(bg_color)
    for k, line in enumerate(arr):
        line.x = (k + 1) * line_width
        if k == index1 or k == index2:
            line.draw(window, is_selected=True)  # Draw current line in red
        else:
            line.draw(window)
    general_btn(window, sorting_button, sorting_button_text, (255, 0, 0))
    pygame.display.update()
    sound.play()
    pygame.time.delay(20)  # Delay in milliseconds for better visualization

# To use quick_sort, call it like this in your main loop or event handling section:
# quick_sort(lines
