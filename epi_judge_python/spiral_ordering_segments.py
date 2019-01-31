from test_framework import generic_test


def matrix_in_spiral_order(square_matrix):
    directions = ((0,1),(1,0),(0,-1),(-1,0))
    d = x = y = 0
    spiral_m = []
    for i in range(len(square_matrix)**2):
        spiral_m.append(square_matrix[x][y])
        square_matrix[x][y] = 0
        next_x, next_y = x+directions[d][0], y+ directions[d][1]
        if (next_x not in range(len(square_matrix))) or (next_y not in range(len(square_matrix))) or (square_matrix[next_x][next_y] == 0):
            d = (d + 1)&3
            next_x, next_y = x+directions[d][0], y+ directions[d][1]
        x, y = next_x, next_y
    return spiral_m


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spiral_ordering_segments.py",
                                       "spiral_ordering_segments.tsv",
                                       matrix_in_spiral_order))
