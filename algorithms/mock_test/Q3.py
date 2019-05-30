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
