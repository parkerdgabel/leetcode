# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

def isBadVersion(mid):
    pass

class Solution:
    def firstBadVersion(self, n: int):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l < r:
            mid = l + (r - l) // 2
            if (isBadVersion(mid)):
                r = mid
            else:
                l = mid + 1
        return l
