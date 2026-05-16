# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
         # BƯỚC 1: Xử lý các trường hợp rỗng (Base cases)
        # Nếu cả hai cây đều rỗng -> Chắc chắn giống nhau (cùng là hư không)
        if not p and not q:
            return True
        
        # Nếu một cây rỗng, cây kia lại có nốt -> Chắc chắn khác nhau (lệch cấu trúc)
        # (Chỉ cần đến dòng này vì dòng trên đã chặn trường hợp cả 2 cùng rỗng rồi)
        if not p or not q:
            return False
        
        # BƯỚC 2: So sánh giá trị hiện tại
        # Nếu cả hai đều có nốt, nhưng con số ghi trên nốt lại khác nhau -> Khác nhau
        if p.val != q.val:
            return False
        
        # BƯỚC 3: Đệ quy
        # Vượt qua 3 vòng kiểm tra trên, nghĩa là Cụ Tổ (Root) của 2 cây đã giống hệt nhau.
        # Giờ ta vung tay sai Đệ quy đi kiểm tra đồng thời:
        # 1. Nhánh trái của p có giống nhánh trái của q không?
        # 2. Nhánh phải của p có giống nhánh phải của q không?
        # Cả hai phải CÙNG ĐÚNG (and) thì 2 cây mới hoàn toàn giống nhau!
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)