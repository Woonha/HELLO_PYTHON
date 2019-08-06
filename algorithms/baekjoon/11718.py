"""
import sys

for i in sys.stdin:

    print(i, end="")
"""
while 1:
    try:
        print(input())
    except EOFError:
        break

"""
# runtime error
for i in range(100):
    if print(input()) == '\n':
        break
"""
