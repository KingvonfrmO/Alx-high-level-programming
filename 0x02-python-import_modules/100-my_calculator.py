from calculator_1 import add, sub, mul, div
import sys

count = len(sys.argv)
if count - 1 != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)
    
operators = {"+":add,"-":sub,"*":mul,"/":div}

if sys.argv[2] not in list(operators.keys()):
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)

a = int(sys.argv[1])
b = int(sys.argv[3])

op = sys.argv[2]
result = operators[op](a, b)

print("{} {} {} = {}".format(a, sys.argv[2], b, result))