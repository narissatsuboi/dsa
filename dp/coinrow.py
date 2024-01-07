"""Coin-row problem 
There is a row of n coins whose values are some
positive integers c1, c2,...,cn, not necessarily distinct. The goal is to pick up the
maximum amount of money subject to the constraint that no two coins adjacent
in the initial row can be picked up.

F(0) = 0
F(1) = 1
F(n) = max => F(n-2) + coin_i (choose coin_n case)
           => F(n-1)          (don't choose coin_n)
"""

def coin_row_bottom_up(coins):
    """ bottom up approach
    TC O(n)
    SC O(n)
    """
    n = len(coins)

    # base cases
    if n == 0:
        return 0
    if n == 1:
        return coins[0]
    
    # fill table F(n) at each i
    dp = [0] * (n + 1)
    dp[1] = coins[0]
    
    for i in range(2, n + 1):
        dp[i] = max(
            dp[i-2] + coins[i-1],  # coins[i-1] for zero index
            dp[i-1]
        )
    return dp[n]

def coin_row_top_down(coins):
    """top down approach w memo
    TC O(n), each subproblem computed only once and there are n subproblems
    SC O(n), memo dictionary stores n subproblem results
    """
    n = len(coins)
    memo = {}
    
    def helper(i):
        if i in memo:
            return memo[i]
        
        # base cases
        if i == 0:
            return 0
        if i == 1:
            return coins[0]
        
        # recurrence relation
        include_current_coin = helper(i - 2) + coins[i - 1]
        exclude_current_coin = helper(i - 1)
        
        # memoize the result
        memo[i] = max(include_current_coin, exclude_current_coin)
        return memo[i]
    
    return helper(n)
    

if __name__ == '__main__':
    print('Coin Row DP Problem')
    
    # F(0) = 0
    print('no coins base case should return 0')
    print('bottom up ', coin_row_bottom_up([]))
    print('top down  ', coin_row_top_down([]))

    print('one coin base case should return 5')
    print('bottom up ',coin_row_bottom_up([5]))
    print('top down  ', coin_row_top_down([5]))

    print('greater than 1 coin should return 23')
    print('bottom up ',coin_row_bottom_up([5, 1, 9, 10, 9, 2]))
    print('top down  ', coin_row_top_down([5, 1, 9, 10, 9, 2]))
