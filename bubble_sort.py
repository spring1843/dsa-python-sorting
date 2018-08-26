def bubble_sort(l: list) -> list:
    for i in range (len(l)):
       for j in range (len(l)):
            if l[i] < l[j]:
                l[j], l[i] = l[i], l[j]
    return l
