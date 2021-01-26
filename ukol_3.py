import argparse
from File import File
from Polylines import Polylines

"""Nacte soubor jako parametr za pomoci modulu Argparse."""
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', required=False, default=None)
parser.add_argument('-l', '--lenght', required=False, default=None)
parser.add_argument('-o', '--output', required=False, default=None)
args = parser.parse_args()
if args.file != None and args.lenght != None and args.output != None:
    input_file = File(args.file)
    output_file = File(args.output)
    data = input_file.read()
    polylines = Polylines(data)
else:
    print("Nezadali jste povinné argumenty (-f pro vstupní geojson, -l pro maximiální délku úsečky a -o pro výstupní geojson")
    exit()