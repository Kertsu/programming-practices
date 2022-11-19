morse_list = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D': '-..', 'E':'.', 'F': '..-.', 'G': '--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L': '.-..', 'M':'--','N':'-.', 'O':'---', 'P': '.--.', 'Q' : '--.-', 'R':'.-.', 'S': '...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', 1 :'.----', 2:'..---', 3:'...--', 4:'....-', 5: '.....', 6:'-....', 7:'--...', 8:'---..', 9:'----.', 0:'-----'}

input = input('Enter any word: ')

def translate():    
    input.upper()
    input_list = []
    for letter in input:
        input_list.append(letter.upper())

    for i in range(len(input_list)):
        for key, value in morse_list.items():
            if input_list[i] == key:
                print(value, end =' ')

translate()