# 일곱 난쟁이
"""
20
7
23
19
10
15
25
8
13
"""
heights = []
while len(heights) != 9:
    height = int(input())
    if height >= 100:
        continue
    heights.append(height)
    tuple(heights)
heights.sort()

total = sum(heights)
result = heights.copy()
for i in range(8):
    for j in range(i+1, 9):
        if total-(result[i]+result[j]) == 100:
            result.remove(result[i])
            result.remove(result[j-1])

            print(*result, sep='\n')

        result = heights.copy()
    else:
        continue
    break




