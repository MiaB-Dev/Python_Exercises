def selection_sort(array):
    for iter_i in range(0, len(array)-1):
        current_min = iter_i
        for iter_j in range(iter_i + 1, len(array)):
            if array[iter_j] < array[current_min]:
                current_min = iter_j
        array[iter_i], array[current_min] = array[current_min], array[iter_i]
    return array

if __name__ == '__main__':
    a = [2, 8, 5, 3, 9, 4, 1]
    b = selection_sort(a)
    print(b)