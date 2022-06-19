tokens = int(input())
token_value = list(map(int, input().split()))
hidenn_num = int(input())


def twosum_extra(numbers, X):
    previous = set()

    for A in numbers:
        Y = X - A
        if Y in previous:
            return print(A, Y, end=" ")
        else:
            previous.add(A)
    return print(None)


twosum_extra(token_value, hidenn_num)
