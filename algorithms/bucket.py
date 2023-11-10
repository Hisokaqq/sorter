import pygame
from buttons.general import general_btn

def insertion_sort_bucket(arr):
    for i in range(1, len(arr)):
        up = arr[i]
        j = i - 1
        while j >= 0 and arr[j].height > up.height:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = up
    return arr

def bucket_sort(lines, line_width, window, bg_color, sorting_button, sorting_button_text, sound):
    max_height = max(line.height for line in lines)
    size = len(lines)
    buckets = [[] for _ in range(size)]

    # Put array elements in different buckets
    for i in range(size):
        index = int(size * lines[i].height / (max_height + 1))
        buckets[index].append(lines[i])

    # Sort individual buckets and concatenate
    new_idx = 0
    for i in range(size):
        buckets[i] = insertion_sort_bucket(buckets[i])
        for j in range(len(buckets[i])):
            lines[new_idx] = buckets[i][j]
            lines[new_idx].x = (new_idx + 1) * line_width
            update_display(lines, window, bg_color, line_width, sorting_button, sorting_button_text, sound,
                           current_index=new_idx)
            new_idx += 1



def update_display(lines, window, bg_color, line_width, sorting_button, sorting_button_text, sound, current_index=None, delay=20):
    window.fill(bg_color)
    for k, line in enumerate(lines):
        is_selected = (k == current_index)
        line.draw(window, is_selected=is_selected)
    general_btn(window, sorting_button, sorting_button_text, (255, 0, 0))
    pygame.display.update()
    sound.play()
    pygame.time.delay(delay)  # Delay in milliseconds


# To use bucket_sort, call it like this in your event handling section where the sorting button is clicked:
# bucket_sort(lines, line_width, window, bg_color, sorting_button, sorting_button_text, sound)
