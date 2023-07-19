#!/usr/bin/python3

if __name__ == "__main__":
    """Handle basic arithmetic operations."""
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    ops = {"+": add, "-": sub, "*": mul, "/": div}

    if argv[2] in ops:
        num1 = int(argv[1])
        num2 = int(argv[3])
        op = ops[argv[2]]
        result = op(num1, num2)
        print('{:d} {:s} {:d} = {:d}'.format(num1, argv[2], num2, result))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    exit(0)
