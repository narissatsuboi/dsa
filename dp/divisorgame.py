def divisorGame(n: int) -> bool:
    """1025 Divisor Game
    base case occurs when Alice loses and n = 1 because there's no
    valid integer to satisfy the first part of the move 0 < x < 1
    
    handle constraints of each turn in the second for loop
    """
    # dp table from base case n = 1 to n
    print('n = ', n)
    dp = [False] * (n + 1)
    
    # initialize base case
    dp[1] = False
    
    # fill dp table from i = 2 to n
    for i in range(2, n + 1):
        # start = 1 bc domain {1, ... n-1}
        # end = half i because we can eliminate x > 1/2 i from consideration
        # more than half of n will not mod to 0
        for x in range(1, (i // 2) + 1):
            if (i % x == 0) and not dp[i - x]:
                dp[i] = True # record a win for Alice at i
                print('n=', i, 'x=', x, dp)
                break
    return dp[n]        

if __name__ == "__main__":
    print('Divisor Game')
    print(divisorGame(1))
    print(divisorGame(2))
    print(divisorGame(3))
    print(divisorGame(4))
    print(divisorGame(5))
    