N = int(input())
ctor = 0 # constructor
sum = 0
while sum != N:
    ctor += 1
    sum = ctor
    for i in range(len(str(ctor))):
        sum += int(str(ctor)[i])
    if ctor > N: # if there is no constructor
        ctor = 0
        break

print(ctor)
