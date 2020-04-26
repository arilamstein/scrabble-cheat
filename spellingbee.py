# code to cheat at the NY Times "Spelling Bee"
# https://www.nytimes.com/puzzles/spelling-bee
from scrabblecheat import load_words

def solve_spelling_bee(required_letter, other_letters):
    all_letters = required_letter + other_letters
    words = [
        one_word
        for one_word in load_words(31)
        if len(one_word) >= 5
        if required_letter in one_word
        if set(one_word) <= set(all_letters)
    ]
    
    return sorted(words)