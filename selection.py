def selection_sort(data, draw):
    i = 0
    for k in range(len(data)):
        cur = k
        for i in range(cur+1, len(data)):
            if data[cur] > data[i]:
                cur = i

        if cur != k:
            data[cur], data[k] = data[k], data[cur]
        draw(data)
