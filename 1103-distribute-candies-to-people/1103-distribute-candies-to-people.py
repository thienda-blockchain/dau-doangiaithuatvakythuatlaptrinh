class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        # Tạo ô lưu trữ theo số lượng người được nhận, ví dụ num_people = 3 thì [_;_;_]
        ans = [0] * num_people
        # Biến i đại diện cho số kẹo sẽ phát ở lượt này (bắt đầu từ 1)
        # Biến index để biết đang phát kẹo cho người thứ mấy (0 đến num_people-1)
        i = 1
        index = 0

        while candies > 0:
            # Số kẹo thực tế phát ra: 
            # Là con số nhỏ hơn giữa (số kẹo dự định phát) và (số kẹo còn lại trong túi)
            to_give = min(i, candies)
            
            # Cộng kẹo vào ô tương ứng trong mảng kết quả
            # Dùng toán tử % để tự động quay lại người đầu tiên khi tới cuối hàng
            ans[index % num_people] += to_give
            
            # Trừ số kẹo đã phát đi từ tổng số kẹo ban đầu
            candies -= to_give
            
            # Tăng số kẹo dự định phát cho lượt sau lên 1
            i += 1
            # Chuyển sang người tiếp theo
            index += 1
            
        return ans
