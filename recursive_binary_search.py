list = [1,2,3,4,5,6,7,8,9,10]
target = int(input('Enter what you want to search for: '))


def recursive_binary_search(list, target, lower_value, upper_value):
    if upper_value >= lower_value:
        midpoint = (upper_value + lower_value) // 2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] > target:
            return recursive_binary_search(list, target, lower_value, midpoint-1)
        else:
            return recursive_binary_search(list, target, midpoint+1, upper_value)

    return -1


result = recursive_binary_search(list, target, 0, len(list)-1)

if result != -1:
    print(f'{target} is at index {result}')
else:
    print(f'{target} is not in {list}')