class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Bước 1: Khởi tạo hai con trỏ y hệt như các bài Binary Search trước
        trai = 0
        phai = len(nums) - 1
        
        # Bê nguyên xi vòng lặp bạn đã bôi đen vào đây!
        while trai <= phai:
            giua = (trai + phai) // 2
            
            # Lấy số ở giữa ra so sánh
            so_giua = nums[giua]
            
            if so_giua == target:
                # Nếu may mắn tìm thấy luôn, thì vị trí đó chính là đáp án
                return giua
                
            elif so_giua < target:
                # Nếu số ở giữa còn nhỏ hơn mục tiêu, nghĩa là mục tiêu nằm ở nửa bên phải
                trai = giua + 1
                
            else: # so_giua > target
                # Nếu số ở giữa lớn hơn mục tiêu, nghĩa là mục tiêu nằm ở nửa bên trái
                phai = giua - 1
                
        # SỰ KHÁC BIỆT DUY NHẤT NẰM Ở ĐÂY:
        # Nếu vòng lặp kết thúc mà chưa tìm thấy (trai > phai),
        # thì con trỏ 'trai' (left) sẽ luôn dừng lại đúng ở vị trí cần chèn!
        return trai