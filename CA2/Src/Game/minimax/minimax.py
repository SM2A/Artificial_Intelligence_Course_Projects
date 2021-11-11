import pygame
import copy
import time

RED = (255, 0, 0)
WHITE = (255, 255, 255)


def minimax(position, depth, maxPlayer, game):

    if position.winner() != None or depth == 0:
        return position.evaluate(), position

    if maxPlayer:
        max_val = float('-inf')
        next_move = None
        for move in getAllMoves(position, WHITE):
            eval = minimax(move, depth - 1, False, game)[0]
            max_val = max(max_val, eval)
            if max_val == eval:
                next_move = move
        if next_move is None:
            print("Red is winner")
            time.sleep(5)
            exit(0)
        return max_val, next_move
    else:
        min_val = float('inf')
        next_move = None
        for move in getAllMoves(position, RED):
            eval = minimax(move, depth - 1, True, game)[0]
            min_val = min(min_val, eval)
            if min_val == eval:
                next_move = move
        if next_move is None:
            print("White is winner")
            time.sleep(5)
            exit(0)
        return min_val, next_move


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
            copy_board = copy.deepcopy(board)
            copy_piece = copy_board.getPiece(piece.row, piece.col)
            new_board = simulateMove(copy_piece, move, copy_board, jump)
            all_moves.append(new_board)

    pygame.display.update()
    return all_moves
