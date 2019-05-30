"""
[문제 설명]
직사각형을 만드는 데 필요한 4개의 점 중 3개의 좌표가 주어질 때, 나머지 한 점의 좌표를 구하려고 합니다.
점 3개의 좌표가 들어있는 배열 v가 매개변수로 주어질 때,
직사각형을 만드는 데 필요한 나머지 한 점의 좌표를 return 하도록 solution 함수를 완성해주세요.
단, 직사각형의 각 변은 x축, y축에 평행하며, 반드시 직사각형을 만들 수 있는 경우만 입력으로 주어집니다.
[제한 사항]
v는 2차원 배열
[입출력 예]
1 4
3 4
3 10
-> 1 10
1 1
2 2
1 2
-> 2 1
"""
def solution(v):
    answer = []

    if v[0][0] == v[1][0]:
        answer.append(v[2][0])
    elif v[1][0] == v[2][0]:
        answer.append(v[0][0])
    else:
        answer.append(v[1][0])

    if v[0][1] == v[1][1]:
        answer.append(v[2][1])
    elif v[1][1] == v[2][1]:
        answer.append(v[0][1])
    else:
        answer.append(v[1][1])

    return answer

if __name__ == "__main__":
    v = []
    for i in range(3):
        v.append([int(j) for j in input().split()])
    
    print(solution(v))

