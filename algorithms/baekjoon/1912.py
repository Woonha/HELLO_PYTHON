num = int(input())
arr = list(map(int, input().split()))

temp = 0 # no need to be array
result = -1001
for i in range(num):
    temp = max(temp + arr[i], arr[i])
    result = max(result, temp)
print(result)