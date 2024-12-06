
import argparse

parser = argparse.ArgumentParser(description='Eliminamos caracteres')
parser.add_argument('-f', '--frase', type=str, required=True, help='Frase a reemplazar')

args = parser.parse_args()

print (args.frase.replace('s', ' '))