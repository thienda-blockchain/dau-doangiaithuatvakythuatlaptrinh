class Solution(object):
    def smallestEqual(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                # Vì ta duyệt từ i=0 tăng dần, nên số đầu tiên 
                # thỏa mãn chính là số nhỏ nhất.
                return i
        

        return -1