""" Coin-collecting problem 
Several coins are placed in cells of an
n × m board, no more than one coin per cell. A robot, located in the upper left cell
of the board, needs to collect as many of the coins as possible and bring them to
the bottom right cell. On each step, the robot can move either one cell to the right
or one cell down from its current location. When the robot visits a cell with a coin,
it always picks up that coin. Design an algorithm to find the maximum number of
coins the robot can collect and a path it needs to follow to do this
"""


def print_grid(grid):
    for row in grid:
        print(row)

def robot_coin(board):
    """recurrence

    F(i, j) = max{F(i - 1, j) , F(i, j - 1)} + board[i][j], 1 <= i, j <=n
    F(0, j) = 0 for 1 <= j <=m, first row.
    F(i, 0) = 0 for 1<= i <=n, first column.

    Args:
        board: n x m matrix of 0's and 1's. 0s = no coin, 1s = coin. 
    """
    if not board or not board[0]:
        return 0
    
    n, m = len(board), len(board[0])
    
    dp = [[0 for j in range(m)] for i in range(n)]
    
    # carry over the first cell
    dp[0][0] = board[0][0]
    
    # init first row and first column
    # note: not necessary if we can assume nothing in first row or first column
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + board[i][0] 

    for j in range(1, m):
        dp[0][j] = dp[0][j - 1] + board[0][j]
    
    # fill in dp table
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = board[i][j] + max(dp[i - 1][j], dp[i][j - 1])
            
    print('DP Table Filled')
    print_grid(dp)
    return dp[n-1][m-1]

if __name__ == "__main__":
    print('Robot Coin Collection')
    n, m = 6, 7
    board = [[0 for j in range(m)] for i in range(n)]
    
    board[1][5] = 1
    board[2][2] = 1
    board[2][4] = 1
    board[3][4] = 1
    board[3][6] = 1
    board[4][3] = 1
    board[5][6] = 1
    board[5][1] = 1
    board[5][5] = 1
    print_grid(board)
    print()
    res = robot_coin(board)
    print(res)