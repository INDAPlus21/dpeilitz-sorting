def insertion_sort(data, draw):
    i = 1
    while i < len(data):
        x = data[i]
        j = i - 1
        while j >= 0 and data[j] > x:
            data[j+1] = data[j]
            j = j - 1
        data[j+1] = x
        i = i + 1
        draw(data)
