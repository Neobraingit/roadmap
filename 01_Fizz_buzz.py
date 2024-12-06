
import argparse

parser = argparse.ArgumentParser(description="Suma dos números.")
parser.add_argument('--num1', type=int, required=True, help="El primer número.")
parser.add_argument('--num2', type=int, required=True, help="El segundo número.")

args = parser.parse_args()
for i in range(args.num1, args.num2):
    if i % 2 == 0:
        print ('Buzz')
    else:
        print ('Fizz')
    
