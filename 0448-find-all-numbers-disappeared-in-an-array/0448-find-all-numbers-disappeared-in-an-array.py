class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        check = set(nums)
        n = len(nums)
        ket_qua = []

        for i in range (1, n + 1 ):
            if i not in check:
                ket_qua.append(i)
        return ket_qua

