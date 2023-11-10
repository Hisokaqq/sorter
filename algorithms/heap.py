import pygame
from buttons.general import general_btn

def heapify(arr, n, i, window, bg_color, line_width, sorting_button, sorting_button_text, sound):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if left child exists and is greater than root
    if left < n and arr[largest].height < arr[left].height:
        largest = left

    # Check if right child exists and is greater than largest so far
    if right < n and arr[largest].height < arr[right].height:
        largest = right

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        update_display(arr, window, bg_color, line_width, sorting_button, sorting_button_text, sound, i, largest)
        heapify(arr, n, largest, window, bg_color, line_width, sorting_button, sorting_button_text, sound)

def heap_sort(arr, window, bg_color, line_width, sorting_button, sorting_button_text, sound):
    n = len(arr)

    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, window, bg_color, line_width, sorting_button, sorting_button_text, sound)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        update_display(arr, window, bg_color, line_width, sorting_button, sorting_button_text, sound, i, 0)
        heapify(arr, i, 0, window, bg_color, line_width, sorting_button, sorting_button_text, sound)


def update_display(arr, window, bg_color, line_width, sorting_button, sorting_button_text, sound, index1=None, index2=None):
    window.fill(bg_color)
    for k, line in enumerate(arr):
        line.x = (k + 1) * line_width
        is_selected = (k == index1 or k == index2)
        line.draw(window, is_selected=is_selected)
    general_btn(window, sorting_button, sorting_button_text, (255, 0, 0))
    pygame.display.update()
    sound.play()
    pygame.time.delay(10)

# To use heap_sort
