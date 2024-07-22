def solve(board):
    if not board or not board[0]:
        return
    m, n = len(board), len(board[0])
    def dfs(x, y):
        if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != 'O':
            return
        board[x][y] = 'T'  
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
    for i in range(m):
        if board[i][0] == 'O':
            dfs(i, 0)
        if board[i][n-1] == 'O':
            dfs(i, n-1)
    for j in range(n):
        if board[0][j] == 'O':
            dfs(0, j)
        if board[m-1][j] == 'O':
            dfs(m-1, j)
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O':
                board[i][j] = 'X'
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'T':
                board[i][j] = 'O'
    return board 
board = [["X","X","X","X"],
         ["X","O","O","X"],
         ["X","X","O","X"],
         ["X","O","X","X"]]
print(solve(board))