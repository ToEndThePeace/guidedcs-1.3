# partition function handles the work of selecting a pivot
# element and partitioning the data in the array around it
# returns left partition, pivot, and right partition
def partition(arr):
    pivot = arr[0]
    left = []
    right = []
    for i in arr[1:]:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)
    return left, pivot, right


def quicksort(arr):
    # base case?
    #   arr length is 1?
    if len(arr) <= 1:
        return arr
    # how do we move closer?
    #   splitting the array further and further down
    left, pivot, right = partition(arr)
    return quicksort(left) + [pivot] + quicksort(right)

x = [3, 5, 7, 1, 3, 1, 8 ,4]
x = quicksort(x)
print(x)