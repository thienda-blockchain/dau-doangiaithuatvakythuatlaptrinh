# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # Bước 1: Vẫn phải có toa tàu mồi (dummy) để đề phòng trường hợp
        # phải xóa ngay cái nút đầu tiên của danh sách.
        dummy = ListNode(0)
        dummy.next = head
        
        # Bước 2: Dùng 2 con trỏ, cùng xuất phát từ dummy
        truoc = dummy
        sau = dummy
        
        # Bước 3: Cho con trỏ 'sau' chạy trước n bước để tạo "khoảng cách an toàn"
        # Khoảng cách này chính bằng n.
        for _ in range(n):
            sau = sau.next
            
        # Bước 4: Cả 2 cùng tiến lên với tốc độ bằng nhau
        # Cho đến khi con trỏ 'sau' đâm đầu vào bức tường (hết danh sách)
        while sau.next:
            truoc = truoc.next
            sau = sau.next
            
        # Lúc này, do khoảng cách luôn là n, nên khi 'sau' ở cuối cùng,
        # 'truoc' sẽ đứng CHÍNH XÁC ngay TRƯỚC cái nút cần bị xóa!
        
        # Bước 5: Tháo móc, bỏ qua cái nút ở giữa
        truoc.next = truoc.next.next
        
        return dummy.next
        