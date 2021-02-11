import argparse
from File import File
from Polyline import Polyline

def parse(data, max_length):
    polylines = []
    for data_polyline in data:
        try:
            if data_polyline["geometry"]["type"]=="LineString":
                polyline = Polyline(data_polyline)
                polylines.append(polyline.divide_long_segments(max_length))
            else:
                print("Preskakuju Feature s OBJECTID: ", data_polyline["properties"]["OBJECTID"],", protoze se nejedna o LineString")
        except KeyError:
            print("Atribut pro vypocet chybi")
            exit()
    return polylines


"""Nacte soubor jako parametr za pomoci modulu Argparse."""
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', required=False, default=None)
parser.add_argument('-l', '--length', required=False, default=None)
parser.add_argument('-o', '--output', required=False, default=None)
args = parser.parse_args()
if args.file != None and args.length != None and args.output != None:
    file = File(args.file)

    data = file.read()
    file.polylines = parse(data, float(args.length))
    file.name = args.output
    file.write()
else:
    print("Nezadali jste povinne argumenty (-f pro vstupni geojson, -l pro maximialni délku usecky a -o pro vystupni geojson")
    exit()