from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared = list(map(lambda x: x * x, nums))
        squared.sort()
        return squared
