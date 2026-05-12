# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Nếu danh sách rỗng hoặc chỉ có 1 nút, chắc chắn không thể có vòng lặp
        if not head or not head.next:
            return False
            
        # Rùa bước 1 bước, Thỏ bước 2 bước
        # Cả hai cùng xuất phát từ vạch đích (head)
        rua = head
        tho = head
        
        # Thỏ chạy nhanh hơn, nên ta chỉ cần kiểm tra xem Thỏ có chạm vạch đích (None) không.
        # Phải kiểm tra cả tho và tho.next vì Thỏ nhảy 2 bước một lúc.
        while tho and tho.next:
            # Rùa nhích 1 bước
            rua = rua.next
            
            # Thỏ nhảy 2 bước
            tho = tho.next.next
            
            # Kiểm tra xem Thỏ có tông trúng Rùa không?
            # Chú ý: Ta so sánh TỌA ĐỘ (tức là chính cái Node đó), chứ không so sánh Giá Trị (val).
            if rua == tho:
                return True # Bắt được vòng lặp!
                
        # Nếu Thỏ chạy thoát ra khỏi danh sách (gặp None), nghĩa là đường thẳng, không có vòng lặp.
        return False