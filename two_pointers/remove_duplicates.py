from typing import List
def remove_duplicates(arr: List[int]) -> int:
    """
    when fast is not the same as slow, 
    increment slow by 1 and swap the value
    then increment fast by one
    """
    slow, fast = 0, 0
    while fast < len(arr):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
        fast += 1
        
    return slow + 1

remove_duplicates([1,1,2,2,3,3])