class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sap_xep = sorted(nums)
        tra_cuu = {}

        for i in range(len(sap_xep)):
            so = sap_xep[i]

            if so not in tra_cuu:
                tra_cuu[so] = i

        ket_qua = []
        for so in nums:
            ket_qua.append(tra_cuu[so])

        return ket_qua