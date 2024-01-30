from disk import Disk


class Board:
    def __init__(self):
        self.MAX_ROWS = 8
        self.MAX_COLS = 8
        self.board = []
        self.BOX_SIZE = 90
        self.HALF_BOX_SIZE = self.BOX_SIZE / 2
        self.WHITE = 255
        self.BLACK = 0
        self.MATRIX_DIMENSION = 9
        self.WIDTH = (self.MATRIX_DIMENSION - 1) * self.BOX_SIZE
        self.HEIGHT = (self.MATRIX_DIMENSION - 1) * self.BOX_SIZE

    def setup(self):
        for i in range(self.MATRIX_DIMENSION):
            strokeWeight(4)
            line(0, (self.BOX_SIZE*i), self.WIDTH, (self.BOX_SIZE*i))
            line((self.BOX_SIZE*i), 0, (self.BOX_SIZE*i), self.HEIGHT)

    def create_board(self):
        for _ in range(self.MAX_ROWS):
            cur_row = []
            for _ in range(self.MAX_COLS):
                cur_row.append(Disk(360, 360, color=None))
            self.board.append(cur_row)

        self.create_disk()

    def create_disk(self):
        row = self.MAX_ROWS // 2 - 1
        col = self.MAX_COLS // 2 - 1

        mid_dot1 = Disk(row, col, self.WHITE)
        mid_dot2 = Disk(row, col+1, self.BLACK)
        mid_dot3 = Disk(row+1, col, self.BLACK)
        mid_dot4 = Disk(row+1, col+1, self.WHITE)

        mid_dot1.display_disk()
        mid_dot2.display_disk()
        mid_dot3.display_disk()
        mid_dot4.display_disk()

        self.board[row][col] = mid_dot1
        self.board[row][col+1] = mid_dot2
        self.board[row+1][col] = mid_dot3
        self.board[row+1][col+1] = mid_dot4
