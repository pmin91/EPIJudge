from test_framework import generic_test


def evaluate(expression):
    mapper = {"+": lambda y, x: x + y, \
    "-": lambda y, x: x-y, \
    "*": lambda y, x: x*y,\
    "/": lambda y, x: int(x/y)
    }
    stack = []
    for i in expression.split(','):
        if i in mapper:
            stack.append(mapper[i](stack.pop(), stack.pop()))
        else:
            stack.append(int(i))
    return stack.pop()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", 'evaluate_rpn.tsv',
                                       evaluate))
