def solution(arr):
    arr.sort()
    if arr[-1] == len(arr):
        if len(set(arr)) == len(arr):
            answer = True
        else:
            answer = False
    else:
        answer = False
    return answer

if __name__== "__main__":
    arr = input().split()
    numbers = [int(i) for i in arr]
    print(solution(numbers))
