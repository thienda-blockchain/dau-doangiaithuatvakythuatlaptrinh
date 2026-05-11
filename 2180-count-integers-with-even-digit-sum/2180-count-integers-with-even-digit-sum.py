class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        
        # Bước 1: Duyệt tất cả các số từ 1 cho đến num
        # Dùng range(1, num + 1) để lấy được cả số num ở cuối
        for i in range(1, num + 1):
            tong_chu_so = 0
            
            # Bước 2: Tách từng chữ số của i để cộng lại
            # Bằng cách biến i thành chuỗi (str), ta có thể duyệt qua từng chữ cái của nó
            for chu_so in str(i):
                tong_chu_so += int(chu_so)
                
            # Bước 3: Kiểm tra xem tổng các chữ số có phải là số chẵn không
            # Chia lấy dư cho 2 (% 2), nếu bằng 0 thì là số chẵn
            if tong_chu_so % 2 == 0:
                count += 1
                
        return count