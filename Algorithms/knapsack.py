def knapSack(W, wt, val, n):
    """
    Given weights and values of n items, put these items in a knapsack of capacity
    W to get the maximum total value in the knapsack. In other words, given two
    integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights
    associated with n items respectively. Also given an integer W which represents
    knapsack capacity, find out the maximum value subset of val[] such that sum of
    the weights of this subset is smaller than or equal to W. You cannot break an
    item, either pick the complete item, or don’t pick it (0-1 property).

    Example:
    wt = 7

    wt | val
    --------
    1  | 1
    3  | 4
    4  | 5
    5  | 7

    result = 9

    Explanation

    +------+-----+---+---+---+---+---+---+---+---+
    | val  | wt  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
    +------+-----+---+---+---+---+---+---+---+---+
    |    1 |   1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
    |    4 |   3 | 0 | 1 | 1 | 4 | 5 | 5 | 5 | 5 |
    |    5 |   4 | 0 | 1 | 1 | 4 | 5 | 6 | 6 | 9 |
    |    7 |   5 | 0 | 1 | 1 | 4 | 5 | 7 | 8 | 9 |
    +------+-----+---+---+---+---+---+---+---+---+
    """
    result = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                result[i][w] = 0
            if wt[i - 1] <= w:
                result[i][w] = max(
                    val[i - 1] + result[i - 1][w - wt[i - 1]], result[i - 1][w]
                )
            else:
                result[i][w] = result[i - 1][w]
    return result[n][W]


val_eg = [1, 4, 5, 7]
wt_eg = [1, 3, 4, 5]
W_eg = 7
n_eg = len(val_eg)
print(knapSack(W_eg, wt_eg, val_eg, n_eg))
