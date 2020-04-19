# the longest word in the dictionary is dichlorodiphenyltrichloroethane,
# which has 31 letters. But the max length of the board in WWF is 15
# also, WWF does not allow 1-letter words
def load_words(max_length=15):
    with open('words_alpha.txt') as word_file:
        return [one_word
                for one_word in set(word_file.read().split())
                if (len(one_word) > 1) and (len(one_word) <= max_length)]


def can_spell_word(word, tiles):
    for one_letter in word:
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


def word_has_letters(word, required_letters):
    if not required_letters:
        return True
    else:
        return all(one_letter in word
                   for one_letter in required_letters)


# here we assume that "tiles" are the tiles that the user has
# "starts_with" and "ends_with" are considered to be tiles that are already on the board
def get_all_words(tiles, required_letters="", max_length=15, starts_with="", ends_with=""):
    tiles += starts_with + ends_with
    words = [(one_word, get_word_score(one_word))
             for one_word in load_words(max_length=max_length)
             if one_word.startswith(starts_with) and
             one_word.endswith(ends_with) and
             word_has_letters(one_word, required_letters) and
             can_spell_word(one_word, tiles)]

    return sorted(words, key=lambda x: x[1], reverse=True)


def starts_with_ends_with(starts_with="", ends_with=""):
    words = [(one_word, get_word_score(one_word))
             for one_word in load_words()
             if one_word.startswith(starts_with) and one_word.ends_with(ends_with)]

    return sorted(words, key=lambda x: x[1], reverse=True)

# Print an example
get_all_words('ilzsiwl', max_length=7, ends_with='i')
