import sys


def main():
    line = sys.stdin.readline().rstrip()
    num_list = list(line.split())
    result = [int(x) % 2 for x in num_list]
    if sum(result) == 0:
        print("WIN")
    elif sum(result) == 3:
        print("WIN")
    else:
        print("FAIL")


if __name__ == '__main__':
    main()
