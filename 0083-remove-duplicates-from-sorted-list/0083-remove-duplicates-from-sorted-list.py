# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Nếu danh sách rỗng, trả về luôn
        if not head:
            return head
            
        # Đặt con trỏ 'curr' (hiện tại) bắt đầu từ đầu danh sách
        curr = head
        
        # Chừng nào vẫn còn nút hiện tại VÀ nút tiếp theo để so sánh
        while curr and curr.next:
            
            # Nếu giá trị của nút hiện tại GIỐNG HỆT giá trị của nút tiếp theo
            if curr.val == curr.next.val:
                # Hành động: Bỏ qua nút tiếp theo (bị trùng)
                # Bằng cách nối móc của nút hiện tại thẳng đến nút "sau của sau"
                curr.next = curr.next.next
            else:
                # Nếu hai nút khác nhau (không bị trùng)
                # Ta an tâm bước con trỏ lên một bước để kiểm tra cặp tiếp theo
                curr = curr.next
                
        # Trả về cái đầu của danh sách đã được dọn dẹp
        return head
        