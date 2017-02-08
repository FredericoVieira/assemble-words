from words_bank import words_bank
from letter_values import letter_values


def possibleWordsByLength(inputed_letters_length):

    possible_words_by_length = []

    for word in words_bank:
        if len(word) <= inputed_letters_length:
            possible_words_by_length.append({'word': word.lower(), 'length': len(word.decode('utf-8'))})

    return possible_words_by_length


def possibleWordsByMatch(possible_words_by_length, inputed_letters):

    possible_words_by_match = []

    for word in possible_words_by_length:
        aux_word = word['word']
        remaining_letters = inputed_letters
        for letter in inputed_letters:

            if letter in aux_word:
                aux_word = aux_word.replace(letter, '_', 1)
                remaining_letters = remaining_letters.replace(letter, '', 1)
                
            if aux_word.count('_') == len(aux_word):
                word['remaining_letters'] = remaining_letters
                possible_words_by_match.append(word)
                break

    return possible_words_by_match


def scoreWords(possible_words_by_match):

    score_words = []

    for word in possible_words_by_match:
        score = 0
        current_word = word['word']
        for letter in current_word:

            if letter_values.has_key(letter):
                score = score + letter_values.get(letter)
                
        word['score'] = score
        score_words.append(word)

    return score_words


def bestChoice(score_words):

    best_choice = {}
    max_score = 0
    min_length = 99

    for word in score_words:
        if word['score'] > max_score:
            best_choice = word
            max_score = word['score']
        
        if word['score'] == max_score:
            if word['length'] < min_length:
                best_choice = word
                min_length = word['length']

    return best_choice


if __name__ == '__main__':
    
    inputed_letters = raw_input('Input avaible letters for this move:')

    ''.join(char for char in inputed_letters if char.isalnum())
    inputed_letters = inputed_letters.replace('_', '')

    possible_words_by_length = possibleWordsByLength(len(inputed_letters))
    possible_words_by_match = possibleWordsByMatch(possible_words_by_length, inputed_letters)
    score_words = scoreWords(possible_words_by_match)
    best_choice = bestChoice(score_words)

    print 'word: {0}, length: {1}, score: {2}, remaining letters: {3}' \
        .format(best_choice['word'], best_choice['length'], best_choice['score'], best_choice['remaining_letters']) \
        if best_choice else 'No word found for the combination of inputed letters...'
