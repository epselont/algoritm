import sys


def main():
    average = sys.stdin.readline().rstrip()
    line = sys.stdin.readline().rstrip()
    num = sys.stdin.readline().rstrip()
    line = int(line.replace(' ', ''))
    result = int(num) + int(line)
    print(" ".join(str(result)))


if __name__ == '__main__':
    main()
