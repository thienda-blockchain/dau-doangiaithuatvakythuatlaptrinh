# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # Nếu danh sách rỗng hoặc chỉ có 1-2 nút thì không cần sắp xếp lại
        if not head or not head.next or not head.next.next:
            return

        # Rùa nhích 1 bước, Thỏ nhảy 2 bước
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Lúc này, 'slow' đang đứng ở điểm chính giữa danh sách
        
        # Lấy nửa sau của danh sách (bắt đầu từ ngay sau slow)
        second = slow.next
        
        # CẮT ĐỨT nửa đầu khỏi nửa sau (quan trọng để danh sách không bị lặp vòng)
        slow.next = None 
        
        # Lật ngược danh sách nửa sau (Giống hệt bài 206. Reverse Linked List)
        prev = None
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node
            
        # Lúc này, 'prev' chính là cái đầu mới của nửa sau đã được lật ngược
        
        first = head  # Con trỏ chạy ở nửa đầu
        second = prev # Con trỏ chạy ở nửa sau (đã lật)
        
        # Chừng nào nửa sau vẫn còn nút để đan
        while second:
            # 1. Giữ lại cái móc của các nút tiếp theo để không bị đứt dây
            tmp1 = first.next
            tmp2 = second.next
            
            # 2. Đan chéo: Nút nửa đầu trỏ sang nửa sau, nút nửa sau trỏ về lại nửa đầu
            first.next = second
            second.next = tmp1
            
            # 3. Tiến cả 2 con trỏ lên vị trí tiếp theo đã được giữ lại
            first = tmp1
            second = tmp2