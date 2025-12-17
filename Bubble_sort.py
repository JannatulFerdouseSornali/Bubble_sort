def bubbleSort(arr):
    n = len(arr)
    
    # Outer loop: repeat n times
    for i in range(n):
        # Inner loop: compare adjacent elements
        for j in range(n - 1 - i):
            # If left element is bigger, swap
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr


# Test
print(bubbleSort([64, 34, 25, 12, 22, 11, 90]))
# Output: [11, 12, 22, 25, 34, 64, 90]

