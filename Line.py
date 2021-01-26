from math import sqrt

class Line:
    def __init__(self, point1=None):
        self.point1 = point1
        self.point2 = None
        self.length = None

    def set_point1(self, point):
        self.point1 = point

    def set_point2(self, point):
        self.point2 = point

    def get_length(self):
        if self.length != None:
            return self.length
        self.length = sqrt((self.point1.x - self.point2.x)**2 + (self.point1.y - self.point2.y)**2)
        return self.length

    def is_set_point2(self):
        return self.point2 != None

    def is_set_point1(self):
        return self.point1 != None