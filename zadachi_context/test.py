# x = 4

# for i in range(1, 6):
#     print(f"{x} в степени {i}: {x ** i}")

# x = 2

# for i in range(2, 1000, 2):
#     print(f"{x} в степени {i}: {x ** i}")

# x = 4
# for i in range(2, 10, 2):
#     print(x * i, i)
x = 4
num = 10
result = []
while num != 0:
    result.append(num % 2)
    num //= 2
result = [str(x) for x in result[::-1]]
print("".join(result))
