import sys


def main():
    line = sys.stdin.readline().rstrip()
    line = int(line)
    result = []
    while line != 0:
        result.append(line % 2)
        line //= 2
    result = [str(x) for x in result[::-1]]
    print("".join(result))


if __name__ == '__main__':
    main()
