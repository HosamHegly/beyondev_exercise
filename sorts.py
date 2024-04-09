def bubble_sort(arr):

    for i in range(0, len(arr)):
        for j in range (0,len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1], arr[j]
    return  arr


def merge_sort(arr):
    """
    Sorts an array in ascending order using the Merge Sort algorithm.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()
        items_greater = []
        items_less = []
        for item in arr:
            if item < pivot:
                items_less.append(item)
            else:
                items_greater.append(item)

        return quick_sort(items_less) + [pivot] + quick_sort(items_greater)

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    sorted_arr = merge_sort(arr)
    print("Merge sorted array is:", sorted_arr)
    arr = [12, 11, 13, 5, 6, 7]
    sorted_arr = bubble_sort(arr)
    print("bubble sorted array is:", sorted_arr)

    arr = [12, 11, 13, 5, 6, 7]
    sorted_arr = quick_sort(arr)
    print("quick sorted array is:", sorted_arr)





