import sys


def main():
    line = sys.stdin.readline().rstrip()
    num = int(line)
    i = 2
    while i * i <= num:
        while num % i == 0:
            print(i, end=' ')
            num = num // i
        i = i + 1
    if num > 1:
        print(num, end=' ')


if __name__ == '__main__':
    main()
