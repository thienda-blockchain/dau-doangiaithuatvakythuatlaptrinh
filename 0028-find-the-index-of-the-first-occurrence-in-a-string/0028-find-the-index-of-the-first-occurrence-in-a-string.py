class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle: 
            return 0
        
        do_dai_kim = len(needle)
        do_dai_rom = len(haystack)
        
        for i in range(do_dai_rom - do_dai_kim + 1):
            if haystack[i : i + do_dai_kim] == needle:
                return i

        return -1