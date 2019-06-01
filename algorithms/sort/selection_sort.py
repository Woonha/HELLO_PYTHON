def selection_sort(array):
    for i in range(len(array)):
        min = 9999
        for j in range(i, len(array)):
            if min > array[j]:
                min = array[j]
                index = j
        temp = array[i]
        array[i] = array[index]
        array[index] = temp
    return array


if __name__ == "__main__":
    array = [2, 3, 4, 1, 5, 9, 10, 7, 6, 8]
    print(array)
    print(selection_sort(array))
