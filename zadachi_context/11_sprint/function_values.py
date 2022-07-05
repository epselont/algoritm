import sys


def main():
    line = sys.stdin.readline().rstrip()
    a, x, b, c = line.split()
    a = int(a)
    b = int(b)
    c = int(c)
    x = int(x)
    result = a * x * x + b * x + c
    print(result)


if __name__ == '__main__':
    main()
