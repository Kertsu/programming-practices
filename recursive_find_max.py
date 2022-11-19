list = [3,5,7,1,10,25,45,2,4,24,76,1521,52]

def find_max(list, idx, highest_val):
    if idx < len(list):    
        if highest_val == list[idx]:
            return find_max(list, idx+1, highest_val)
        if highest_val < list[idx]:
            return find_max(list, idx+1, list[idx])
        if highest_val > list[idx]:
            return find_max(list, idx+1, highest_val)

    return highest_val 

result = find_max(list, 0, list[0])
if result > 0:
    print(result)