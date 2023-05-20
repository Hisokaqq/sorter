def bucket_sort(lines, line_width, window, bg_color, sort_button, sort_button_text, sound):
    # Find the minimum and maximum values of the heights
    min_height = min(line.height for line in lines)
    max_height = max(line.height for line in lines)

    # Calculate the number of buckets
    num_buckets = int(np.sqrt(len(lines)))

    # Create empty buckets
    buckets = [[] for _ in range(num_buckets)]

    # Distribute the lines into buckets based on their heights
    for line in lines:
        # Calculate the index of the bucket
        index = int((line.height - min_height) / (max_height - min_height + 1) * num_buckets)
        buckets[index].append(line)

    # Sort each bucket individually
    for bucket in buckets:
        # Sort the lines in the bucket using any sorting algorithm (e.g., insertion sort)
        insertion_sort(bucket, line_width, window, bg_color, sort_button, sort_button_text, sound)

    # Concatenate the sorted buckets into a single list
    sorted_lines = [line for bucket in buckets for line in bucket]

    # Update the original lines with the sorted lines
    for i, line in enumerate(lines):
        lines[i] = sorted_lines[i]

    # Draw the sorted lines
    window.fill(bg_color)
    for line in lines:
        line.draw(window)
    general_btn(window, sort_button, sort_button_text, (255, 0, 0))
    pygame.display.update()

    # Perform the checker review
    checker_review(window, bg_color, lines, sound)
