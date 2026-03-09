class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tong = sum(nums)
        tong_trai = 0
        for i in range (len(nums)):
            x = nums[i]

            tong_phai = tong - tong_trai - x 

            if tong_phai == tong_trai:
                return i

            tong_trai += x 

        return -1 