class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        now = 0
        max_n = 0

        for n in nums:
            if n == 1:
                now += 1

                if now > max_n:
                    max_n = now
            else:
                now = 0

        return max_n