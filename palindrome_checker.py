word = input('Enter any word to check: ')

def is_palindrome():
    list = []

    for letter in word:
        list.append(letter)

    test_list = list[:]

    test_list.reverse()

    if list == test_list:
        return True
    
    return False


if is_palindrome():
    print(f'{word} is a palindrome')
else:
    print(f'{word} is not a palindrome')

