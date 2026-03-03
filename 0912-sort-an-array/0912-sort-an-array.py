class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums

        giua = len(nums) // 2
        ben_trai = self.sortArray(nums[:giua])
        ben_phai = self.sortArray(nums[giua:])
        
        return self.merge(ben_trai, ben_phai)

    def merge(self, trai, phai):
        ket_qua = []
        i = j = 0
        
        while i < len(trai) and j < len(phai):
            if trai[i] < phai[j]:
                ket_qua.append(trai[i])
                i += 1
            else:
                ket_qua.append(phai[j])
                j += 1
        
        ket_qua.extend(trai[i:])
        ket_qua.extend(phai[j:])
        return ket_qua