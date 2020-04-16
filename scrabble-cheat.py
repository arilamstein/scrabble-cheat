def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return sorted(valid_words)


def can_spell_word(word, tiles, requirements):
    # 1 letter words are not valid
    if len(word) == 1:
        return False

    if requirements is None:
        requirements = '*' * len(word)
    elif len(word) != len(requirements):
        return False

    for one_requirement, one_letter in zip(requirements, word):
        # if we are required to play a certain letter here,
        # abort if the word does not meet the requirement
        if one_requirement != '*':
            if one_requirement != one_letter:
                return False

        # if this letter is available in our tiles, remove it and continue
        if one_letter in tiles:
            tiles = tiles.replace(one_letter, '', 1)
        else:
            return False

    return True


def get_word_score(word):
    letter_scores = {'a': 1, 'b': 4, 'c': 4, 'd': 2,
                     'e': 1, 'f': 4, 'g': 3, 'h': 3,
                     'i': 1, 'j': 10, 'k': 5, 'l': 2,
                     'm': 4, 'n': 2, 'o': 1, 'p': 4,
                     'q': 10, 'r': 1, 's': 1, 't': 1,
                     'u': 2, 'v': 5, 'w': 4, 'x': 8,
                     'y': 3, 'z': 10}

    return sum([letter_scores[letter]
                for letter in word])


# requirements is a string like '***s', which means
# 'requires a "s" at the end of a 4 letter word',
# ex 'cats' and 'dogs'
def get_all_possible_words(tiles, requirements=None):
    words = [(one_word, get_word_score(one_word))
             for one_word in load_words()
             if can_spell_word(one_word, tiles, requirements)]

    return sorted(words, key=lambda x: x[1], reverse=True)

# Print an example
print(get_all_possible_words('crtswyo'))
