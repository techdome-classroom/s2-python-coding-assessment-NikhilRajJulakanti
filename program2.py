class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_map={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }

        total=0
        prev_val=0

        for c in s:
            current_val=roman_map[c]
            if current_val>prev_val:
                total+=current_val -2*prev_val
            else:
                total+=current_val
            prev_val=current_val
        return total
sol=Solution()
print(sol.romanToInt("III"))
print(sol.romanToInt("LVIII"))
print(sol.romanToInt("MCMXCIV"))



