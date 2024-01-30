from board import Board
from disk import Disk
from game import Game
import time
import random

MATRIX_DIMENSION = 9
BOX_SIZE = 90
WIDTH = (MATRIX_DIMENSION - 1) * BOX_SIZE
HEIGHT = (MATRIX_DIMENSION - 1) * BOX_SIZE
BLACK = 0
WHITE = 255
game = Game()
board = Board()


def setup():
    size(WIDTH, HEIGHT)
    background(0, 100, 0)

    global game
    game.init()


def draw():
    if not game.player_turn:
        print("It is computer's turn, please wait for move to be taken")
        random_sec = random.random()*1000
        end_time = millis() + random_sec
        while (millis() < end_time):
            continue

        if not game.has_valid_move(game.computer_disk_color):
            game.player_turn = True
        else:
            game.computer_make_move()

    game.end_when_possible()
    if game.game_ended:
        game.announce_winner()

        redraw()

        # Stop the execution
        noLoop()

    delay(500)


def mousePressed():
    col = int(mouseX//BOX_SIZE)
    row = int(mouseY//BOX_SIZE)

    if game.player_turn:
        print("It is player's turn, please make a move")
        game.player_make_move(row, col)
