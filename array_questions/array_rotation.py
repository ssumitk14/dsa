# Find the number of rotations in a circularly sorted array
# Input:  nums = [8, 9, 10, 2, 5, 6]
# Output: The array is rotated 3 times

# [10, 2, 5, 6, 8, 9]
# Since, its a sorted array, we can just find the index of the lowest element using a Linear Search
# But this will have time complexity of O(n)

# Instead we can use, binary search to solve this problem which has better time complexity O(log2(n))

def find_num_of_rotation(arr):
    first = 0
    last = len(arr) - 1

    while last >= first:
        mid = (first + last)//2
        if arr[first] < arr[last]:
            # This is best case scenario when array is already sorted
            return 0
        if arr[mid-1] > arr[mid] < arr[mid+1]:
            # We make use of the fact that if next element and previous element both are greater than the mid
            # element then, we've found the lowest element
            return mid
        if arr[mid] < arr[last]:
            # If the last element is greater than the mid element this means that the right half is already sorted.
            # The lowest element must be on the left half side.
            last = mid
        else:

            first = mid


if __name__ == "__main__":
    # nums = [8, 9, 10, 2, 5, 6]
    # nums = [10, 2, 5, 6, 8, 9]
    nums = [2, 5, 6, 8, 9, 10]

    index = find_num_of_rotation(nums)
    if index:
        print(f"Array is rotated {index} times")
    else:
        print(f"Array is NOT rotated")
