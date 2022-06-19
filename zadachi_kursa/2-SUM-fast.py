tokens = int(input())
token_value = list(map(int, input().split()))
hidenn_num = int(input())


def twosum_fast(numbers, X):
    left = 0
    right = len(numbers)-1
    numbers.sort()

    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == X:
            return print(numbers[left], numbers[right], end=" ")
        if current_sum < X:
            left += 1
        else:
            right -= 1
    return print(None)


twosum_fast(token_value, hidenn_num)
