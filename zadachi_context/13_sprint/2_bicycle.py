import sys


def binarySearch(arr, x, left, right):
    if (right <= left and left != 0):
        return -1
    mid = (left + right) // 2
    if (arr[mid] >= x and (arr[mid - 1] < x or mid == 0)):
        return mid + 1
    elif x <= arr[mid]:
        return binarySearch(arr, x, left, mid)
    else:
        return binarySearch(arr, x, mid + 1, right)


def day_of_purchase(days, capital, price):
    days = int(days)
    capital = [int(x) for x in capital.split()]
    price = int(price)
    print(binarySearch(capital, price, left=0, right=days), end=' ')
    print(binarySearch(capital, price * 2, left=0, right=days))


def main():

    days = sys.stdin.readline().rstrip()
    capital = sys.stdin.readline().rstrip()
    price = sys.stdin.readline().rstrip()
    day_of_purchase(days, capital, price)


if __name__ == '__main__':
    main()
