

class worker(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 5

        self.left = False
        self.right = False
        self.up = False
        self.down = False