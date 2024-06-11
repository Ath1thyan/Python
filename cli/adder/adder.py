import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument('greeting', help='The greeting message')
parser.add_argument('-n', '--nums', type=float, nargs='*', help='The numbers to be added')
parser.add_argument('-v', '--verbose', type=int, choices=[0, 1, 2], help='Determines how much info is displayed')
parser.add_argument('--debug', action='store_true', help='Enables debug mode')

args = parser.parse_args()

if args.debug:
    start = time.perf_counter()

print(args)
print(args.nums)

if args.verbose is None:
    print(args.greeting)
    if args.nums is not None:
        print(sum(args.nums))
else:
    if args.verbose >= 0:
        print(args.greeting)
        if args.nums is not None:
            print(sum(args.nums))
    if args.verbose >= 1:
        print(args.nums)
    if args.verbose == 2:
        print('Extra info')

if args.debug:
    end = time.perf_counter()
    print(f'Finished in {round(end - start, 2)} seconds')
