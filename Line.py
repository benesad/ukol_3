from math import sqrt
from Polyline import Polyline
from Point import Point

class Line:
    def __init__(self, point1=None, point2=None):
        self.point1 = point1
        self.point2 = point2
        self.length = None
        self.middle_point = None

    def set_point1(self, point):
        self.point1 = point

    def set_point2(self, point):
        self.point2 = point
        self.length = sqrt((self.point1.x - self.point2.x)**2 + (self.point1.y - self.point2.y)**2)

    def is_set_point2(self):
        return self.point2 != None

    def is_set_point1(self):
        return self.point1 != None

    def compute_middle_point(self):
        middle_x = self.compute_middle_coordinate(self.point1.x, self.point2.x)
        middle_y = self.compute_middle_coordinate(self.point1.y, self.point2.y)
        self.middle_point = Point(middle_x, middle_y)

    def compute_middle_coordinate(self, coordinate1, coordinate2):
        farther = coordinate1
        closer = coordinate2

        if closer>farther:
            farther = closer
            closer = farther

        return (((farther-closer)/2)+closer)

    def divide(self, max_length):
        polyline = Polyline()

        if self.length>max_length:
            self.compute_middle_point()
            polyline.addLine(Line(self.point1, self.middle_point))
            polyline.addLine(Line(self.middle_point, self.point2))
            return polyline

        polyline.addLine(self)
        return polyline