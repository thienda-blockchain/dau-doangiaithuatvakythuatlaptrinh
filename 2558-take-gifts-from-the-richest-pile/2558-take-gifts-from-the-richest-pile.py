import heapq

class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        # Bước 1: Tạo Max-Heap (Hàng đợi ưu tiên lấy số lớn nhất)
        # Python mặc định chỉ có Min-Heap (ưu tiên số nhỏ nhất). 
        # MẸO: Nhân tất cả các số với -1 để "lừa" Python thành Max-Heap.
        max_heap = [-g for g in gifts]
        heapq.heapify(max_heap) # Lệnh này sắp xếp lại mảng thành cấu trúc Heap
        
        # Bước 2: Thực hiện hành động trong k giây
        for _ in range(k):
            # Lấy đống quà to nhất ra (nhớ thêm dấu '-' để trả về số dương ban đầu)
            # heappop tự động lấy và xóa phần tử ưu tiên nhất trong Heap cực nhanh
            max_val = -heapq.heappop(max_heap)
            
            # Tính căn bậc 2 và làm tròn xuống
            # Trong Python, x ** 0.5 chính là căn bậc 2. Ép kiểu int() để làm tròn xuống.
            new_val = int(max_val ** 0.5)
            
            # Đưa giá trị mới vào lại Heap (nhớ nhân lại với -1)
            # heappush tự động nhét vào và sắp xếp lại cực nhanh
            heapq.heappush(max_heap, -new_val)
            
        # Bước 3: Trả về tổng số quà còn lại
        # Vì các số trong heap đang bị âm, ta thêm dấu '-' trước hàm sum() để lấy kết quả dương
        return -sum(max_heap)