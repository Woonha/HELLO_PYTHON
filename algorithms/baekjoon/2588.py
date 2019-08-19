num1 = int(input())
num2 = input()
mult = []
result = 0

for i in range(2, -1, -1):
    mult.append(num1 * int(num2[i]))
    print(mult[-1])

for i in range(3):
    result += mult[0]*10**i
    del(mult[0])
print(result)