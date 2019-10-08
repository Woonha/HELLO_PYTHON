arr = []

while len(arr) != 9:
    num = int(input())
    if num < 100:
        arr.append(num)
sortedArr = arr.copy()
sortedArr.sort()
print(sortedArr[-1])
print(arr.index(sortedArr[-1])+1)
"""
[input]
3
29
38
12
57
74
40
85
61
"""

'''
나중에 확인하기
arr = []

while len(arr) != 9:
    num = int(input())
    if num < 100:
        arr.append(num)

maxNum = arr[0]
maxIndex = 0

for i in range(len(arr)):
    if maxNum < arr[i]:
        maxNum = arr[i]
        maxIndex = i+1

print(maxNum)
print(maxIndex)
'''