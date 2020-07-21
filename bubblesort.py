
def bubble_sort(arr):
    swap_count = 1
    while swap_count != 0:
        swap_count = 0
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap_count += 1
    # for i in range(len(arr)):
    #     for j in range(len(arr) - i - 1):
    #         if arr[j] > arr[j + 1]:
    #             arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# recursive version


def bubble_sort_rec(arr, unsorted_length):
    for i in range(unsorted_length - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    if unsorted_length > 0:
        bubble_sort_rec(arr, unsorted_length - 1)

def bubble_sort_rec2(arr): # not working but i'm determined
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    if len(arr) > 0:
        bubble_sort_rec2(arr[:-1])


x = [5, 1, 1, 6, 0, 2, 7]
y = [5, 1, 7, 6, 2, 1, 0]
z = [5, 1, 7, 6, 2, 1, 0]

bubble_sort(x)
print(x)
bubble_sort_rec(y, len(y))
print(y)
bubble_sort_rec2(z)
print(z)
