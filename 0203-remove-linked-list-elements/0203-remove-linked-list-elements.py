# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        # Bước 1: Khởi tạo Dummy Node (Vị cứu tinh)
        # Dummy node giúp ta xử lý trường hợp mảng bắt đầu bằng chính phần tử cần xóa một cách dễ dàng
        dummy = ListNode(0)
        dummy.next = head
        
        # Bước 2: Dùng con trỏ curr bắt đầu từ dummy
        curr = dummy
        
        # Bước 3: Chừng nào vẫn còn phần tử tiếp theo để kiểm tra
        while curr and curr.next:
            
            # Nếu phần tử tiếp theo mang giá trị cần xóa
            if curr.next.val == val:
                # "Tháo móc", bỏ qua phần tử cần xóa, nối thẳng tới phần tử sau nó
                curr.next = curr.next.next
            else:
                # Nếu phần tử tiếp theo an toàn, ta mới yên tâm bước lên
                curr = curr.next
                
        # Trả về phần đầu thực sự của danh sách, bỏ qua dummy
        return dummy.next