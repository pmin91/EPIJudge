import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size, s):
    # TODO - you fill in here.
    count_a = 0
    count_b = 0
    for i in s:
        if i == "a":
            count_a += 1
        elif i == "b":
            count_b += 1
    
    
    return s


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("replace_and_remove.py",
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
