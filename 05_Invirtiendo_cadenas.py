import argparse

parser = argparse.ArgumentParser(description='Invierto una palabra')
parser.add_argument('-p', '--palabra', type=str, required=True, help='Palabra a voltear')

args = parser.parse_args()

print (args.palabra)
print (args.palabra[::-1])