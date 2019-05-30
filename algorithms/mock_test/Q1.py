def solution(N):
    answer = 0
    for i in str(N):
        print(i)
        answer += int(i)
    return answer

if __name__ == "__main__":
    N = int(input())
    print(solution(N))
