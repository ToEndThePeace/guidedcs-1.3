# returns the index of the target in the array OR
# returns -1 if target isn't in array
def binary_search(arr, target):
    # 1. compare target element to midpoint
    # how do we find midpoint?
    # the length of array can determine this
    # or the range: leftmost and rightmost indices
    # can be used to determine the element between them
    # midpoint is `((right_index + left_index) / 2)`
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = mp(low, high)
    # 2. determine which direction to go in
    # reassign left or right index to point to the element past
    # the midpoint we jsut checked
    # don't need to include the midpoint because we just checked it
    # 3. if midpoint element matches, return the index
        if target == arr[mid]:
            return mid
        if target < arr[mid]:
            high = mid - 1
        if target > arr[mid]:
            low = mid + 1
    # 4. repeat this process: we need to loop
    # until we find the target OR we've searched the whole array
    # if low and high are the same index and we have no target yet, return -1
    return -1


def mp(n1, n2):
    return (n1 + n2) // 2


# x = [1, 2, 3, 4, 5, 6, 7]
# print(binary_search(x, -2))
