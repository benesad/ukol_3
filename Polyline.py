from Point import Point
import Line

class Polyline:
    def __init__(self, data=None):
        self.lines = []
        self.data = data
        if data!=None:
            self.parse()

    def parse(self):
        tmpLine = Line.Line()
        for data_point in self.data["geometry"]["coordinates"]:
            point = Point(data_point[0], data_point[1])
            if tmpLine.point1!=None:
                tmpLine.point2 = point
                self.add_line(tmpLine)
                tmpLine = Line.Line(point)
            else: 
                tmpLine.point1 = point

    def add_line(self, line):
        self.lines.append(line)

    def add_polyline(self, polyline):
        for line in polyline.lines:
            self.add_line(line)

    def divide_long_segments(self, max_length):
        new_polyline = Polyline()
        new_polyline.data = self.data

        for line in self.lines:
            tmp_polyline = line.divide(max_length)
            new_polyline.add_polyline(tmp_polyline)

        return new_polyline

    def get_object_for_json(self):
        coordinates = []
        was_first = False
        for line in self.lines:
            if not was_first:
                coordinates.append([line.point1.x, line.point1.y])
                was_first = True
            coordinates.append([line.point2.x, line.point2.y])
        self.data["geometry"]["coordinates"] = coordinates
        return self.data