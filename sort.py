def sort(l):
    if l is None:
        return l
    a = len(l)
    if a <= 1:
        return l

    for j in range(a-1, 1, -1):
        for i in range(0, j):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]

    return l
