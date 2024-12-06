
import argparse

parser = argparse.ArgumentParser(description='Programa que calcula el área de un polígono')
parser.add_argument('-b', '--base', type=float, required=True, help='Base del polígono')
parser.add_argument('-a', '--altura', type=float, required=True, help='Altura del polígono')

args = parser.parse_args()

área = args.base * args.altura

print (f'El área del polígono es de {área}')
    