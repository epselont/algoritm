# 69297715
import sys


def count_step(average, line):
    average = int(average)
    street = line.split()
    position = False
    counter_steps = 0
    for step in range(average):
        if street[step] == '0' and not position:
            position = True
            for step_return in range(step):
                street[step_return] = counter_steps
                counter_steps -= 1
            counter_steps = 1
        elif not position:
            counter_steps += 1
        elif street[step] == '0' and position:
            num = 1
            for step_return in range(step-1, step-(counter_steps//2) - 1, -1):
                street[step_return] = num
                num += 1
            counter_steps = 1
        elif position:
            street[step] = counter_steps
            counter_steps += 1
    return street


def main():
    average = sys.stdin.readline().rstrip()
    line = sys.stdin.readline().rstrip()
    print(*count_step(average, line))


if __name__ == '__main__':
    main()
