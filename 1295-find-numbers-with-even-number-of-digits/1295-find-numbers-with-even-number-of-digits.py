class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dem = 0 
        for i in nums:
            chuoi_so = str(i)
            do_dai = len(chuoi_so)
            
            # Kiểm tra độ dài có phải số chẵn không
            if do_dai % 2 == 0:
                dem += 1
        return dem