class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """
        digits = number.replace(" ", "").replace("-","")
        ket_qua = []
        i = 0
        n = len(digits)
        while n - i > 4:
            ket_qua.append(digits[i:i + 3])
            i += 3

        con_lai = n - i
        if con_lai == 4:
            ket_qua.append(digits[i: i+2])
            ket_qua.append(digits[i + 2: i + 4])
        else:
            ket_qua.append(digits[i:])

        return "-".join(ket_qua)