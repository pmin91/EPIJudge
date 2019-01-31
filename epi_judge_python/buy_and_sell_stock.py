from test_framework import generic_test

"""
<2,4,5,3>
 l h
"""

def buy_and_sell_stock_once(prices):
    # low = [prices[0], 0]
    # high = [prices[1], 0]

    # for i, n in enumerate(prices):
    #     if n < low[0] and i < high[1]:
    #         low[0], low[1] = n, i
    #     if n > high[0] and i > low[1]:
    #         high[0], high[1] = n, i
        

    # return high[0] - low[0]
    if not prices:
        return 0.0
    low = prices[0]
    result = 0.0
    for current in prices:
        if current - low > result:
            result = current - low
        if current < low:
            low = current
    return result


    ## Brute force solution O(n^2)
    # difference = prices[0] - prices[0]
    # for i in range(len(prices)):
    #     if i == len(prices)-1:
    #         break
    #     for j in range(i, len(prices)):
    #         if j>i and prices[j] - prices[i] > difference:
    #             difference = prices[j]- prices[i]
    
    # return difference


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
