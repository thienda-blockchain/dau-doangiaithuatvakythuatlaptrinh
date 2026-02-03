class Solution(object):
    def containsDuplicate(self, nums):
        so_ghi_nho = set()

        for so in nums:
            if so in so_ghi_nho:
                return True

            so_ghi_nho.add(so)

        return False