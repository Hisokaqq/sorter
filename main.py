import pygame
import random

from algorithms.bubble import bubble_sort
from algorithms.simple import simple_sort
from buttons.general import general_btn
# Initialize Pygame
pygame.mixer.init()
pygame.init()
sound = pygame.mixer.Sound("sound effects/td.mp3")


# Set the dimensions of the window
window_width = 900
window_height = 600

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
simple_button = pygame.Rect(window_width - 135-125-10, 10, 125, 40)
simple_button_text = font.render("Simple", True, (255, 255, 255))
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

            if simple_button.collidepoint(event.pos):
                simple_sort(lines, line_width, window, bg_color, sorting_button, sorting_button_text, sound)

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



    # Draw the "Sort" button
    general_btn(window, bubble_button, bubble_button_text, (0, 0, 0))
    general_btn(window, reorder_button, reorder_button_text, (0, 0, 0))
    general_btn(window, simple_button, simple_button_text, (0, 0, 0))

    # Update the display
    pygame.display.update()
