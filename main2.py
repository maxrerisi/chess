import chess
import time
start = time.time()

def count_moves(board, depth, memo):
    if depth == 0:
        return 1  # Only one way to stay in the same position

    board_fen = board.fen()  # Use the board's FEN as a unique key for memoization
    if (board_fen, depth) in memo:
        return memo[(board_fen, depth)]

    total_moves = 0
    for move in board.legal_moves:
        board.push(move)
        total_moves += count_moves(board, depth - 1, memo)
        board.pop()

    memo[(board_fen, depth)] = total_moves
    return total_moves

# Usage

for MOVE in range(1, 7):
    start = time.time()
    board = chess.Board()
    memo = {}
    depth = MOVE  # Example depth
    number_of_moves = count_moves(board, depth, memo)

    print(f"Number of possible moves up to depth {depth}: {number_of_moves}, {time.time()-start}")

#print(type(board.fen()))