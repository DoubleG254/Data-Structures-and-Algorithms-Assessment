#QUESTION 1 : STACKS
def is_balanced(expression):
    opening_bracket = []

    brackets ={")":"(","]":"[","}":"{"}
    for bracket in expression:
        if bracket in "([{":
            opening_bracket.append(bracket)
        elif bracket in ")]}":
            if not opening_bracket:
                return False
            if brackets[bracket] != opening_bracket.pop():
                return False
    return len(opening_bracket) == 0

expression ="([]})"
print(is_balanced(expression))
#  QUESTION 2 :SEQUENCES
def remove_duplicates(sequence):
    new_list = []
    for char in sequence:
        if char not in new_list:
            new_list.append(char)
    return new_list

set_sequence = [2,4,6,4,2,3,9,7]
print(remove_duplicates(set_sequence))

#QUESTION 3: DICTIONARIES

def word_frequency(sentence):
    level_sentence = sentence.lower().split()
    word_number = {}
    for word in level_sentence:
        if word in word_number:
            word_number[word] += 1
        else:
            word_number[word] = 1
    return word_number

sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)