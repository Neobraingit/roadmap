
import datetime
import argparse

parser = argparse.ArgumentParser(description='Cálculo de  fechas')
parser.add_argument('-f', '--fecha', required=True, help='Fecha actual')
parser.add_argument('-fp', '--fechapasada', required=True, help='Fecha pasada')

args = parser.parse_args()

print (int(args.fecha) / int(args.fechapasada))

