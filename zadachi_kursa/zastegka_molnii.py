len_list = int(input())
first_list = list(map(int, input().split()))
second_list = list(map(int, input().split()))

for num in range(0, len_list):
    print(first_list[num], end=" ")
    print(second_list[num], end=" ")
