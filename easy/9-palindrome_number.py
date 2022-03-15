# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward.

#     For example, 121 is a palindrome while 123 is not.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        digits = [d for d in str(x)]

        for i in range(int(len(digits)/2)):
            if digits[i] == digits[len(digits)-1-i]:
                continue
            else:
                return False
        return True