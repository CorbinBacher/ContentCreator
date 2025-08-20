def bubble_sort(values):
    """Sorts a list using bubble sort and returns a new sorted list"""
    arr = values[:]  # make a copy so we don’t modify the original
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    print("Please enter 10 values")
    notSortedList = []
    for i in range(10):
        value = int(input(f"Enter value {i+1}: "))
        notSortedList.append(value)

    print("\nUnsorted List:")
    print(notSortedList)

    sortedList = bubble_sort(notSortedList)

    print("\nSorted List:")
    print(sortedList)
