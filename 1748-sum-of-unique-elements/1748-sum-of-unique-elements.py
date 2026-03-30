class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dem = {}
        for i in nums:
            dem[i] = dem.get(i, 0) + 1

        tong = 0 
        for i in dem:
            if dem[i] == 1:
                tong += i

        return tong 