from board import Board
from disk import Disk

b = Board()


def test_constructor():
    assert b.MAX_ROWS == 8
    assert b.MAX_COLS == 8
    assert b.board == []
    assert b.BOX_SIZE == 90
    assert b.HALF_BOX_SIZE == b.BOX_SIZE / 2
    assert b.WHITE == 255
    assert b.BLACK == 0
    assert b.MATRIX_DIMENSION == 9
    assert b.WIDTH == (b.MATRIX_DIMENSION - 1) * b.BOX_SIZE
    assert b.HEIGHT == (b.MATRIX_DIMENSION - 1) * b.BOX_SIZE


def test_creat_disk():
    assert b.MAX_ROWS // 2 - 1 == 3
    assert b.MAX_COLS // 2 - 1 == 3
