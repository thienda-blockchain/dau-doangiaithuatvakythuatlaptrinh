class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Bước 1: Khởi tạo ống cầu lông (Stack)
        stack = []
        
        # Bước 2: Tạo một cái từ điển (Sổ tay) để tra cứu xem
        # ngoặc đóng nào thì đi với ngoặc mở nào
        tra_cuu = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        # Bước 3: Duyệt qua từng dấu ngoặc trong chuỗi
        for ngoac in s:
            
            # Nếu là ngoặc ĐÓNG (nó có mặt trong keys của từ điển)
            if ngoac in tra_cuu:
                
                # Bốc phần tử trên đỉnh Stack ra để kiểm tra
                # Nếu Stack rỗng (chưa có ngoặc mở nào), thì lấy một ký tự tạm là '#'
                dinh_stack = stack.pop() if stack else '#'
                
                # Kiểm tra: Cái ngoặc mở vừa bốc ra có KHỚP với ngoặc đóng hiện tại không?
                if tra_cuu[ngoac] != dinh_stack:
                    return False # Ngoại tình hoặc trật nhịp -> Sai ngay!
                    
            # Nếu là ngoặc MỞ
            else:
                # Cứ ném vào ống chờ đóng
                stack.append(ngoac)
                
        # Bước 4: Cuối cùng, nếu tất cả đều có đôi có cặp, Stack phải rỗng.
        # Nếu vẫn còn ngoặc mở bơ vơ (ví dụ "(["), trả về False.
        return len(stack) == 0