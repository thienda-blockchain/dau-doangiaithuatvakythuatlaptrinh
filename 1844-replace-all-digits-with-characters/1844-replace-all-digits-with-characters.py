class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
       
        # chuyển sang dạng danh sách (list) để dễ dàng thay thế.
        res = list(s)
        
        # Đề bài cho biết các chữ số luôn nằm ở vị trí lẻ (1, 3, 5...)
        # Ta sẽ chạy vòng lặp bước nhảy 2 để tìm đúng các chữ số.
        for i in range(1, len(res), 2):
            char_truoc = res[i-1]  # Chữ cái đứng ngay trước con số hiện tại
            buoc_tien = int(res[i]) # Giá trị của con số hiện tại (chuyển từ chữ sang số nguyên)
            
            # Thực hiện phép toán "Shift" (Tịnh tiến):
            # 1. ord(char_truoc): Lấy mã số của chữ cái trước.
            # 2. Cộng thêm bước tiến.
            # 3. chr(...): Chuyển kết quả về lại dạng chữ cái.
            res[i] = chr(ord(char_truoc) + buoc_tien)
            
        return "".join(res)   # Nối danh sách lại thành chuỗi hoàn chỉnh để trả về