def bubble_sort(arr):
    """
    Sorts a list using the Bubble Sort algorithm.

    :param arr: The list to be sorted.
    :type arr: list of comparable elements
    :return: Sorted list.
    :rtype: list of comparable elements
    """
    n = len(arr)

    # Traverse through all elements in the list
    for i in range(n):
        # Flag to optimize the algorithm by detecting if any swaps were made
        swapped = False

        # Last i elements are already in place, so we don't need to check them
        for j in range(0, n - i - 1):
            # If the current element is greater than the next element, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap the elements
                swapped = True  # Set the flag to True to indicate a swap occurred

        # If no two elements were swapped in the inner loop, the array is already sorted
        if not swapped:
            break

    return arr

# Example usage
if __name__ == "__main__":
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    sorted_list = bubble_sort(unsorted_list)
    print("Sorted list:", sorted_list)
