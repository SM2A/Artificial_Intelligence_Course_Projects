from copy import deepcopy
import pygame

RED = (255, 0, 0)
WHITE = (255, 255, 255)


def minimax(position, depth, maxPlayer, game):

    if position.winner() != None or depth == 0:
        return position.evaluate(), position

    if maxPlayer:
        max_val = float('-inf')
        best_move = None
        for move in getAllMoves(position, WHITE):
            evaluated = minimax(move, depth - 1, False, game)[0]
            max_val = max(max_val, evaluated)
            if max_val == evaluated:
                best_move = move
        return max_val, best_move
    else:
        min_val = float('inf')
        best_move = None
        for move in getAllMoves(position, RED):
            evaluated = minimax(move, depth - 1, True, game)[0]
            min_val = min(min_val, evaluated)
            if min_val == evaluated:
                best_move = move
        return min_val, best_move


def simulateMove(piece, move, board, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)
    return board


def getAllMoves(board, color):
    all_moves = []
    for piece in board.getAllPieces(color):
        valid_moves = board.getValidMoves(piece)
        for move, jump in valid_moves.items():
            copy_board = deepcopy(board)
            copy_piece = copy_board.getPiece(piece.row, piece.col)
            new_board = simulateMove(copy_piece, move, copy_board, jump)
            all_moves.append(new_board)

    pygame.display.update()
    return all_moves
