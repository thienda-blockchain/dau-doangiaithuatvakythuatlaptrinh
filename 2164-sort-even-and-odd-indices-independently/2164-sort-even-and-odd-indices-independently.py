class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums[0::2] = sorted(nums[0::2])
        nums[1::2] = sorted(nums[1::2], reverse = True) 
        return nums