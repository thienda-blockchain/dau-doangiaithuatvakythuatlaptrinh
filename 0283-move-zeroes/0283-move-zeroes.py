class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Đứng chờ ở vị trí đầu tiên để hoán đổi với số khác 0
        cham = 0
        
        # Con trỏ "Nhanh" (Người Dò Đường)
        # Quét qua toàn bộ mảng
        for nhanh in range(len(nums)):
            
            # Nếu tìm thấy một số KHÁC 0 (số hợp lệ cần giữ lại)
            if nums[nhanh] != 0:
                
                # Cú pháp hoán đổi thần thánh của Python!
                # Đổi chỗ số khác 0 này cho con số mà Người Ghi Chép đang đứng (thường là số 0)
                nums[cham], nums[nhanh] = nums[nhanh], nums[cham]
                
                # Sau khi đổi xong, Người Ghi Chép bước lên 1 bước
                cham += 1