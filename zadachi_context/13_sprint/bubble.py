import sys


def bubble_sort(num):
    sort_on = True
    for i in range(len(num) - 1):
        for j in range(0, len(num) - i - 1):
            if num[j+1] < num[j]:
                num[j], num[j+1] = num[j+1], num[j]
                sort_on = True
        if sort_on:
            print(*num)
            sort_on = False


def main():
    num = sys.stdin.readline().rstrip()
    line = sys.stdin.readline().rstrip().rsplit()
    bubble_sort([int(x) for x in line])


if __name__ == '__main__':
    main()
