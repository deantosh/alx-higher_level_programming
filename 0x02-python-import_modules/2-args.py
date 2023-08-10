#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    n = len(sys.argv)
    index = 1

    if n == 1:
        print("0 arguments.")
    elif n == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(n - 1))
        for i in sys.argv:
            if i == "./2-args.py":
                continue
            print("{}: {}".format(index, i))
            index = index + 1
