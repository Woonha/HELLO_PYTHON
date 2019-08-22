n, x = map(int, input().split())
arr = list(map(int, input().split()))

for i in arr:
    if i < x:
        print(i, end=" ")


"""
10 5
1 10 4 9 2 3 8 5 7 6
"""