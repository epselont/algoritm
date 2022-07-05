import sys


def main():
    len_line = int(input())
    line = sys.stdin.readline().rstrip()
    line = line.split()
    result = []
    for word in line:
        if len(word) > len(result):
            result = word
    print(result)
    print(len(result))


if __name__ == '__main__':
    main()
