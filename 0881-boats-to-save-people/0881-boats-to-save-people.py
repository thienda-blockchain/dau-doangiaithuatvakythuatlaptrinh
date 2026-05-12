class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        # Bước 1: Sắp xếp mọi người theo cân nặng từ nhẹ nhất đến nặng nhất
        people.sort()
        
        # Bước 2: Đặt hai con trỏ ở hai đầu
        trai = 0                  # Người nhẹ nhất
        phai = len(people) - 1    # Người nặng nhất
        
        so_thuyen = 0
        
        # Chừng nào chưa giải cứu hết mọi người (hai con trỏ chưa vượt qua nhau)
        while trai <= phai:
            # Kiểm tra xem người nặng nhất và người nhẹ nhất có thể đi chung 1 thuyền không?
            if people[trai] + people[phai] <= limit:
                # Nếu đi chung được, cho cả 2 lên thuyền -> Người nhẹ tiếp theo chuẩn bị
                trai += 1
                
            # Dù có đi chung được hay không, người nặng nhất HIỂN NHIÊN phải lên thuyền
            # (Nếu không ghép được với người nhẹ nhất, họ bắt buộc phải đi 1 mình)
            phai -= 1
            
            # Mỗi lần lặp là một chiếc thuyền rời bến
            so_thuyen += 1
            
        return so_thuyen