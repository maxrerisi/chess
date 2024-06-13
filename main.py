import chess
import chess.pgn
import time

# Initialize the chess board
board = chess.Board()


# Function to generate all valid moves for the current position
overall = {}
def generate_moves(board, depth):
    if depth == 0:
        return [board.fen()]  # Use FEN to represent the board state

    moves = []
    for move in board.legal_moves:
        board.push(move)
        if (board, depth-1) in overall:
            return overall[[board, depth-1]]
        moves.extend(generate_moves(board, depth - 1))
        board.pop()
    overall[(board, depth)] = moves
    return moves


# Generate all possible sequences of moves for the first two moves of each player
depth = 4  # Two moves each by white and black

for a in range(1,6):
    strt = time.time()
    all_moves = generate_moves(board, a)
    print(a, len(all_moves), time.time()-strt)

# # Output the number of sequences generated
# print(f"Total number of sequences for the first {depth // 2} moves of each player: {len(all_moves)}")
#
# # Example of printing the first 10 sequences (for demonstration)
# for i, sequence in enumerate(all_moves[:10]):
#     print(f"Sequence {i + 1}: {sequence}")