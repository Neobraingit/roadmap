
import argparse

parser = argparse.ArgumentParser(description='Comprobamos si las palabras son anagramas')
parser.add_argument('-p', '--palabra1', type=str, required=True, help='Primera palabra a comprobar')
parser.add_argument('-p2', '--palabra2', type=str, required=True, help='Segunda palabra a comprobar')

args = parser.parse_args()

args.palabra1 = args.palabra1.lower().replace(' ', '')
args.palabra2 = args.palabra2.lower().replace(' ', '')

if sorted(args.palabra1) == sorted(args.palabra2):
    print ('Son anagramas')
else:
    print ('No son anagramas')
        