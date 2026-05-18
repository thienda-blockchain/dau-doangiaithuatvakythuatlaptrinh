class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Tạo một cuốn sổ tay (Set) để ghi nhớ những con số đã từng xuất hiện
        # Set tìm kiếm siêu nhanh O(1)
        da_thay = set()
        
        # Hàm phụ: Tính tổng bình phương các chữ số của một số
        def tinh_tong_binh_phuong(so):
            tong = 0
            while so > 0:
                # Lấy chữ số cuối cùng (y hệt như kỹ thuật bạn bôi đen ở bài 7)
                chu_so = so % 10
                # Cắt bỏ chữ số cuối cùng đi
                so = so // 10
                # Cộng bình phương của chữ số vừa lấy vào tổng
                tong += chu_so * chu_so
            return tong
            
        # Vòng lặp chính: Cứ tiếp tục tính cho đến khi n bằng 1
        # HOẶC cho đến khi n rơi vào một số đã từng xuất hiện trong sổ tay (Vòng lặp vô tận)
        while n != 1 and n not in da_thay:
            # Ghi n hiện tại vào sổ tay trước khi biến đổi nó
            da_thay.add(n)
            
            # Biến đổi n thành con số mới (tổng bình phương các chữ số)
            n = tinh_tong_binh_phuong(n)
            
        # Khi vòng lặp dừng lại, chỉ có 2 khả năng:
        # 1. n đã bằng 1 (Số hạnh phúc!) -> Trả về True
        # 2. n nằm trong sổ tay (Vòng lặp vô tận, số bất hạnh!) -> Trả về False
        return n == 1

        # ---------------------------------------------------------
        # CÁCH 2: DÙNG RÙA VÀ THỎ (Không dùng Set - O(1) Bộ nhớ)
        # ---------------------------------------------------------
        # def tinh_tong_binh_phuong(so):
        #     tong = 0
        #     while so > 0:
        #         chu_so = so % 10
        #         so = so // 10
        #         tong += chu_so * chu_so
        #     return tong
        # 
        # rua = n
        # tho = tinh_tong_binh_phuong(n)
        # 
        # while tho != 1 and rua != tho:
        #     rua = tinh_tong_binh_phuong(rua)
        #     tho = tinh_tong_binh_phuong(tinh_tong_binh_phuong(tho))
        #     
        # return tho == 1