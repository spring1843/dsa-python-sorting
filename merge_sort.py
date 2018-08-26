def merge_sort(l: list) -> list:
    if len(l) <= 1:
        return l

    # Split list into smaller lists (left and right) and sort each separately
    left, right = [], []
    for i in range(len(l)):
        if i < len(l) // 2:
            left.append(l[i])
        else:
            right.append(l[i])

    # Repeat on left and right lists
    left = merge_sort(left)
    right = merge_sort(right)

    # Join left and right which are sorted into a sorted list
    i = 0
    for i in range(len(l)):
        if len(left) == 0:
            return l[:i] + right
        if len(right) == 0:
            return l[:i] + left

        if left[0] < right[0]:
            l[i] = left.pop(0)
        else:
            l[i] = right.pop(0)
    return l[:i]
