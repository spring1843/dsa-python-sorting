import math

base = 10 # i.e. Decimal

def empty_queue():
    return [[] for _ in range(base)]

def radix_sort(l: list) -> list:
    if len(l) <= 1:
        return l

    max_key_size = 1
    for item in l:
        digits = int(math.log10(abs(item))) + 2
        if digits > max_key_size:
            max_key_size = digits


    queues = empty_queue()
    index_of_key = 1
    for i in range (max_key_size - 1):
        for item in l:
            queue_index = (item // index_of_key) % base # This is not going work for negative integers
            queues[queue_index].insert(0, item)

        # Collapse the queue
        l = []
        for ii in range(base):
            while len(queues[ii]) != 0:
                l.append(queues[ii].pop())

        queues =  empty_queue()
        index_of_key *= base
    return l
