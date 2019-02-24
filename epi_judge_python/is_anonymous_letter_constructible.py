from test_framework import generic_test
from collections import Counter

def is_letter_constructible_from_magazine(letter_text, magazine_text):
    # TODO - you fill in here.
    
    m = Counter(magazine_text)
    for i in letter_text:
        m[i] -= 1
        if m[i] < 0:
            return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
