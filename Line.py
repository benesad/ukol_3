from math import sqrt
import Polyline
from Point import Point

class Line:
    def __init__(self, point1=None, point2=None):
        self.point1 = point1
        self.point2 = point2
        self.length = None
        self.middle_point = None

    def compute_middle_point(self):
        middle_x = self.compute_middle_coordinate(self.point1.x, self.point2.x)
        middle_y = self.compute_middle_coordinate(self.point1.y, self.point2.y)
        self.middle_point = Point(middle_x, middle_y)

    def compute_middle_coordinate(self, coordinate1, coordinate2):
        return (coordinate1+coordinate2)/2

    def divide(self, max_length):
        polyline = Polyline.Polyline()
        self.length = sqrt((self.point1.x - self.point2.x)**2 + (self.point1.y - self.point2.y)**2)

        if self.length>max_length:
            self.compute_middle_point()
            polyline.add_line(Line(self.point1, self.middle_point))
            polyline.add_line(Line(self.middle_point, self.point2))
            return polyline.divide_long_segments(max_length)

        polyline.add_line(self)
        return polyline