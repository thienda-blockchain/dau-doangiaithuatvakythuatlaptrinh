class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        # Bước 1: Khởi tạo 2 con trỏ ở hai đầu mảng
        trai = 0
        phai = len(arr) - 1
        
        # Bước 2: Ép 2 con trỏ lại gần nhau
        # Mục tiêu là vứt bỏ những phần tử "xa" x nhất
        # Chừng nào số lượng phần tử còn lại vẫn lớn hơn k
        while phai - trai + 1 > k:
            # Tính khoảng cách từ phần tử bên trái đến x
            khoang_cach_trai = abs(arr[trai] - x)
            # Tính khoảng cách từ phần tử bên phải đến x
            khoang_cach_phai = abs(arr[phai] - x)
            
            # So sánh để vứt phần tử xa hơn
            if khoang_cach_trai > khoang_cach_phai:
                # Nếu bên trái xa hơn, bỏ bên trái đi
                trai += 1
            else:
                # Nếu bên phải xa hơn (hoặc bằng nhau nhưng theo đề bài số lớn hơn sẽ bị bỏ)
                # Bỏ bên phải đi
                phai -= 1
                
        # Bước 3: Lấy các phần tử còn lại từ trai đến phai
        return arr[trai:phai+1]