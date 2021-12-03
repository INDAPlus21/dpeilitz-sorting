import math


def merge_sort(data, draw):
    if len(data) > 1:
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]

        # Recursive call on each half
        merge_sort(left, draw)
        merge_sort(right, draw)

        # Two iterators for traversing the two halves
        i = 0
        j = 0

        # Iterator for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                # The value from the left half has been used
                data[k] = left[i]
                # Move the iterator forward
                i += 1
            else:
                data[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1

        draw(data)
