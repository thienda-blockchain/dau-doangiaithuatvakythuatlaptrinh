# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        ket_qua = []
        
        # Hàm đệ quy con để duyệt cây
        def duyet_cay(node):
            # Điều kiện dừng: Nếu rễ này rỗng (không có lá, không có cây), thì quay xe
            if not node:
                return
            
            # QUY TẮC PREORDER: GIỮA -> TRÁI -> PHẢI
            
            # 1. GIỮA: Ghi nhận giá trị của node hiện tại vào mảng kết quả NGAY LẬP TỨC
            ket_qua.append(node.val)
            
            # 2. TRÁI: Dùng đệ quy bắt nó đi khám phá toàn bộ nhánh bên trái
            duyet_cay(node.left)
            
            # 3. PHẢI: Sau khi khám phá xong bên trái, mới đi tiếp sang nhánh bên phải
            duyet_cay(node.right)
            
        # Gọi hàm đệ quy bắt đầu từ cụ Tổ (root)
        duyet_cay(root)
        
        return ket_qua

        # ---------------------------------------------------------
        # CÁCH 2: DÙNG VÒNG LẶP & STACK (Không dùng đệ quy)
        # ---------------------------------------------------------
        # if not root: return []
        # stack = [root]
        # ket_qua = []
        # while stack:
        #     node = stack.pop()
        #     ket_qua.append(node.val)
        #     # Chú ý: Vì Stack là Vào sau-Ra trước (LIFO), ta nhét nhánh Phải vào trước
        #     # Để lát nữa nhánh Trái sẽ nằm trên đỉnh và được bốc ra trước!
        #     if node.right: stack.append(node.right)
        #     if node.left: stack.append(node.left)
        # return ket_qua