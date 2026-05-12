class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        trai = 0
        phai = len(nums) - 1
        
        # Bước 2: Vòng lặp thu hẹp phạm vi
        # Chừng nào vùng tìm kiếm vẫn còn (trai chưa vượt qua phai)
        while trai <= phai:
            
            # Tính vị trí chính giữa của vùng tìm kiếm hiện tại
            # Dùng // để chia lấy phần nguyên
            giua = (trai + phai) // 2
            
            # Bốc số ở giữa ra so sánh với mục tiêu
            so_giua = nums[giua]
            
            # Trường hợp 1: Trúng phóc!
            if so_giua == target:
                return giua
                
            # Trường hợp 2: Số ở giữa NHỎ HƠN mục tiêu
            # Vì mảng đã sắp xếp tăng dần, mọi số từ 'trai' đến 'giua' chắc chắn cũng nhỏ hơn mục tiêu
            # Ta bỏ đi nửa trái, thu hẹp vùng tìm kiếm sang nửa phải
            elif so_giua < target:
                trai = giua + 1
                
            # Trường hợp 3: Số ở giữa LỚN HƠN mục tiêu
            # Mọi số từ 'giua' đến 'phai' chắc chắn cũng lớn hơn mục tiêu
            # Ta bỏ đi nửa phải, thu hẹp vùng tìm kiếm sang nửa trái
            else:
                phai = giua - 1
                
        # Bước 3: Tìm hết mọi ngóc ngách mà không thấy
        return -1