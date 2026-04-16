class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        #Tách chuỗi thành danh sách các từ
        words = title.split()
        
        result = []
        
        for word in words:
            # Kiểm tra độ dài của từ
            if len(word) <= 2:
                # Nếu từ có 1 hoặc 2 chữ cái -> Chuyển hết thành chữ thường
                result.append(word.lower())
            else:
                # Nếu từ có từ 3 chữ cái trở lên:
                # Dùng capitalize() để viết hoa chữ đầu và viết thường các chữ sau
                result.append(word.capitalize())
        
        # Bước 3: Nối các từ lại bằng dấu cách
        return " ".join(result)