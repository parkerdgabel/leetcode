from functools import partial
from typing import List


def rotate_by_k(nums: List[int], i: int, k: int = 1) -> int:
    return nums[(i + k) % len(nums)]


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rot = partial(rotate_by_k, k=k)
        temp = []
        for i in range(len(nums)):
            temp.append(rot(nums, i))
        for i in range(len(temp)):
            nums[i] = temp[i]
