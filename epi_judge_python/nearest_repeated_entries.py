from test_framework import generic_test


def find_nearest_repetition(paragraph):
    word_dict = dict()
    max_dist = len(paragraph) + 1
    for idx, word in enumerate(paragraph):
        if word in word_dict:
            dist = idx - word_dict[word]
            max_dist = min(max_dist, dist)
        word_dict[word] = idx
    return max_dist if max_dist != len(paragraph)+1 else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("nearest_repeated_entries.py",
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
