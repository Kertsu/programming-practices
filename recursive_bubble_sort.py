list = [2,1,3,5,4,52,12,24]

def recursive_bubble_sort(list, idx, val):
    if idx < len(list):
        if val == list[idx]:
            return recursive_bubble_sort(list, idx+1, list[idx])
        if val > list[idx]:
            list[idx-1], list[idx] = list[idx], list[idx-1]
            return recursive_bubble_sort(list, idx+1, list[idx])
        if val < list[idx]:
            return recursive_bubble_sort(list, idx+1, list[idx])
        
    return list
result = recursive_bubble_sort(list, 0, list[0])

if result != -1:
    print(result)