import sys


def main():
    line = sys.stdin.readline().rstrip()
    num_list = list(line.split())
    if (int(num_list[0]) % 2 == 0) and (int(num_list[1]) % 2 == 0) and (int(num_list[2]) % 2 == 0):
        print("WIN")
    elif (int(num_list[0]) % 2 == 1) and (int(num_list[1]) % 2 == 1) and (int(num_list[2]) % 2 == 1):
        print("WIN")
    else:
        print("FAIL")


if __name__ == '__main__':
    main()
