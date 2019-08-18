num = int(input())
arr = []
for i in range(num):
    arr.append(list(map(int, input().split())))

for i in range(num):
    print("Case #%d: %d" % (i+1, arr[i][0] + arr[i][1]))