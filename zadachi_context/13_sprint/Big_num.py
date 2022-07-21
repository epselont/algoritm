import sys

num_alph = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
}


def gen_psp(digit, prefix=None):
    prefix = prefix or str()
    if digit == '':
        print(prefix, end=' ')
        return
    for char in num_alph[digit[0]]:
        prefix += char
        gen_psp(digit[1:], prefix)
        prefix = prefix[:-1]


def main():
    num = sys.stdin.readline().rstrip()
    gen_psp(num)


if __name__ == '__main__':
    main()
