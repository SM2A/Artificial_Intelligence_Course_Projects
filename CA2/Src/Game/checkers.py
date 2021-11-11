import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from checkers.game import Game
from minimax.minimax import minimax

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')


def getRowColFromMouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def run_game(white_depth, red_depth):

    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.turn == WHITE:
            value, newBoard = minimax(game.getBoard(), white_depth, True, game)
            game.aiMove(newBoard)

        if game.winner() != None:
            print(game.winner())
            run = False

        if game.turn == RED:
            value, newBoard = minimax(game.getBoard(), red_depth, False, game)
            game.aiMove(newBoard)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        game.update()

    pygame.quit()
