#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    n = len(sys.argv) - 1
    if n != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    ar_op = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in ar_op.keys():
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
