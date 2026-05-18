class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Bước 1: Xác định n (chiều dài của mảng)
        n = len(nums)
        
        # Bước 2: Tính "Tổng kỳ vọng" nếu mảng có ĐẦY ĐỦ các số từ 0 đến n
        # Dùng công thức Gauss: Tổng = n * (n + 1) / 2
        # (Lưu ý: Vì dãy bắt đầu từ 0 nên tổng từ 0 đến n cũng bằng tổng từ 1 đến n)
        tong_ky_vong = n * (n + 1) // 2
        
        # Bước 3: Tính "Tổng thực tế" của các con số đang có mặt trong mảng
        # Hàm sum() của Python chạy cực kỳ nhanh và tối ưu bằng C bên dưới
        tong_thuc_te = sum(nums)
        
        # Bước 4: Tìm kẻ đi lạc!
        # Số bị thiếu chắc chắn bằng Tổng đầy đủ trừ đi Tổng thực tế
        so_bi_thieu = tong_ky_vong - tong_thuc_te
        
        return so_bi_thieu

        # ---------------------------------------------------------
        # CÁCH 2: Dùng phép toán XOR (Dành cho dân "Pro" Bitwise)
        # ---------------------------------------------------------
        # ket_qua = len(nums)
        # for i, num in enumerate(nums):
        #     ket_qua ^= i ^ num
        # return ket_qua