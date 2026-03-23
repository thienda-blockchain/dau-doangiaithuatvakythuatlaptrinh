class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        dem_5 = 0
        dem_10 = 0
        for i in bills:
            if(i == 5):
                dem_5 += 1
            elif(i == 10):
                if (dem_5 == 0):
                    return False
                dem_5 -= 1
                dem_10 += 1

            elif(i == 20):
                if(dem_10 >= 1 and dem_5 >=1):
                    dem_5 -= 1
                    dem_10 -= 1
                elif(dem_5 >= 3):
                    dem_5 -= 3
                else:
                    return False

        return True
