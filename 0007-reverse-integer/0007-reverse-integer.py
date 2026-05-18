class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Xác định giới hạn 32-bit nguyên (Từ -2^31 đến 2^31 - 1)
        # MAX_INT = 2147483647
        MAX_INT_CHIA_10 = 214748364 # Dùng để canh chừng trước khi nhân 10
        
        # Lưu lại dấu của x và chuyển x về số dương để dễ tính toán
        # (Trong Python, phép chia lấy dư % cho số âm hoạt động hơi khác C++/Java)
        dau = 1 if x >= 0 else -1
        x = abs(x)
        
        ket_qua = 0
        
        while x != 0:
            # Lấy chữ số cuối cùng
            chu_so_cuoi = x % 10
            # Vứt bỏ chữ số cuối cùng vừa lấy
            x = x // 10
            
            # BƯỚC QUAN TRỌNG: Kiểm tra tràn số (Overflow) TRƯỚC KHI nhân 10
            # Nếu ket_qua hiện tại đã lớn hơn 214748364, lần tới nhân 10 chắc chắn sẽ > 2147483647 (Tràn!)
            # Hoặc nếu nó bằng đúng 214748364, nhưng chữ số cuối chuẩn bị cộng vào lại > 7 (Tràn!)
            if ket_qua > MAX_INT_CHIA_10 or (ket_qua == MAX_INT_CHIA_10 and chu_so_cuoi > 7):
                return 0
                
            # Ráp chữ số cuối vào kết quả
            ket_qua = ket_qua * 10 + chu_so_cuoi
            
        # Trả lại dấu ban đầu cho kết quả
        return ket_qua * dau

        # ---------------------------------------------------------
        # CÁCH 2: Dùng Xử lý Chuỗi (Rất ngắn nhưng Pythonic)
        # ---------------------------------------------------------
        # dau = 1 if x >= 0 else -1
        # ket_qua = int(str(abs(x))[::-1]) * dau
        # # Ép giới hạn 32-bit theo yêu cầu đề bài
        # if ket_qua < -2**31 or ket_qua > 2**31 - 1:
        #     return 0
        # return ket_qua