class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Bước 1: Sắp xếp lại các thẻ bài từ bé đến lớn
        nums.sort()
        ket_qua = []
        
        # Bước 2: Cho Đội trưởng (i) đi từ đầu đến gần cuối hàng
        for i in range(len(nums) - 2):
            
            # Anti-Clone: Đội trưởng không chọn lại thẻ giống hệt thẻ trước đó
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Bước 3: Đặt vị trí cho 2 người phụ việc
            trai = i + 1
            phai = len(nums) - 1
            
            # Chừng nào hai người phụ việc chưa chạm mặt nhau
            while trai < phai:
                tong = nums[i] + nums[trai] + nums[phai]
                
                if tong == 0:
                    # Tìm thấy bộ ba hoàn hảo, ghi vào sổ!
                    ket_qua.append([nums[i], nums[trai], nums[phai]])
                    
                    # Hai người cùng dịch chuyển vào trong để tìm thêm
                    trai += 1
                    phai -= 1
                    
                    # Anti-Clone: Phụ việc lờ đi những thẻ bài bị trùng
                    while trai < phai and nums[trai] == nums[trai - 1]:
                        trai += 1
                    while trai < phai and nums[phai] == nums[phai + 1]:
                        phai -= 1
                        
                elif tong < 0:
                    # Thiếu điểm, Người Trái bước lên để lấy thẻ to hơn
                    trai += 1
                else:
                    # Dư điểm, Người Phải lùi lại để lấy thẻ nhỏ hơn
                    phai -= 1
                    
        return ket_qua