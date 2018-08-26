def quick_sort(l: list) -> list:
    if len(l) <= 1:
        return l

    # Pick an item, call it pivot
    m = len(l) // 2
    pivot = l[m]

    # Partition: Move all smaller items before pivot, and all greater items after it
    less, equal, greater = [], [], []
    for i in range(len(l)):
        if l[i] == pivot:
            equal.append(l[i])
        if l[i] < pivot:
            less.append(l[i])
        if l[i] > pivot:
            greater.append(l[i])

    # Repeat on smaller and greater lists
    return quick_sort(less) + equal + quick_sort(greater)
