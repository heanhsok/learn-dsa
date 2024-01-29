from typing import List

def move_zeros(nums: List[int]) -> None:
    """
    always keep the slow point at index with zero value
    """
    slow, fast = 0, 0
    while fast < len(nums):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
        fast += 1

nums = [1, 0, 0, 0, 2, 0, 0, 7]
move_zeros(nums)
print(nums)