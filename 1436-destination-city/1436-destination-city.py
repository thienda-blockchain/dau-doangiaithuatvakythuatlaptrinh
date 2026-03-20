class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        diem_bat_dau = set()
        for chang_bay in paths:
            diem_bat_dau.add(chang_bay[0])

        for chang_bay in paths:
            dich = chang_bay[1]

            if dich not in diem_bat_dau:
                return dich
        