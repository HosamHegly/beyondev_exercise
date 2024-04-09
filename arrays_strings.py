def reverse_string(str):
    return str[::-1]


def min_max_array(array):
    """retrun min and max values in array"""
    if len(array) > 0:
        max = array[0]
        min = array[0]
        if len(array) == 1:
            return min
        else:
            for num in array:
                if num > max:
                    max = num
                elif num < min:
                    min = num
        return min, max
    return


def remove_duplicates_from_sorted_array(array: list):
    """checks adjacent values in array if they are equal don't return the first value"""

    return [array[index] for index in range(len(array)) if index == len(array) - 1 or array[index] != array[index + 1]]


if __name__ == "__main__":
    print(reverse_string("hello world"))
    first_array = [1, 3, 4, 5, 2, 1, 0, 10]
    second_array = [100, 2, -10, 0, 1]
    print(min_max_array(first_array))
    print(min_max_array(second_array))
    print(remove_duplicates_from_sorted_array([1, 2, 2, 3, 3, 5, 7, 10]))
    print(remove_duplicates_from_sorted_array([-100, -100, 0, 0, 10, 15, 70, 100, 100]))
