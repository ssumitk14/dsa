def binary_search_1(arr, x):
    """

    :param arr: List of elements sorted in ascending order
    :param x: Element that you want to search
    :return: Index of element found
    """
    low = 0
    high = len(arr) - 1
    while high >= low:
        mid = (low + high)//2
        # print(mid)
        if arr[mid] == x:
            return mid
        if x > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == "__main__":
    lst = [2, 3, 4, 10, 40, 50, 60, 70, 80]
    look_for = 40
    index = binary_search_1(lst, look_for)

    if index == -1:
        print("Element not present in the list")
    else:
        print("Element present at index: ", index)
