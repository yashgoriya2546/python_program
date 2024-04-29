import argparse
import sys

def calc(args):
    if args.o == 'add':
        return args.x + args.y

    elif args.o == 'sub':
        return args.x - args.y

    elif args.o == 'mul':
        return args.x * args.y

    elif args.o == 'div':
        return args.x / args.y

    else:
        print('write a something')

parser = argparse.ArgumentParser()
parser.add_argument('--x',type=int,default=1,help="enter the first number...")

parser.add_argument('--y',type=int,default=2,help="enter the second number...")

parser.add_argument('--o',type=str,default='add',help="This is a utilities of calculation")

args = parser.parse_args()
sys.stdout.write(str(calc(args)))