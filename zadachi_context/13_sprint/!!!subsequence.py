import sys


def find_chars(chars, line):
    line = set(line)
    for char in chars:
        if char not in line:
            return False
    return True


def main():
    chars = sys.stdin.readline().rstrip()
    line = sys.stdin.readline().rstrip()

    print(find_chars(list(chars), line))


if __name__ == '__main__':
    main()
