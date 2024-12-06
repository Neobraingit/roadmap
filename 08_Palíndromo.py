
import argparse

parser = argparse.ArgumentParser(description='Comprobador de palíndromos')
parser.add_argument('-p', '--palabra', type=str, required=True, help='Palabra a comprobar')

args = parser.parse_args()

if args.palabra == args.palabra[::-1]:
    print ('Es un palíndromo')
else:
    print ('No es un palíndromo')