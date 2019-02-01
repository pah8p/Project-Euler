


def quick_sort(x):
    if len(x) < 1:
        return x
    n = int(len(x)/2)
    top = []
    bottom = []
    for i in range(len(x)):
        if i != n:
            if x[i] >= x[n]:
                top.append(x[i])
            elif x[i] < x[n]:
                bottom.append(x[i])
    return quick_sort(bottom) + [x[n]] + quick_sort(top)


print(quick_sort([1, 4, 5, 6, 2, 3, 9, 7, 8]))

    
