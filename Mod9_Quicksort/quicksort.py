from random import shuffle

def partition(arr, low, high):
    pivot_val = arr[low]
    left_index = low

    for i in range(low + 1, high):
        if arr[i] < pivot_val:
            left_index += 1
            tmp = arr[i]
            arr[i] = arr[left_index]
            arr[left_index] = tmp

    tmp = arr[low]
    arr[low] = arr[left_index]
    arr[left_index] = tmp

    return left_index

def quicksort(array, low, high):
    print(f'Array right now: {array}')
    shuffle
    if low < high:
        pivot_location = partition(array, low, high)
        print(f'Pivot Value: {array[pivot_location]} Pivot location: {pivot_location}')
        quicksort(array, low, pivot_location - 1)
        quicksort(array, pivot_location + 1, high)


def sort(array):
    shuffle(array)
    quicksort(array, 0, len(array))

array = [2, 3, 7, 9, 2, 4, 8, 5, 1, 6]

# quicksort(array, 0, len(array))
sort(array)

print(array)

# result = partition(array, 0, len(array))
#
# print(f'result: {result}')
# print(array)
#
# result = partition(array, 2, len(array))
#
# print(f'result: {result}')
# print(array)

print('\n\n=======\n\n')
array2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# quicksort(array2, 0, len(array2))
sort(array2)


print(array2)