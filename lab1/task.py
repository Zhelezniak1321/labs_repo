def is_monotonic(arr):
    increasing = True
    decreasing = True
    
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            increasing = False
        if arr[i] < arr[i + 1]:
            decreasing = False
    
    if increasing or decreasing:
        return True
    else:
        return False

if __name__ == "__main__":
    test_arrays = [
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [1, 2, 2, 3, 2, 4],
        [3, 3, 3, 3],
        [10],
        []
    ]
    
    for arr in test_arrays:
        print(f"Масив: {arr}  {is_monotonic(arr)}")