# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # Tạo một nốt "Lót nền" (Dummy node). 
        # Nốt này không có giá trị thực tế, chỉ dùng để làm điểm neo giữ cái rễ của cây mới.
        dummy = TreeNode(-1)
        
        # Con trỏ "Thợ xây" (self.current) luôn chỉ vào viên gạch cuối cùng vừa được đặt.
        # Ban đầu nó chỉ vào nốt lót nền.
        self.current = dummy
        
        # Hàm duyệt In-order (Trái - Giữa - Phải)
        def duyet_inorder(node):
            if not node:
                return
            
            # 1. TRÁI: Đi mò xuống tận cùng bên trái để tìm số nhỏ nhất trước
            duyet_inorder(node.left)
            
            # 2. GIỮA: Xử lý nốt hiện tại
            # - Cắt bỏ hoàn toàn nhánh trái của nốt này (vì luật mới yêu cầu không có nốt trái)
            node.left = None
            
            # - Nối nốt hiện tại vào CÁNH TAY PHẢI của viên gạch cuối cùng
            self.current.right = node
            
            # - Dời tay "Thợ xây" sang viên gạch mới vừa đặt để chuẩn bị cho lượt sau
            self.current = node
            
            # 3. PHẢI: Đi xử lý tiếp nhánh phải
            duyet_inorder(node.right)
            
        # Bắt đầu gọi thợ xây đi đập cây cũ
        duyet_inorder(root)
        
        # Trả về cái cây mới. Nhớ bỏ qua nốt "Lót nền" (dummy) lúc đầu nhé!
        return dummy.right