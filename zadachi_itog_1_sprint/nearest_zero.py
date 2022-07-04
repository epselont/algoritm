import sys


def main():
    average = sys.stdin.readline().rstrip()
    average = int(average)
    line = sys.stdin.readline().rstrip()
    street = line.split()
    list_distance = []
    position = False
    counter_steps = 0
    for step in range(average):
        if street[step] == '0' and not position:
            position = True
            for step_return in range(step):
                list_distance.insert(step_return, counter_steps)
                counter_steps -= 1
            list_distance.insert(step, counter_steps)
            counter_steps = 1
        elif not position:
            counter_steps += 1
        elif street[step] == '0' and position:
            num = 1
            list_distance.append(0)
            for step_return in range(step-1, step-(counter_steps//2) - 1, -1):
                list_distance[step_return] = num
                num += 1
            counter_steps = 1
        elif position:
            list_distance.append(counter_steps)
            counter_steps += 1
    print(*list_distance)


if __name__ == '__main__':
    main()
