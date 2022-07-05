import sys


def main():
    line = sys.stdin.readline().rstrip()
    num = int(line)
    while num and not (num & 3):
        num >>= 2
    print(num == 1)


if __name__ == '__main__':
    main()
