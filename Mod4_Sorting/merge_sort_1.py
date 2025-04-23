

def merge(data, low, mid, high):
    left = data[low:mid + 1] ## sublist starting at the low, and including everything less than high
    right = data[mid + 1: high + 1]

    print(right)
    i, j = 0, 0
    for k in range(low, high + 1):
        print(f'Looking at {k} loop')
        if left[i] < right[j]:
            data[k] = left[i]
            i += 1
        else:
            data[k] = right[j]
            j += 1

        if i >= len(left):
            ### Done with the left
            ## Copy everything from the right into the source
            k += 1
            for n in range(j, len(right)):
                data[k] = right[n]
                k += 1
            return

        if j >= len(right):
            ## Copy everything from left into the source
            k += 1
            for n in range(i, len(left)):
                data[k] = left[n]
                k += 1
            return


    pass


def mergesort(data, low, high):
    if low < high:
        mid = (low + high) // 2
        mergesort(data, low, mid)
        mergesort(data, mid + 1, high)
        merge(data, low, mid, high)


