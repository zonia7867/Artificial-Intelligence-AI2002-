def print_board(board):
    for i in range(0,9,3):
        print(board[i], board[i+1], board[i+2])

def check_win(board):
    lines = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for line in lines:
        if board[line[0]] == board[line[1]] == board[line[2]] != 0:
            return board[line[0]]
    return 0

def check_draw(board):
    return all(x != 0 for x in board)

def get_moves(board):
    return [i for i in range(9) if board[i] == 0]

def minimax(board, depth, is_max, alpha, beta):
    winner = check_win(board)
    if winner != 0:
        return winner
    if check_draw(board):
        return 0
    if is_max:
        max_eval = -1000
        for move in get_moves(board):
            board[move] = 1
            eval = minimax(board, depth+1, False, alpha, beta)
            board[move] = 0
            if eval > max_eval:
                max_eval = eval
            if eval > alpha:
                alpha = eval
                print("Depth", depth, "Alpha updated to", alpha)
            if beta <= alpha:
                print("Depth", depth, "Cutoff")
                break
        return max_eval
    else:
        min_eval = 1000
        for move in get_moves(board):
            board[move] = -1
            eval = minimax(board, depth+1, True, alpha, beta)
            board[move] = 0
            if eval < min_eval:
                min_eval = eval
            if eval < beta:
                beta = eval
                print("Depth", depth, "Beta updated to", beta)
            if beta <= alpha:
                print("Depth", depth, "Cutoff")
                break
        return min_eval

def best_move(board, is_max):
    best_val = -1000 if is_max else 1000
    best_move = -1
    for move in get_moves(board):
        board[move] = 1 if is_max else -1
        val = minimax(board, 0, not is_max, -1000, 1000)
        board[move] = 0
        if (is_max and val > best_val) or (not is_max and val < best_val):
            best_val = val
            best_move = move
    return best_move, best_val

board = [0]*9
is_max = True
while True:
    print_board(board)
    move, val = best_move(board, is_max)
    board[move] = 1 if is_max else -1
    print("Player", "MAX" if is_max else "MIN", "moves to", move)
    if is_max:
        utility_max = val
        utility_min = -val
    else:
        utility_min = val
        utility_max = -val
    print("Utility MAX:", utility_max, "MIN:", utility_min)
    winner = check_win(board)
    if winner != 0 or check_draw(board):
        break
    is_max = not is_max
print_board(board)
if winner == 1:
    print("MAX wins")
elif winner == -1:
    print("MIN wins")
else:
    print("Draw")