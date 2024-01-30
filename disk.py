class Disk:
    def __init__(self, col, row, color):
        self.row = row
        self.col = col
        self.color = color
        self.BOX_SIZE = 90
        self.DISK_SIZE = 80
        self.HALF_BOX_SIZE = self.BOX_SIZE / 2

    def display_disk(self):
        fill(self.color)
        ellipse(self.row*self.BOX_SIZE + self.HALF_BOX_SIZE,
                self.col*self.BOX_SIZE + self.HALF_BOX_SIZE,
                self.DISK_SIZE, self.DISK_SIZE)
