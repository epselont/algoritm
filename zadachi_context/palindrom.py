import sys


def main():
    line = sys.stdin.readline().rstrip()
    line = line.lower()
    word = "".join(i for i in line if i.isalpha())
    result = word[::-1]
    if result == word:
        print(True)
    else:
        print(False)


if __name__ == '__main__':
    main()
