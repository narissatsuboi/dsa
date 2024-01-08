
def fib(n):
    m = n + 1
    dp = [-1] * m    
    dp[0], dp[1] = 0, 1
    
    for i in range(2, m):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

if __name__ == '__main__':
    print('Fibonacci DP')
    print(fib(5))