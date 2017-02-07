#coding: utf-8

from words_bank import words_bank

def possibleWordsByLength(inputed_letters_length):

    possible_words_by_length = []

    for word in words_bank:
        if len(word) <= inputed_letters_length:
            possible_words_by_length.append({word.lower(): len(word)})

    return possible_words_by_length


def possibleWordsByMatch(possible_words_by_length, inputed_letters):

    possible_words_by_match = []
    repetead_letters = []
    counter = 0

    for word in possible_words_by_length:
        for letter in inputed_letters:

            #if word.keys()[0].count(letter) >= 1:
            #    pass
            #else:
            #    word['unused_letters'] = letter

            if letter in word.keys()[0]:
                counter = counter + 1

        if counter == word.values()[0]:
            #verificar se da pra formar a palavra com letras repetidas
            #batata = 3a e 2t tamanho 5 forma porta
            possible_words_by_match.append(word)

        counter = 0

    return possible_words_by_match


def scoreWords(possible_words_by_match):

    letter_values = {
        'aeilnorstu': 1,
        'dgw': 2,
        'bcmp': 3,
        'fhv': 4,
        'jx': 8,
        'qz': 10
    }

    #for key in letters_values:
    #    for letter in key.keys()[0]:
    #        for word in possible_words_by_match:
    #            if letter in word:

    #scored_words.append({word, score})
    scored_words = []


    return scored_words


if __name__ == "__main__":
    try:
        inputed_letters = str(raw_input('Input avaible letters:'))
    except ValueError:
        print "Not a valid input!"

    #inputed_letters expected format 'example'

    possible_words_by_length = possibleWordsByLength(len(inputed_letters))
    possible_words_by_match = possibleWordsByMatch(possible_words_by_length, inputed_letters)
    score_words = scoreWords(possible_words_by_match)

    print(possible_words_by_length)
    print(possible_words_by_match)