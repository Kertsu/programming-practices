list = [1,1,2,5,8,13]

def summation(list, idx, val, Sum):
    if idx < len(list)-1:
        if Sum != 0:
            return summation(list, idx+1, Sum, list[idx+1]+Sum)
        else:
            return summation(list, idx+1, val, list[idx+1]+val)
    if list[idx] == val and idx != 1:
        return val
    return Sum
        
result = summation(list, 0, list[0], 0)
if result >= 0:
    print(f'The sum of all the numbers in list {list} is : {result}')
