class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
         # BƯỚC 1: Lập "Sổ tay" cho Nhóm 1 (nums1 và nums2)
        # Sổ tay này lưu [Tổng của 2 số : Số lần xuất hiện của tổng đó]
        dem_tong = {}
        for a in nums1:
            for b in nums2:
                tong = a + b
                dem_tong[tong] = dem_tong.get(tong, 0) + 1
                
        count = 0
        
        # BƯỚC 2: Duyệt qua Nhóm 2 (nums3 và nums4) và đối chiếu với Sổ tay
        for c in nums3:
            for d in nums4:
                # Nếu (a + b) + (c + d) = 0
                # Thì (a + b) phải bằng -(c + d)
                muc_tieu = -(c + d)
                
                # Kiểm tra xem con số mục tiêu này có nằm trong sổ tay của Nhóm 1 không?
                if muc_tieu in dem_tong:
                    # Nếu có, cộng thêm số lần xuất hiện của tổng đó vào kết quả
                    count += dem_tong[muc_tieu]
                    
        return count