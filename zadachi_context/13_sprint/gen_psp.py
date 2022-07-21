import sys


def gen_psp(count, line='', left=0, right=0):
    if left == count and right == count:
        print(line)
    else:
        if left < count:
            gen_psp(count, line + '(', left + 1, right)
        if right < left:
            gen_psp(count, line + ')', left, right + 1)


def main():
    num = sys.stdin.readline().rstrip()
    gen_psp(count=int(num))


if __name__ == '__main__':
    main()
