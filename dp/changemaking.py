"""
Coin Change problem Consider the general instance of the
following well-known problem. Give change for amount n using the minimum
number of coins of denominations d1 < d2 < ... < dm.
"""

def print_matrix(m):
    for row in m:
        print(row)

    
def coin_change(coins, amount):
    """ bottom up approach
    TC O(amount * len(coins)) -> O(n2)
    SC O(amount)
    F(0) = 0
    F(n) = minimum number of coins needed to make change for amount n
    F(n) = min(F(n - 1), 1 + F(n - coins(i))
    
    F(n-1): Min no coins to make change for n-1.
    1 + F(n - coins(i)): Use 1 coin of the current denomination (+1) and the min. no coins to
    account for the remaining amount using table at F(n - coins(i)) 
    """
    dp = [amount + 1] * (amount + 1) # 0 ... amount
    dp[0] = 0
    
    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(
                            dp[a], # (itself) of c
                            1 + dp[a - c]  # (1) of c + tabulated # cs for remaining amnt
                        )
    return dp[amount] if dp[amount] != amount + 1 else -1
            
if __name__ == "__main__":  
    print('Change Making')
    num_coins = coin_change([1, 5, 6, 9], 10)
    print(num_coins)