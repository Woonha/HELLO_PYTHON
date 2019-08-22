num = int(input())

for i in range(num):
    print("%s%s" % (" "*(num-i-1), "*"*(i+1)))