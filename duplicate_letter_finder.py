word = input('Enter any word: ')

def find_dupe():
    for i in range(len(word)):
        current_letter = word[i]
        for j in range(i, len(word)-1):
            next_letter = word[j+1]
            if next_letter == current_letter:
                return True
    return False

if find_dupe():
    print("A letter has a duplicate.")
else:
    print('No duplicate letters.')