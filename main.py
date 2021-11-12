import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from checkers.game import Game
from minimax.minimax import minimax

FPS = 60
DELAY = 400

WHITE_DEPTH = 3
RED_DEPTH = 1

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Moein Shafi - 810196492 - Checkers')

if __name__ == '__main__':
    clock = pygame.time.Clock()
    game = Game(WIN)

    while True:
        clock.tick(FPS)

        if game.winner() != None:
            print(game.winner())
            break

        if game.turn == WHITE:
            value, newBoard = minimax(game.getBoard(), WHITE_DEPTH, True)
            game.aiMove(newBoard)

        elif game.turn == RED:
            value, newBoard = minimax(game.getBoard(), RED_DEPTH, False)
            game.aiMove(newBoard)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break

        game.update()
        pygame.time.delay(DELAY)

    pygame.time.delay(DELAY * 5)
    pygame.quit()
