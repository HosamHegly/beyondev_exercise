def linear_search(arr, target):
    """Performs a linear search for a target value in a given list."""
    for index,value in enumerate(arr):
        if value == target:
            return index
    return -1  #if not found return -1


def binary_search(arr,target):
    """ binary search for target index in array"""
    left , right = 0, len(arr) - 1
    while left <= right:
        mid = (left+right)//2 #floor div to find mimd index
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1 # if not found


if __name__ == "__main__":
    arr = [5, 3, 8, 6, 1, 9, 2, 7]
    target = 6

    result_index = linear_search(arr, target)
    if result_index != -1:
        print(f"Value {target} found at index: {result_index}")
    else:
        print(f"Value {target} not found in the list.")

    result_index = binary_search(arr, target)
    if result_index != -1:
        print(f"Value {target} found at index: {result_index}")
    else:
        print(f"Value {target} not found in the list.")
