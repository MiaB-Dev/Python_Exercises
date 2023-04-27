def bubble_sort(array):
    for i in range(0, len(array) - 1):
        for j in range(0, len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


if __name__ == '__main__':
    a = [2, 8, 5, 3, 9, 4, 1]
    b = bubble_sort(a)
    print(b)