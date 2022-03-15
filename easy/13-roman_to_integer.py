# roman to integer

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D 
# and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# For example, 2 is written as II in Roman numeral, just two one's added 
# together. 12 is written as XII, which is simply X + II. The number 27 is 
# written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. 
# However, the numeral for four is not IIII. Instead, the number four is written
# as IV. Because the one is before the five we subtract it making four. The same
# principle applies to the number nine, which is written as IX. There are six 
# instances where subtraction is used:

#     I can be placed before V (5) and X (10) to make 4 and 9. 
#     X can be placed before L (50) and C (100) to make 40 and 90. 
#     C can be placed before D (500) and M (1000) to make 400 and 900.

# Given a roman numeral, convert it to an integer.
class Solution:
    def romanToInt(self, s: str) -> int:
        s_lower = s.lower()
        total = 0 
        lookup = {
            'i': 1,
            'v': 5,
            'x': 10,
            'l': 50,
            'c': 100,
            'd': 500,
            'm': 1000,
            'iv': 4,
            'ix': 9,
            'xl': 40,
            'xc': 90,
            'cd': 400,
            'cm': 900,
        }
        i = 0
        while i < len(s_lower):
            if s_lower[i:i+2] == "iv" or s_lower[i:i+2] == "ix" \
            or s_lower[i:i+2] == "xl" or s_lower[i:i+2] == "xc" \
            or s_lower[i:i+2] == "cd" or s_lower[i:i+2] == "cm":
                total += lookup[s_lower[i:i+2]]
                i += 2
            else:
                total += lookup[s_lower[i]]
                i += 1

        return total


    def main(self):
        print("total of \"MCMXCIV\" = ", self.romanToInt("MCMXCIV"))

if __name__ == "__main__":
    Solution().main()