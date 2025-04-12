import argparse
import math

def is_even(n):
    return n % 2 == 0

def main():
    parser = argparse.ArgumentParser(description="python math CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    parity_parser = subparsers.add_parser("parity", help="parity checking")
    parity_parser.add_argument("n", type=int)

    args = parser.parse_args()

    if args.command == "parity":
        result = is_even(args.n)
        parity = "even" if result else "odd"
        print(f"{args.n} is {parity}")

if __name__ == "__main__":
    main()
