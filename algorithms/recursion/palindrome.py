def isPalindrome(str):
    if len(str) != 0:
        return False
    elif len(str) == 1:
        return True
    else:
        if str[0] == str[-1]:
            return isPalindrome(str[1:len(str)-1])
        else:
            return False


if __name__ == "__main__":
    print(isPalindrome("rotor"))