# x = 4

# for i in range(1, 6):
#     print(f"{x} в степени {i}: {x ** i}")

# x = 2

# for i in range(2, 1000, 2):
#     print(f"{x} в степени {i}: {x ** i}")

# x = 4
# for i in range(2, 10, 2):
#     print(x * i, i)
# x = 4
# num = 10
# result = []
# while num != 0:
#     result.append(num % 2)
#     num //= 2
# result = [str(x) for x in result[::-1]]
# print("".join(result))

# def near_zero(value, iterable):
#     min_val = abs(iterable[-1] - value)
#     near = iterable[-1]
#     for val in iterable:
#         if abs(val - value) < min_val:
#             min_val = abs(val - value)
#             near = val
#     print(near)


# near_zero(1, [1, 5])
# near_zero(2, [1, 5])
# near_zero(8, [1, 5])
# near_zero(9, [1, 5])
# near_zero(10, [1, 100])

import sys


def main():
    average = sys.stdin.readline().rstrip()
    average = int(average)
    line = sys.stdin.readline().rstrip()
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
    print(*street)


if __name__ == '__main__':
    main()
