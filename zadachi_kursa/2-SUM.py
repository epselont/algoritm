tokens = int(input())
token_value = list(map(int, input().split()))
hidenn_num = int(input())


def twosum(numbers, X):
    for i in range(0, len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == X:
                return print(numbers[i], numbers[j], end=" ")
    return print(None)


twosum(token_value, hidenn_num)
