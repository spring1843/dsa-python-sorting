def shell_sort(l: list) -> list:
    if len(l) <= 1:
        return l

    increment = len(l) // 2
    while increment != 0:
        for current in range(len(l)):
            hold = l[current]
            i = current - increment
            while i >= 0 and hold < l[i]:
                l[i + increment] = l[i]
                i -= increment
            l[i + increment] = hold
        increment //= 2
    return l
