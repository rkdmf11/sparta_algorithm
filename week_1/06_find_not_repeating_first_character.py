input = "abadabac" #"abacabade"


def find_not_repeating_character(string):
    alphabet_occurrence_array = [0]*26
    for char in string:
        if not char.isalpha():
            continue
        array_index = ord(char) - ord('a')
        alphabet_occurrence_array[array_index] += 1

    not_repeating_character = []
    for index in range(len(alphabet_occurrence_array)):
        array_occurrence = alphabet_occurrence_array[index]
        if array_occurrence == 1:
            not_repeating_character.append(chr(index+ord('a')))

    for char in string:
        if char in not_repeating_character:
            return char

    return "_"


result = find_not_repeating_character(input)
print(result)