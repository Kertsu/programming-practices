list = ['a','b','c','d','e','f']

def recursive_iteration(list, idx):
    if idx >= len(list):
        return -1
    if list[idx] == list[idx]:
        print(list[idx], end = '')
        return recursive_iteration(list, idx+1)


recursive_iteration(list, 0)