from typing import List
import heapq


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        minHeap = []
        lists = nums1  + nums2
        for i in range(len(lists)):
            heapq.heappush(minHeap, lists[i])

        for i in range(0, len(minHeap)//2):
            result = heapq.heappop(minHeap)


        if len(lists) % 2 != 0:
            result = heapq.heappop(minHeap)

        if len(lists) % 2 == 0:
            result += heapq.heappop(minHeap)
            result /= 2

        return result
