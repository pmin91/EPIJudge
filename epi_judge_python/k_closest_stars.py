import functools
import math

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class Star:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    @property
    def distance(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __lt__(self, rhs):
        return self.distance < rhs.distance

    def __repr__(self):
        return str(self.distance)

    def __str__(self):
        return self.__repr__()

    def __eq__(self, rhs):
        return math.isclose(self.distance, rhs.distance)

import heapq
def find_closest_k_stars(stars, k):
    # TODO - you fill in here.
    # heap for this since it's k closest, we have distance 
    # compute distances, store in an array (O(N)), sort (nlogn)
    # heap O(nlogk) max heap (closest, or the smallest distance)
    # assume euclidean distance, distance fn is already given
    # heapq library, -
    # max_heap = []
    # # first itialize the heap with k elements
    # stars_iter = iter(stars)
    # n = len(stars)
    # for _ in range(k):
    #     star = next(stars_iter, None)
    #     heapq.heappush(max_heap, (-1*star.distance, star))
    # for _ in range(n-k):
    #     star = next(stars_iter, None)
    #     heapq.heappushpop(max_heap, (-1*star.distance, star))
    # for i in range(k):
    #     max_heap[i] = max_heap[i][1]
    max_heap = []
    for star in stars:
        heapq.heappush(max_heap, (-star.distance, star))
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    return [x[1] for x in heapq.nlargest(k, max_heap)]


def comp(expected_output, output):
    if len(output) != len(expected_output):
        return False
    return all(
        math.isclose(s.distance, d)
        for s, d in zip(sorted(output), expected_output))


@enable_executor_hook
def find_closest_k_stars_wrapper(executor, stars, k):
    stars = [Star(*a) for a in stars]
    return executor.run(
        functools.partial(find_closest_k_stars, iter(stars), k))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("k_closest_stars.py",
                                       "k_closest_stars.tsv",
                                       find_closest_k_stars_wrapper, comp))
