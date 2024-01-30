from board import Board
from disk import Disk
import re
import time


class Game:
    def __init__(self):
        self.board = Board()
        self.MAX_ROWS = 8
        self.MAX_COLS = 8
        self.BOX_SIZE = 90
        self.HALF_BOX_SIZE = self.BOX_SIZE / 2
        self.WHITE = 255
        self.BLACK = 0
        self.player_disk_color = self.BLACK
        self.computer_disk_color = self.WHITE
        self.computer_disk_count = 2
        self.player_disk_count = 2
        self.player_turn = True
        self.game_ended = False
        self.name = ''
        self.MATRIX_DIMENSION = 9
        self.WIDTH = (self.MATRIX_DIMENSION - 1) * self.BOX_SIZE
        self.HEIGHT = (self.MATRIX_DIMENSION - 1) * self.BOX_SIZE

    def init(self):
        self.board.setup()
        self.board.create_board()

    def player_make_move(self, row, col):
        if not self.has_valid_move(self.player_disk_color):
            self.player_turn = False
        elif self.is_valid_move(row, col, self.player_disk_color):
            new_disk = Disk(row, col, self.player_disk_color)
            new_disk.display_disk()
            self.board.board[row][col] = new_disk
            self.player_disk_count += 1
            self.player_turn = False
            self.flip_disks(row, col, self.player_disk_color)
        else:
            print("Invalid move, please try again")

    def computer_make_move(self):
        # Try all the tiles, and place the disk on the
        # first valid move that it can find
        for row in range(self.MAX_ROWS):
            for col in range(self.MAX_COLS):
                if self.is_valid_move(row, col, self.computer_disk_color):
                    new_disk = Disk(row, col, self.computer_disk_color)
                    new_disk.display_disk()
                    self.board.board[row][col] = new_disk
                    self.computer_disk_count += 1
                    self.flip_disks(row, col, self.computer_disk_color)
                    self.player_turn = True
                    return

    def is_within_range(self, row, col):
        # Check if the row and col is within boundary
        if (row < 0 or row >= self.MAX_ROWS or col < 0
                or col >= self.MAX_COLS):
            return False
        return True

    def is_valid_move(self, row, col, color):
        if not self.is_within_range(row, col):
            return False

        # Check if there is already disk placed on that tile
        if self.board.board[row][col].color is not None:
            return False

        # It is a valid move, if it can find a disk of the same color
        # horizontall/vertically/diagonally
        # - Doesn't have any empty gap inbetween
        # - Must contain at least one opponent's chip IN BETWEEN its disks

        if self.is_valid_vertically_towards_bottom(row, col, color):
            return True

        if self.is_valid_vertically_towards_top(row, col, color):
            return True

        if self.is_valid_horizontally_towards_right(row, col, color):
            return True

        if self.is_valid_horizontally_towards_left(row, col, color):
            return True

        if self.is_valid_diagonally_towards_bottom_right(row, col, color):
            return True

        if self.is_valid_diagonally_towards_top_left(row, col, color):
            return True

        if self.is_valid_diagonally_towards_bottom_left(row, col, color):
            return True

        if self.is_valid_diagonally_towards_top_right(row, col, color):
            return True

        return False

    def is_valid_vertically_towards_bottom(self, row, col, color):
        has_space = False
        has_own_disk = False
        has_opponent_disk = False
        for next_row in range(row + 1, self.MAX_ROWS):
            if self.board.board[next_row][col].color is None:
                break
            if (self.board.board[next_row][col].color == color and
                    has_opponent_disk is False):
                break
            if self.board.board[next_row][col].color != color:
                has_opponent_disk = True
            if (has_opponent_disk and
                    self.board.board[next_row][col].color == color):
                has_own_disk = True
            if has_own_disk and has_opponent_disk:
                return True
        return False

    def is_valid_vertically_towards_top(self, row, col, color):
        has_space = False
        has_own_disk = False
        has_opponent_disk = False
        for next_row in range(row - 1, -1, -1):
            if self.board.board[next_row][col].color is None:
                break
            if (self.board.board[next_row][col].color == color and
                    has_opponent_disk is False):
                break
            if self.board.board[next_row][col].color != color:
                has_opponent_disk = True
            if (has_opponent_disk and
                    self.board.board[next_row][col].color == color):
                has_own_disk = True
            if has_own_disk and has_opponent_disk:
                return True
        return False

        # Check horizontally

    def is_valid_horizontally_towards_right(self, row, col, color):
        has_space = False
        has_own_disk = False
        has_opponent_disk = False
        for next_col in range(col + 1, self.MAX_COLS):
            if self.board.board[row][next_col].color is None:
                break
            if (self.board.board[row][next_col].color == color and
                    has_opponent_disk is False):
                break
            if self.board.board[row][next_col].color != color:
                has_opponent_disk = True
            if (has_opponent_disk and
                    self.board.board[row][next_col].color == color):
                has_own_disk = True
            if has_own_disk and has_opponent_disk:
                return True
        return False

    def is_valid_horizontally_towards_left(self, row, col, color):
        has_space = False
        has_own_disk = False
        has_opponent_disk = False
        for next_col in range(col - 1, -1, -1):
            if self.board.board[row][next_col].color is None:
                break
            if (self.board.board[row][next_col].color == color and
                    has_opponent_disk is False):
                break
            if self.board.board[row][next_col].color != color:
                has_opponent_disk = True
            if (has_opponent_disk and
                    self.board.board[row][next_col].color == color):
                has_own_disk = True
            if has_own_disk and has_opponent_disk:
                return True
        return False

    def is_valid_diagonally_towards_bottom_right(self, row, col, color):
        has_space = False
        has_own_disk = False
        has_opponent_disk = False
        for i in range(1, self.MAX_ROWS):
            if self.is_within_range(row + i, col + i):
                if self.board.board[row + i][col + i].color is None:
                    break
                if (self.board.board[row + i][col + i].color == color and
                        has_opponent_disk is False):
                    break
                if self.board.board[row + i][col + i].color != color:
                    has_opponent_disk = True
                if (has_opponent_disk and
                        self.board.board[row + i][col + i].color == color):
                    has_own_disk = True
                if has_own_disk and has_opponent_disk:
                    return True
        return False

    def is_valid_diagonally_towards_top_left(self, row, col, color):
        has_space = False
        has_own_disk = False
        has_opponent_disk = False
        for i in range(1, self.MAX_ROWS):
            if self.is_within_range(row - i, col - i):
                if self.board.board[row - i][col - i].color is None:
                    break
                if (self.board.board[row - i][col - i].color == color and
                        has_opponent_disk is False):
                    break
                if self.board.board[row - i][col - i].color != color:
                    has_opponent_disk = True
                if (has_opponent_disk and
                        self.board.board[row - i][col - i].color == color):
                    has_own_disk = True
                if has_own_disk and has_opponent_disk:
                    return True
        return False

    def is_valid_diagonally_towards_bottom_left(self, row, col, color):
        has_space = False
        has_own_disk = False
        has_opponent_disk = False
        for i in range(1, self.MAX_ROWS):
            if self.is_within_range(row + i, col - i):
                if self.board.board[row + i][col - i].color is None:
                    break
                if (self.board.board[row + i][col - i].color == color and
                        has_opponent_disk is False):
                    break
                if self.board.board[row + i][col - i].color != color:
                    has_opponent_disk = True
                if (has_opponent_disk and
                        self.board.board[row + i][col - i].color == color):
                    has_own_disk = True
                if has_own_disk and has_opponent_disk:
                    return True
        return False

    def is_valid_diagonally_towards_top_right(self, row, col, color):
        has_space = False
        has_own_disk = False
        has_opponent_disk = False
        for i in range(1, self.MAX_ROWS):
            if self.is_within_range(row - i, col + i):
                if self.board.board[row - i][col + i].color is None:
                    break
                if (self.board.board[row - i][col + i].color == color and
                        has_opponent_disk is False):
                    break
                if self.board.board[row - i][col + i].color != color:
                    has_opponent_disk = True
                if (has_opponent_disk and
                        self.board.board[row - i][col + i].color == color):
                    has_own_disk = True
                if has_own_disk and has_opponent_disk:
                    return True
        return False

    def has_valid_move(self, color):
        for row in range(self.MAX_ROWS):
            for col in range(self.MAX_COLS):
                if self.is_valid_move(col, row, color):
                    return True
        return False

    def end_when_possible(self):
        if (self.has_valid_move(self.player_disk_color) is False and
                self.has_valid_move(self.computer_disk_color) is False):
            print("Game Over!")
            self.save_score()
            self.game_ended = True

    def flip_disks(self, row, col, color):
        if self.is_valid_vertically_towards_bottom(row, col, color):
            for next_row in range(row + 1, self.MAX_ROWS):
                if self.board.board[next_row][col].color is None:
                    break
                if self.board.board[next_row][col].color == color:
                    break
                if self.board.board[next_row][col].color != color:
                    self.board.board[next_row][col].color = color
                    if color == self.computer_disk_color:
                        self.computer_disk_count += 1
                        self.player_disk_count -= 1
                    if color == self.player_disk_color:
                        self.computer_disk_count -= 1
                        self.player_disk_count += 1
                    self.board.board[next_row][col].display_disk()

        if self.is_valid_vertically_towards_top(row, col, color):
            for next_row in range(row - 1, -1, -1):
                if self.board.board[next_row][col].color is None:
                    break
                if self.board.board[next_row][col].color == color:
                    break
                if self.board.board[next_row][col].color != color:
                    self.board.board[next_row][col].color = color
                    if color == self.computer_disk_color:
                        self.computer_disk_count += 1
                        self.player_disk_count -= 1
                    if color == self.player_disk_color:
                        self.computer_disk_count -= 1
                        self.player_disk_count += 1
                    self.board.board[next_row][col].display_disk()

        if self.is_valid_horizontally_towards_right(row, col, color):
            for next_col in range(col + 1, self.MAX_COLS):
                if self.board.board[row][next_col].color is None:
                    break
                if self.board.board[row][next_col].color == color:
                    break
                if self.board.board[row][next_col].color != color:
                    self.board.board[row][next_col].color = color
                    if color == self.computer_disk_color:
                        self.computer_disk_count += 1
                        self.player_disk_count -= 1
                    if color == self.player_disk_color:
                        self.computer_disk_count -= 1
                        self.player_disk_count += 1
                    self.board.board[row][next_col].display_disk()

        if self.is_valid_horizontally_towards_left(row, col, color):
            for next_col in range(col - 1, -1, -1):
                if self.board.board[row][next_col].color is None:
                    break
                if self.board.board[row][next_col].color == color:
                    break
                if self.board.board[row][next_col].color != color:
                    self.board.board[row][next_col].color = color
                    if color == self.computer_disk_color:
                        self.computer_disk_count += 1
                        self.player_disk_count -= 1
                    if color == self.player_disk_color:
                        self.computer_disk_count -= 1
                        self.player_disk_count += 1
                    self.board.board[row][next_col].display_disk()

        if self.is_valid_diagonally_towards_bottom_right(row, col, color):
            for i in range(1, self.MAX_ROWS):
                if self.is_within_range(row + i, col + i):
                    if self.board.board[row + i][col + i].color is None:
                        break
                    if self.board.board[row + i][col + i].color == color:
                        break
                    if self.board.board[row + i][col + i].color != color:
                        self.board.board[row + i][col + i].color = color
                        if color == self.computer_disk_color:
                            self.computer_disk_count += 1
                            self.player_disk_count -= 1
                        if color == self.player_disk_color:
                            self.computer_disk_count -= 1
                            self.player_disk_count += 1
                        self.board.board[row + i][col + i].display_disk()

        if self.is_valid_diagonally_towards_top_left(row, col, color):
            for i in range(1, self.MAX_ROWS):
                if self.is_within_range(row - i, col - i):
                    if self.board.board[row - i][col - i].color is None:
                        break
                    if self.board.board[row - i][col - i].color == color:
                        break
                    if self.board.board[row - i][col - i].color != color:
                        self.board.board[row - i][col - i].color = color
                        if color == self.computer_disk_color:
                            self.computer_disk_count += 1
                            self.player_disk_count -= 1
                        if color == self.player_disk_color:
                            self.computer_disk_count -= 1
                            self.player_disk_count += 1
                        self.board.board[row - i][col - i].display_disk()

        if self.is_valid_diagonally_towards_bottom_left(row, col, color):
            for i in range(1, self.MAX_ROWS):
                if self.is_within_range(row + i, col - i):
                    if self.board.board[row + i][col - i].color is None:
                        break
                    if self.board.board[row + i][col - i].color == color:
                        break
                    if self.board.board[row + i][col - i].color != color:
                        self.board.board[row + i][col - i].color = color
                        if color == self.computer_disk_color:
                            self.computer_disk_count += 1
                            self.player_disk_count -= 1
                        if color == self.player_disk_color:
                            self.computer_disk_count -= 1
                            self.player_disk_count += 1
                        self.board.board[row + i][col - i].display_disk()

        if self.is_valid_diagonally_towards_top_right(row, col, color):
            for i in range(1, self.MAX_ROWS):
                if self.is_within_range(row - i, col + i):
                    if self.board.board[row - i][col + i].color is None:
                        break
                    if self.board.board[row - i][col + i].color == color:
                        break
                    if self.board.board[row - i][col + i].color != color:
                        self.board.board[row - i][col + i].color = color
                        if color == self.computer_disk_color:
                            self.computer_disk_count += 1
                            self.player_disk_count -= 1
                        if color == self.player_disk_color:
                            self.computer_disk_count -= 1
                            self.player_disk_count += 1
                        self.board.board[row - i][col + i].display_disk()
        return

    def announce_winner(self):
        if self.computer_disk_count > self.player_disk_count:
            screen_message = "WHITE WINS!! Result is {}:{}".format(
                self.player_disk_count, self.computer_disk_count)
        elif self.computer_disk_count == self.player_disk_count:
            screen_message = "IT IS A TIE!! Result is {}:{}".format(
                self.player_disk_count, self.computer_disk_count)
        else:
            screen_message = "BLACK WINS!! Result is {}:{}".format(
                self.player_disk_count, self.computer_disk_count)
        
        fill(255, 0, 0)
        textSize(40)
        text(screen_message, 0, self.HEIGHT / 2)

        print(screen_message)


    def is_score_higher(self):
        """if the current score is higher"""
        # without the path, it can't open and finish the pytest on my computer
        # Here is the normal one below. Thank you!
        # with open('/Users/liangsiting/CS5001/hw12/othello/scores.txt',
        #           'r')as f:
        with open('scores.txt', 'r')as f:
            old_score = f.readline()
            for score in re.findall(r'([0-9]+)\n', old_score):
                if self.player_disk_count <= int(score):
                    return False
        return True

    def input(self, message=''):
        """get a input string"""
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, message)

    def save_score(self):
        """save the current score"""
        self.name = self.input("Please Enter your name:")
        with open('scores.txt', 'r') as f:
            old_scores = f.read()
        if self.is_score_higher():
            with open('scores.txt', 'w') as f:
                f.write(self.name + " " +
                        str(self.player_disk_count) + "\n")
                f.write(old_scores)
        else:
            with open('scores.txt', 'a') as f:
                f.write(self.name + " " +
                        str(self.player_disk_count) + "\n")
        return False