def QuickSort(arr):
    elements = len(arr)

    # Base case
    if elements < 2:
        return arr

    current_position = 0  # Position of the partitioning element

    for i in range(1, elements):  # Partitioning loop
        if arr[i] <= arr[0]:
            print("arr[i]: ", arr[i])
            current_position += 1
            print("current pos:", current_position)
            temp = arr[i]
            print("temp jtz arr[i]: ", temp)
            arr[i] = arr[current_position]
            print("arr[i] an stelle i jtz wert current pos: ", arr[i])
            arr[current_position] = temp
            print("array an stelle current pos jtz temp: ", arr[current_position], "\n")

    temp = arr[0]
    arr[0] = arr[current_position]
    arr[current_position] = temp  # Brings pivot to it's appropriate position

    left = QuickSort(arr[0:current_position])  # Sorts the elements to the left of pivot
    right = QuickSort(arr[current_position + 1:elements])  # sorts the elements to the right of pivot

    arr = left + [arr[current_position]] + right  # Merging everything together

    return arr


array_to_be_sorted = [35, 28, 41, 7, 14, 50, 33, 21, 21, 60, 18, 12]
print("Original Array: ", array_to_be_sorted)
print("Sorted Array: ", QuickSort(array_to_be_sorted))