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

def near_zero(value, iterable):
    min_val = abs(iterable[-1] - value)
    near = iterable[-1]
    for val in iterable:
        if abs(val - value) < min_val:
            min_val = abs(val - value)
            near = val
    print(near)


near_zero(1, [1, 5])
near_zero(2, [1, 5])
near_zero(8, [1, 5])
near_zero(9, [1, 5])
near_zero(10, [1, 100])
