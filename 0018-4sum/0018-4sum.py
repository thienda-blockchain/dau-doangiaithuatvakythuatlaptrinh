class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # Bước 1: Luôn luôn phải sắp xếp mảng trước khi dùng Hai con trỏ
        nums.sort()
        ket_qua = []
        n = len(nums)
        
        # Bước 2: Chọn Đội trưởng (Người thứ 1)
        for i in range(n - 3):
            # Chống trùng lặp cho Đội trưởng (Anti-clone)
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Bước 3: Chọn Phó tướng (Người thứ 2)
            # Phó tướng luôn xuất phát từ ngay sau lưng Đội trưởng
            for j in range(i + 1, n - 2):
                # Chống trùng lặp cho Phó tướng
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                    
                # Bước 4: Gọi 2 Người phụ việc đứng ở 2 đầu của phần mảng còn lại
                trai = j + 1
                phai = n - 1
                
                # Áp dụng chiến thuật Hai con trỏ y hệt như bài 3Sum!
                while trai < phai:
                    tong = nums[i] + nums[j] + nums[trai] + nums[phai]
                    
                    if tong == target:
                        # Tìm thấy bộ 4 hoàn hảo, lưu vào sổ!
                        ket_qua.append([nums[i], nums[j], nums[trai], nums[phai]])
                        
                        # Cả 2 phụ việc cùng dịch chuyển để tìm bộ mới
                        trai += 1
                        phai -= 1
                        
                        # Chống trùng lặp cho 2 người phụ việc
                        while trai < phai and nums[trai] == nums[trai - 1]:
                            trai += 1
                        while trai < phai and nums[phai] == nums[phai + 1]:
                            phai -= 1
                            
                    elif tong < target:
                        # Thiếu điểm -> Phụ việc trái bước lên để lấy số lớn hơn
                        trai += 1
                    else:
                        # Dư điểm -> Phụ việc phải lùi lại để lấy số nhỏ hơn
                        phai -= 1
                        
        return ket_qua