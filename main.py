import argparse
import math

def is_even(n):
    return n % 2 == 0

def add(x, y):
    return x + y

def factorial(n):
    return math.factorial(n)

def main():
    parser = argparse.ArgumentParser(description="python math CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    parity_parser = subparsers.add_parser("parity", help="parity checking")
    parity_parser.add_argument("n", type=int)

    add_parser = subparsers.add_parser("add", help="add operation")
    add_parser.add_argument("x", type=int)
    add_parser.add_argument("y", type=int)

    fact_parser = subparsers.add_parser("factorial", help="factorial operation")
    fact_parser.add_argument("n", type=int)

    args = parser.parse_args()

    if args.command == "parity":
        result = is_even(args.n)
        parity = "even" if result else "odd"
        print(f"{args.n} is {parity}")
    elif args.command == "add":
        result = add(args.x, args.y)
        print(f"{args.x} + {args.y} = {result}")
    elif args.command == "factorial":
        result = factorial(args.n)
        print(f"{args.n}! = {result}")

if __name__ == "__main__":
    main()
