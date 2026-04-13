class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_sap_xep = sorted(nums)
        
        ket_qua = []
        
        # Duyệt qua từng vị trí i trong mảng đã sắp xếp
        for i in range(len(nums_sap_xep)):
            # Nếu số tại vị trí i là số ta đang tìm (target)
            if nums_sap_xep[i] == target:
                ket_qua.append(i)
                
        return ket_qua