from math import sqrt

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        self.length = sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)