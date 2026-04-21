class Solution(object):
    def countOperations(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        count = 0
        # Điều kiện: CẢ HAI số đều lớn hơn 0 thì mới làm tiếp
        # Nếu 1 trong 2 số chạm mốc 0, vòng lặp sẽ dừng
        while num1 > 0 and num2 > 0:
            # Nếu num1 lớn hơn hoặc bằng num2
            if num1 >= num2:
                num1 = num1 - num2
            
            # Ngược lại (nghĩa là num2 > num1)
            else:
                num2 = num2 - num1
                
            count += 1
            
        return count