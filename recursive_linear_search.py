list  = [1,2,3,4,5,6,7,8,9,10]

target = int(input('Enter target: '))

def recursive__linear_search(list, idx, target):
    if idx >= len(list):
        return -1
    if list[idx] == target:
        return idx
    return recursive__linear_search(list, idx+1, target)

result = recursive__linear_search(list, 0, target)

if result < 0:
    print(f'{target} was not found')
else:
    print(f'{target} was found at index {result}')