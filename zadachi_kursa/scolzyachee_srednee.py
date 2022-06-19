time = int(input())
timeseries = list(map(float, input().split()))
K = int(input())
result = []
current_sum = sum(timeseries[0:K])
print(current_sum/K, end=" ")

for num in range(0, time - K):
    current_sum -= timeseries[num]
    current_sum += timeseries[num+K]
    print(current_sum/K, end=" ")
