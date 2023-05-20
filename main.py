import pygame
import random

from algorithms.bubble import bubble_sort
from algorithms.selection import selection_sort
from algorithms.insertion import insertion_sort
from algorithms.merge import merge_sort

from buttons.general import general_btn

# Initialize Pygame
pygame.mixer.init()
pygame.init()
sound = pygame.mixer.Sound("sound effects/td.mp3")

# Set the dimensions of the window
window_width = 1200
window_height = 800

# Create the window
window = pygame.display.set_mode((window_width, window_height))

# Set the title of the window
pygame.display.set_caption("Sorter")

# Set the background color of the window
bg_color = (255, 255, 255)

line_width = 10


class Line:
    def __init__(self, x, y, height):
        self.x = x
        self.y = y
        self.height = height
        self.width = line_width
        self.color = (0, 0, 0)  # Black

    def draw(self, surface, is_selected=False):
        if is_selected:
            color = (255, 0, 0)  # Red
        else:
            color = self.color
        pygame.draw.rect(surface, color, (self.x, self.y, self.width, self.height))


# Create a list of Line objects
lines = []
for i in range(int(window_width / line_width - 2)):
    height = random.randint(line_width, 500)
    x = (i + 1) * line_width
    y = window_height - height
    line = Line(x, y, height)
    lines.append(line)

# Create a font object for the button text
font = pygame.font.Font(None, 28)

# Create buttons
bubble_button = pygame.Rect(window_width - 135, 10, 125, 40)
bubble_button_text = font.render("Bubble", True, (255, 255, 255))
selection_button = pygame.Rect(window_width - 135 - 125 - 10, 10, 125, 40)
selection_button_text = font.render("Selection", True, (255, 255, 255))
insertion_button = pygame.Rect(window_width - 135 - 125 - 10 - 125 - 10, 10, 125, 40)
insertion_button_text = font.render("Insertion", True, (255, 255, 255))
merge_button = pygame.Rect(window_width - 135 - 125 - 10 - 125 - 10 - 125 - 10, 10, 125, 40)
merge_button_text = font.render("Merge", True, (255, 255, 255))
quick_button = pygame.Rect(window_width - 135 - 125 - 10 - 125 - 10 - 125 - 10 - 125 - 10, 10, 125, 40)
quick_button_text = font.render("Quick", True, (255, 255, 255))
counting_button = pygame.Rect(window_width - 135, 60, 125, 40)
counting_button_text = font.render("Counting", True, (255, 255, 255))
radix_button = pygame.Rect(window_width - 135 - 125 - 10, 60, 125, 40)
radix_button_text = font.render("Radix", True, (255, 255, 255))
bucket_button = pygame.Rect(window_width - 135 - 125 - 10 - 125 - 10, 60, 125, 40)
bucket_button_text = font.render("Bucket", True, (255, 255, 255))
heap_button = pygame.Rect(window_width - 135 - 125 - 10 - 125 - 10 - 125 - 10 , 60, 125, 40)
heap_button_text = font.render("Heap", True, (255, 255, 255))
shell_button = pygame.Rect(window_width - 135 - 125 - 10 - 125 - 10 - 125 - 10 - 125 - 10, 60, 125, 40)
shell_button_text = font.render("Shell", True, (255, 255, 255))
linear_search_button = pygame.Rect(window_width - 135 - 125 - 10 - 125 - 10 - 125 - 10 - 125 - 10 - 155 -10, 10, 155, 40)
linear_search_button_text = font.render("Linear Search", True, (255, 255, 255))
binary_search_button = pygame.Rect(window_width - 135 - 125 - 10 - 125 - 10 - 125 - 10 - 125 - 10 - 155 -10, 60, 155, 40)
binary_search_button_text = font.render("Binary Search", True, (255, 255, 255))
reorder_button = pygame.Rect(10, 10, 125, 40)
reorder_button_text = font.render("Reorder", True, (255, 255, 255))
sorting_button = pygame.Rect(10, 10, 125, 40)
sorting_button_text = font.render("Sorting...", True, (255, 255, 255))

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Exit the game
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if bubble_button.collidepoint(event.pos):
                bubble_sort(lines, line_width, window, bg_color, sorting_button, sorting_button_text, sound)
            elif selection_button.collidepoint(event.pos):
                selection_sort(lines, line_width, window, bg_color, sorting_button, sorting_button_text, sound)
            elif insertion_button.collidepoint(event.pos):
                insertion_sort(lines, line_width, window, bg_color, sorting_button, sorting_button_text, sound)
            elif merge_button.collidepoint(event.pos):
                merge_sort(lines, line_width, window, bg_color, sorting_button, sorting_button_text, sound)
            elif quick_button.collidepoint(event.pos):
                merge_sort(lines, line_width, window, bg_color, sorting_button, sorting_button_text, sound)
            elif counting_button.collidepoint(event.pos):
                merge_sort(lines, line_width, window, bg_color, sorting_button, sorting_button_text, sound)
            elif radix_button.collidepoint(event.pos):
                merge_sort(lines, line_width, window, bg_color, sorting_button, sorting_button_text, sound)
            elif bucket_button.collidepoint(event.pos):
                merge_sort(lines, line_width, window, bg_color, sorting_button, sorting_button_text, sound)
            elif heap_button.collidepoint(event.pos):
                merge_sort(lines, line_width, window, bg_color, sorting_button, sorting_button_text, sound)
            elif shell_button.collidepoint(event.pos):
                merge_sort(lines, line_width, window, bg_color, sorting_button, sorting_button_text, sound)
            elif linear_search_button.collidepoint(event.pos):
                merge_sort(lines, line_width, window, bg_color, sorting_button, sorting_button_text, sound)
            elif binary_search_button.collidepoint(event.pos):
                merge_sort(lines, line_width, window, bg_color, sorting_button, sorting_button_text, sound)
            elif reorder_button.collidepoint(event.pos):
                # Regenerate the list of lines with new random heights
                lines = []
                for i in range(int(window_width / line_width - 2)):
                    height = random.randint(line_width, 500)
                    x = (i + 1) * line_width
                    y = window_height - height
                    line = Line(x, y, height)
                    lines.append(line)

    # Fill the window with the background color
    window.fill(bg_color)

    # Draw the lines
    for line in lines:
        line.draw(window)

    # Draw the buttons
    general_btn(window, bubble_button, bubble_button_text, (0, 0, 0))
    general_btn(window, selection_button, selection_button_text, (0, 0, 0))
    general_btn(window, insertion_button, insertion_button_text, (0, 0, 0))
    general_btn(window, merge_button, merge_button_text, (0, 0, 0))
    general_btn(window, quick_button, quick_button_text, (0, 0, 0))
    general_btn(window, counting_button, counting_button_text, (0, 0, 0))
    general_btn(window, radix_button, radix_button_text, (0, 0, 0))
    general_btn(window, bucket_button, bucket_button_text, (0, 0, 0))
    general_btn(window, heap_button, heap_button_text, (0, 0, 0))
    general_btn(window, shell_button, shell_button_text, (0, 0, 0))
    general_btn(window, linear_search_button, linear_search_button_text, (0, 0, 0))
    general_btn(window, binary_search_button, binary_search_button_text, (0, 0, 0))
    general_btn(window, reorder_button, reorder_button_text, (0, 0, 0))

    # Update the display
    pygame.display.update()
