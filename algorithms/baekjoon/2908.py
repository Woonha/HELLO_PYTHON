def reverse(str):
    reversed = ""
    for i in range(len(str)-1, -1, -1):
        reversed += str[i]

    return reversed

def main():
    a, b = input().split()

    a = int(reverse(a))
    b = int(reverse(b))

    print(max(a, b))

if __name__ == "__main__":
    main()
