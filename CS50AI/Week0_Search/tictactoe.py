"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = 0
    for row in board:
        count += row.count(EMPTY)
    return O if count % 2 == 0 else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    res = set()
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == EMPTY:
                res.add((i, j))
    return res


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError

    new_board = deepcopy(board)
    (i, j) = action
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i, row in enumerate(board):
        # Check row
        if len(set(row)) == 1 and row[0] != EMPTY:
            return row[0]

        # Check col
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]

    # Check diagonal
    center = board[1][1]
    if center == EMPTY:
        return None

    if board[0][0] == center == board[2][2] or board[0][2] == center == board[2][0]:
        return center


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or not actions(board)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    is_maximizing = player(board) == X
    _, best_move = recur(board, is_maximizing)
    return best_move


def recur(board, is_maximizing):
    if terminal(board):
        return utility(board), None

    best_move = None

    if is_maximizing:
        best_score = -math.inf
        for a in actions(board):
            new_board = result(board, a)
            score, _ = recur(new_board, not is_maximizing)
            if score > best_score:
                best_score = score
                best_move = a
    else:
        best_score = math.inf
        for a in actions(board):
            new_board = result(board, a)
            score, _ = recur(new_board, not is_maximizing)
            if score < best_score:
                best_score = score
                best_move = a
    return best_score, best_move
