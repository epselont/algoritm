# 69301215
import sys


def sleight_hand(fingers, data):
    fingers = int(fingers) * 2
    data = list(data)
    num_dict = {x: data.count(x) for x in [x for x in set(data)]}
    count = 0
    for sec in range(10):
        if str(sec) in num_dict.keys():
            if num_dict[str(sec)] <= fingers:
                count += 1
    return count


def main():
    fingers = sys.stdin.readline().rstrip()
    line = sys.stdin.readline().rstrip()
    data = line.replace('.', '')
    while line != '':
        line = sys.stdin.readline().rstrip()
        data += line.replace('.', '')
    print(sleight_hand(fingers, data))


if __name__ == '__main__':
    main()
