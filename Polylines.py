class Polylines:
    def __init__(self, data):
        self.data = data
        self.polylinesStorage = []

    def parse():
        for data_polyline in data:
            try:
                polyline data_polyline["geometry"]["coordinates"]
            except KeyError:
                print("Atribut pro výpočet chybí")

    def compression():
