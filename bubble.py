def bubble_sort(data, draw_data):
    for i in range(0, len(data)):
        for j in range(0, len(data)-i-1):

            a = data[j]
            b = data[j+1]
            if (a > b):
                data[j], data[j+1] = b, a
                draw_data(data)
