### Method 1
def isPermutation1(str1, str2):
    if len(str1) == len(str2):
        str1_ascii = []
        str2_ascii = []

        for c in str1:
            str1_ascii.append(ord(c))
        for c in str2:
            str2_ascii.append(ord(c))

        str1_ascii.sort()
        str2_ascii.sort()

        if (str1_ascii == str2_ascii):
            return True
        else:
            return False
    else:
        return False

### Method 2
def isPermutation2(str1, str2):
    if len(str1) == len(str2):
        str1_dict = {}
        str2_dict = {}
        for i in range(len(str1)):
            if str1[i] not in str1_dict:
                str1_dict[str1[i]] = 1
            else:
                str1_dict[str1[i]] += 1

            if str2[i] not in str2_dict:
                str2_dict[str2[i]] = 1
            else:
                str2_dict[str2[i]] += 1
        if str1_dict == str2_dict:
            return True
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    str1 = "abcab"
    str2 = "cbaba"
    print(isPermutation1(str1, str2))
    print(isPermutation2(str1, str2))