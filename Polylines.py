from Polyline import Polyline

class Polylines:
    def __init__(self, data):
        self.data = data
        self.polylinesStorage = []
        self.parse()

    def parse(self):
        for data_polyline in self.data:
            try:
                polyline = Polyline(data_polyline["geometry"]["coordinates"])
                self.polylinesStorage.append(polyline)
            except KeyError:
                print("Atribut pro výpočet chybí")
                exit()