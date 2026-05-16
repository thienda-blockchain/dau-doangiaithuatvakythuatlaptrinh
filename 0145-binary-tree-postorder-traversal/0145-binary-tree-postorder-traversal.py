# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        ket_qua = []
        
        # Hàm đệ quy con để duyệt cây
        def duyet_cay(node):
            # Điều kiện dừng: Nếu rễ này rỗng thì quay xe
            if not node:
                return
            
            # QUY TẮC POSTORDER: TRÁI -> PHẢI -> GIỮA
            
            # 1. TRÁI: Dùng đệ quy đi sâu xuống tận cùng nhánh trái trước
            duyet_cay(node.left)
            
            # 2. PHẢI: Sau đó, đi sâu xuống tận cùng nhánh phải
            duyet_cay(node.right)
            
            # 3. GIỮA: Chỉ ghi nhận giá trị của node SAU KHI đã khám phá xong 2 nhánh con
            ket_qua.append(node.val)
            
        # Gọi hàm đệ quy bắt đầu từ cụ Tổ (root)
        duyet_cay(root)
        
        return ket_qua