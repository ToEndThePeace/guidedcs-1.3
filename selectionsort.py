from binarysearch import binary_search


def selection_sort(arr):
    # iterate through the array to find the smallest element in the
    # unsorted portion of the array
    # swap the smallest element with the front of the unsorted buffer
    for i in range(len(arr)):
        # in this loop, i is the index of the boundary

        # find the smallest element to the RIGHT of the boundary
        mindex = i
        for j in range(i, len(arr)):
            if arr[j] < arr[mindex]:
                mindex = j

        # then swap
        arr[i], arr[mindex] = arr[mindex], arr[i]

    return arr


x = [3, 76, 34, 52, 19, 305, 0, 0, 0, 34, -3, 1, 42, 0]
print(x)

selection_sort(x)
print(x)

print(binary_search(x, 0))
