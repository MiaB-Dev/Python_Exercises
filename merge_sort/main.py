def mergesort(array):
    if len(array) > 1:
        left = array[:len(array) // 2]
        right = array[len(array) // 2:]
        mergesort(left)
        mergesort(right)

        merge(left, right, array)


def merge(left, right, array):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(left):
        array[k] = right[j]
        j += 1
        k += 1


if __name__ == '__main__':
    a = [3, 7, 8, 5, 4, 2, 6, 1]
    mergesort(a)
    print(a)