def insertion_sort(l: list) -> list:
    if len(l) <= 1:
        return l

    # Pick one item, then find the right place in the list to put it in
    for unsorted  in range(len(l)):
        hold = l[unsorted]
        i = unsorted - 1
        while i >= 0 and hold < l[i]:
            l[i + 1] = l[i]
            i -= 1
        l[i + 1] = hold
    return l
