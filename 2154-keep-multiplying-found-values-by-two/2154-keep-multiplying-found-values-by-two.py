class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        tap_hop_so = set(nums)
        while original in tap_hop_so:
            # Nhân đôi giá trị lên
            original *= 2
        return original