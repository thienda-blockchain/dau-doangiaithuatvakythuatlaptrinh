# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        ket_qua = []
        
        # Hàm đệ quy mang theo "cuốn sổ tay" (duong_di_hien_tai)
        def dfs(node, duong_di_hien_tai):
            if not node:
                return
            
            # 1. Ghi số của phòng hiện tại vào sổ tay
            # (Giống hệt bước GIỮA của Preorder Traversal)
            duong_di_hien_tai += str(node.val)
            
            # 2. CHỐT CHẶN: Kiểm tra xem đây có phải là "Ngõ cụt" (Chiếc lá) không?
            if not node.left and not node.right:
                # Nếu đúng là ngõ cụt, lưu lại cuốn sổ vào kết quả và quay đầu
                ket_qua.append(duong_di_hien_tai)
                return
            
            # 3. Nếu chưa phải ngõ cụt, thêm mũi tên "->" để chuẩn bị đi tiếp
            duong_di_hien_tai += "->"
            
            # Đi khám phá tiếp nhánh Trái và nhánh Phải với cuốn sổ đã cập nhật
            dfs(node.left, duong_di_hien_tai)
            dfs(node.right, duong_di_hien_tai)
            
        # Bắt đầu từ Cụ Tổ với cuốn sổ tay trống rỗng ""
        if root:
            dfs(root, "")
            
        return ket_qua