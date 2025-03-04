from typing import List, Tuple

def find_unsorted_subarray(arr: List[int]) -> Tuple[int, int]:
    n = len(arr)
    left, right = 0, n - 1
    
    while left < n - 1 and arr[left] <= arr[left + 1]:
        left += 1
    
    if left == n - 1:
        return -1, -1
    
    while right > 0 and arr[right] >= arr[right - 1]:
        right -= 1
    
    min_val = min(arr[left:right+1])
    max_val = max(arr[left:right+1])
    
    while left > 0 and arr[left - 1] > min_val:
        print(left)
        left -= 1
    
    while right < n - 1 and arr[right + 1] < max_val:
        print(right)
        right += 1
    
    return left, right