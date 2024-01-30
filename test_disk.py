from disk import Disk

t = Disk(0, 0, 0)


def test_constructor():
    assert t.row == 0
    assert t.col == 0
    assert t.color == 0
    assert t.BOX_SIZE == 90
    assert t.DISK_SIZE == 80
    assert t.HALF_BOX_SIZE == t.BOX_SIZE / 2


def test_display_disk():
    assert t.row * t.BOX_SIZE + t.HALF_BOX_SIZE == t.HALF_BOX_SIZE
    assert t.col * t.BOX_SIZE + t.HALF_BOX_SIZE == t.HALF_BOX_SIZE
