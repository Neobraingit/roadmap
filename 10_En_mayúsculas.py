
import argparse

parser = argparse.ArgumentParser('Herramienta para poner un texto con las iniciales en mayúsculas')
parser.add_argument('-frase', '--frase', type=str, required=True, help='Frase con la que trabajar')

args = parser.parse_args()

mayus = args.frase.upper()

print (mayus)