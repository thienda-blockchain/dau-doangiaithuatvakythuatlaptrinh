class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Cuốn sổ tay để đếm số lần xuất hiện của từng con số
        dem_so = {}
        
        # BƯỚC 1: Duyệt qua mảng và đếm (Áp dụng đúng đoạn code bạn vừa chọn!)
        for num in nums:
            dem_so[num] = dem_so.get(num, 0) + 1
            
        # BƯỚC 2: Kiểm tra số lần xuất hiện của tất cả các số trong sổ tay
        # dem_so.values() sẽ lấy ra danh sách các số lần xuất hiện (ví dụ: [2, 4, 2])
        for so_lan in dem_so.values():
            
            # Nếu có bất kỳ số nào xuất hiện lẻ lần (chia 2 dư khác 0)
            if so_lan % 2 != 0:
                return False # Thất bại, không thể chia cặp hoàn hảo
                
        # Nếu đi qua hết sổ tay mà toàn là số chẵn
        return True # Thành công!