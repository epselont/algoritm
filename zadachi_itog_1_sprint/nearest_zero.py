import sys


def main():
    average = sys.stdin.readline().rstrip()
    line = sys.stdin.readline().rstrip()
    street = line.split()
    position = []
    for num in range(int(average)):
        if street[num] == '0':
            position.append(num)
    for x in range(int(average)):
        if street[x] != '0':
            min_val = abs(int(position[-1]) - x)
            near = position[-1]
            for val in position:
                if abs(val - x) < min_val:
                    min_val = abs(val - x)
                    near = val
            print(abs(near - x), end=' ')
        else:
            print(0, end=' ')


if __name__ == '__main__':
    main()
