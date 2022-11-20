list = [3,5,7,1,10,25,45,2,4,24,76,1521,52]

def find_min(list, idx, minimum_val):
    if idx < len(list):    
        if minimum_val == list[idx]:
            return find_min(list, idx+1, minimum_val)
        if minimum_val < list[idx]:
            return find_min(list, idx+1, minimum_val)
        if minimum_val > list[idx]:
            return find_min(list, idx+1, list[idx])

    return minimum_val 

result = find_min(list, 0, list[0])
if result > 0:
    print(result)