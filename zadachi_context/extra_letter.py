import sys


def main():
    first_line = sys.stdin.readline().rstrip()
    second_line = sys.stdin.readline().rstrip()
    first_line = list(first_line)
    second_line = list(second_line)
    for i in first_line:
        if i in second_line:
            second_line.remove(i)
    print(*second_line)


if __name__ == '__main__':
    main()
