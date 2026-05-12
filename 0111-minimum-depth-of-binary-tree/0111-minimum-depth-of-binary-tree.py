# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
         # Nếu cây rỗng, độ sâu bằng 0
        if not root:
            return 0
            
        # Nếu đây là một "chiếc lá" (không có con trái, không có con phải)
        # Quãng đường từ nó đến chính nó là 1
        if not root.left and not root.right:
            return 1
            
        # Nếu bị khuyết nhánh TRÁI, ta BẮT BUỘC phải đi tìm lá ở nhánh PHẢI
        if not root.left:
            return self.minDepth(root.right) + 1
            
        # Nếu bị khuyết nhánh PHẢI, ta BẮT BUỘC phải đi tìm lá ở nhánh TRÁI
        if not root.right:
            return self.minDepth(root.left) + 1
            
        # Nếu có đủ cả 2 nhánh, ta cho quân trinh sát đi cả 2 đường
        # Đường nào ngắn hơn (min) thì ta chọn, nhớ cộng thêm 1 (là cái node hiện tại)
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1