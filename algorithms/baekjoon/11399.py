# same code with ../greedy/ATM.py
def solution(P):
    minSum = 0
    P.sort()
    for i in range(len(P)):
        for j in range(len(P)-i):
            minSum += P[i]

    return minSum

if __name__ == "__main__":
    N = int(input())
    P = [int(i) for i in input().split()]

    print(solution(P))