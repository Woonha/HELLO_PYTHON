"""
# 완전 탐색 (시간 초과)
num = int(input())
arr = list(map(int, input().split()))

contSum = arr[0]  # contiguous sum
for i in range(num):
    for j in range(i+1, num):
        temp = sum(arr[i:j])
        if contSum < temp:
            contSum = temp
print(contSum)
"""
"""
# DP ? (메모리 초과)
num = int(input())
arr = list(map(int, input().split()))

# dp = [[0] * num] * num # 이렇게 하면 메모리가 공유됨 ...
dp = [[-999 for col in range(num)] for row in range(num)]

for i in range(num):
    dp[i][i] = arr[i]
    for j in range(i+1, num):
        if (dp[i][j-1] == -999):
            dp[i][j] = arr[j]
        dp[i][j] = dp[i][j-1] + arr[j]

print(max(map(max, dp)))
'''
dp[0][0] = arr[0]
dp[0][1] = dp[0][0] + arr[1]
dp[0][2] = dp[0][1] + arr[2]
...
dp[0][4] = dp[0][3] + arr[4]

dp[1][0] = 0
dp[1][1] = arr[1]
dp[1][2] = dp[1][0] + arr[2]
...
dp[1][4] = dp[1][3] + arr[4]
...
dp[2][0] = 0
dp[2][1] = 0
dp[2][2] = dp[2][1] + arr[2]
###dp[4][0] = 0
...
dp[4][4] = arr[4]
'''
"""

"""
# DP ? 시간 초과
num = int(input())
arr = list(map(int, input().split()))

# dp = [[0] * num] * num # 이렇게 하면 메모리가 공유됨 ...
dp = [-999 for row in range(num)] # 각 시작 index를 기준으로 더한 것들잉용
result = -999
for i in range(num):
    dp[i] = arr[i]
    for j in range(i+1, num):
        if (dp[j-1] == -999):
            dp[j] = arr[j]
        dp[j] = dp[j-1] + arr[j]
        dp[i] = max(dp)
    result = max(result, dp[i])

print(result)
"""
"""
# DP ? 시간초과
num = int(input())
arr = list(map(int, input().split()))

dp = [-999 for row in range(num)] # 각 시작 index를 기준으로 더한 것들잉용
result = -999
for i in range(num):
    dp[i] = arr[i]
    for j in range(i+1, num):
        if (dp[j] == -999):
            dp[j] = arr[j]
        dp[j] = dp[j-1] + arr[j]
    result = max(result, max(dp))
print(result)
"""
# DP ? 이쯤되면 for문 두개 쓰는건 노답임... 답을 보자 흑흑쓰
# 내가 놓친 부분: 나는 각 인덱스까지 더한 값들을 다 저장함. 근데 그럴 필요 X --> 그냥 이전과 더한 값과 현재 중 큰 값을 저장
num = int(input())
arr = list(map(int, input().split()))

dp = [0 for _ in range(num)]
result = -1001 # -999로 하면 틀림.. 왜냐하면 문제에서 수는 -1000<=n<=1000 라고 했기 때문쓰
for i in range(num):
    dp[i] = max(dp[i-1] + arr[i], arr[i])
    result = max(result, dp[i])
print(result)

"""
10
10 -4 3 1 5 6 -35 12 21 -1
-> 33
10
2 1 -4 3 4 -4 6 5 -5 1
-> 14
5
-1 -2 -3 -4 -5
-> -1
"""
