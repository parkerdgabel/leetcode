from typing import List, Optional

def get_decreasing_sequence(height: List[int], start: int) -> Optional[int]:
    j, last_index = start + 1, len(height) - 1
    while j <= last_index and height[j] < height[start]:
        j = j + 1



def get_trough(height: List[int], start: int) -> Optional[(int, int)]:
    pass

class Solution:
    def trap(self, height: List[int]) -> int:
        pass