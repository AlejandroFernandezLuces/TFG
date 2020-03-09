import numpy as np
def odd_list(list):
    odd_items = []
    for i in range(list.__len__()):
        if i % 2 != 0:
            odd_items.append(list[i])
    return odd_items