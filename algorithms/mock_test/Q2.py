"""
[문제 설명]
길이가 n인 배열에 1부터 n까지 숫자가 중복 없이 한 번씩 들어 있는지를 확인하려고 합니다.
1부터 n까지 숫자가 중복 없이 한 번씩 들어 있는 경우 true를, 아닌 경우 false를 반환하도록 함수 solution을 완성해주세요.

[입출력 예]
4 1 3 2 -> true
4 1 3 -> false
"""
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
