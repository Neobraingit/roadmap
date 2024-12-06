
import argparse

parser = argparse.ArgumentParser(description='Contamos las palabras de una frase')
parser.add_argument('-frase', '--frase', type=str, required=True, help='Frase para contar')

args = parser.parse_args()


contador = 0
for i in args.frase.split():
    contador += 1
print (f'El número de palabras es de {contador}')
    
