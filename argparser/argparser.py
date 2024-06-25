# using argparser for basic arithmetic opr using positional args
# to make optional use -- infront of the arg name.OPtional provides more clarity but little boring to use
import argparse

print("hellllo")
print(__name__)
if __name__ == "__main__":
    print("hello")
    parser = argparse.ArgumentParser()
    parser.add_argument("num1", metavar="M", type=int, help="1st operand")
    parser.add_argument("num2", metavar="N", type=int, help="2nd operand")
    parser.add_argument(
        "operator", metavar="O", type=str, help="operations (add,sub,mul)"
    )
    args = parser.parse_args()
    print(args.num1)
    print(type(args.num2))
    print(args.operator)
    result = None
    if args.operator == "add":
        result = args.num1 + args.num2
    elif args.operator == "sub":
        result = args.num1 - args.num2
    elif args.operator == "mul":
        result = args.num1 * args.num2
    else:
        print("Invalid operation use 'python argparser.py --h' to see command")
    print(result)
