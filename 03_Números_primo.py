
import argparse

parser = argparse.ArgumentParser(description='Programa que averigua qué números son primos')
parser.add_argument('-n1', '--numero1', type=int, required=True, help='Primer número del rango')
parser.add_argument('-n2', '--numero2', type=int, required=True, help='Segundo número del rango')

args = parser.parse_args()

for i in range(args.numero1, args.numero2):
    if i % i == 0 or i % 1 == 0:
        print (f'{i} es un número primo')
    else:
        print (f'{i} no es un número primo')