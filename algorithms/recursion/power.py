def power(x, n):
    print("Computing ", x, " raised to power ", n, ".")
    if n == 0: # 지수가 0일 경우
        return 1
    elif n > 0: # 지수가 양수일 경우
        if n % 2 == 0: # 지수가 짝수일 경우
            return power(x, n/2) * power(x, n/2)
        else: # 지수가 홀수일 경우
            return x * power(x, n-1)
    else: # 지수가 음수일 경우
        return 1 / power(x, -n)

if __name__ == "__main__":
    print(power(2, 3))
