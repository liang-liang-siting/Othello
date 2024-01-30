from game import Game
from board import Board
from disk import Disk

g = Game()
for _ in range(g.MAX_ROWS):
    cur_row = []
    for _ in range(g.MAX_COLS):
        cur_row.append(Disk(360, 360, color=None))
    g.board.board.append(cur_row)


row = g.MAX_ROWS // 2 - 1
col = g.MAX_COLS // 2 - 1

mid_disk1 = Disk(col, row, g.WHITE)
mid_disk2 = Disk(col, row+1, g.BLACK)
mid_disk3 = Disk(col+1, row, g.BLACK)
mid_disk4 = Disk(col+1, row+1, g.WHITE)
disk5 = Disk(2, 3, g.BLACK)
disk6 = Disk(3, 2, g.BLACK)
disk7 = Disk(2, 5, g.WHITE)
disk8 = Disk(1, 6, g.BLACK)
disk9 = Disk(2, 2, g.BLACK)
disk10 = Disk(1, 1, g.WHITE)

g.board.board[col][row] = mid_disk1
g.board.board[col][row+1] = mid_disk2
g.board.board[col+1][row+1] = mid_disk4
g.board.board[col+1][row] = mid_disk3
g.board.board[2][3] = disk5
g.board.board[3][2] = disk6
g.board.board[2][5] = disk7
g.board.board[1][6] = disk8
g.board.board[2][2] = disk9
g.board.board[1][1] = disk10


def test_constructor():
    assert g.MAX_ROWS == 8
    assert g.MAX_COLS == 8
    assert g.BOX_SIZE == 90
    assert g.HALF_BOX_SIZE == g.BOX_SIZE / 2
    assert g.WHITE == 255
    assert g.BLACK == 0
    assert g.player_disk_color == g.BLACK
    assert g.computer_disk_color == g.WHITE
    assert g.computer_disk_count == 2
    assert g.player_disk_count == 2
    assert g.player_turn is True
    assert g.game_ended is False
    assert g.name == ''
    assert g.MATRIX_DIMENSION == 9
    assert g.WIDTH == (g.MATRIX_DIMENSION - 1) * g.BOX_SIZE
    assert g.HEIGHT == (g.MATRIX_DIMENSION - 1) * g.BOX_SIZE


def test_is_within_range():
    assert g.is_within_range(0, 0) is True
    assert g.is_within_range(7, 7) is True
    assert g.is_within_range(3, 3) is True
    assert g.is_within_range(360, 360) is False


def test_is_valid_move():
    assert g.is_valid_move(0, 0, 0) is True
    assert g.is_valid_move(3, 3, 255) is False
    assert g.is_valid_move(5, 3, 255) is True


def test_is_valid_vertically_towards_bottom():
    assert g.is_valid_vertically_towards_bottom(2, 3, 0) is True
    assert g.is_valid_vertically_towards_bottom(5, 3, 255) is False


def test_is_valid_vertically_towards_top():
    assert g.is_valid_vertically_towards_top(4, 3, 0) is True
    assert g.is_valid_vertically_towards_top(3, 3, 255) is False


def test_is_valid_horizontally_towards_right():
    assert g.is_valid_horizontally_towards_right(3, 2, 0) is True
    assert g.is_valid_horizontally_towards_right(4, 2, 0) is False


def test_is_valid_horizontally_towards_left():
    assert g.is_valid_horizontally_towards_left(3, 4, 0) is True
    assert g.is_valid_horizontally_towards_left(4, 4, 0) is False


def test_is_valid_diagonally_towards_bottom_right():
    assert g.is_valid_diagonally_towards_bottom_right(1, 1, 255) is True
    assert g.is_valid_diagonally_towards_bottom_right(3, 3, 255) is False


def test_is_valid_diagonally_towards_top_left():
    assert g.is_valid_diagonally_towards_top_left(3, 3, 255) is True
    assert g.is_valid_diagonally_towards_top_left(1, 1, 255) is False


def test_is_valid_diagonally_towards_bottom_left():
    assert g.is_valid_diagonally_towards_bottom_left(1, 6, 0) is True
    assert g.is_valid_diagonally_towards_bottom_left(2, 5, 0) is False


def test_is_valid_diagonally_towards_top_right():
    assert g.is_valid_diagonally_towards_top_right(3, 4, 0) is True
    assert g.is_valid_diagonally_towards_top_right(2, 4, 0) is False

# only work with the local path file
# def test_is_score_higher():
#     g.player_disk_count = 10
#     g.is_score_higher() is False
#     g.player_disk_count = 70
#     g.is_score_higher() is True
