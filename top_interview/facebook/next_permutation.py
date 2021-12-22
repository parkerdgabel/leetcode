from typing import List


def swap(nums: List[int], i: int, j: int) -> None:
    nums[j], nums[i] = nums[i], nums[j]


def reverse(nums: List[int], start: int) -> None:
    i, j = start, len(nums) - 1
    while i < j:
        swap(nums, i, j)
        i, j = i + 1, j - 1


def first_decreasing_index(nums: List[int]) -> int:
    i = len(nums) - 2
    while i >= 0 and nums[i + 1] <= nums[i]:
        i = i - 1
    return i


def swap_just_larger_element(nums: List[int], i: int) -> None:
    j = len(nums) - 1
    while nums[j] <= nums[i]:
        j = j - 1
    swap(nums, i, j)


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = first_decreasing_index(nums)
        if i >= 0:
            swap_just_larger_element(nums, i)
        reverse(nums, i + 1)
