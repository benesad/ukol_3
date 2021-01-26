from Point import Point
from Line import Line

class Polyline:
    def __init__(self, data_of_points):
        self.lines = []
        tmpLine = Line()
        
        for data_point in data_of_points:
            point = Point(data_point[0], data_point[1])
            