# Valid Parentheses

#  Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.


# Example 1:

# Input: s = "()"
# Output: true

# Example 2:

# Input: s = "()[]{}"
# Output: true

# Example 3:

# Input: s = "(]"
# Output: false


# Constraints:

#     1 <= s.length <= 104
#     s consists of parentheses only '()[]{}'.


class Solution:
    def isValid(self, s: str) -> bool:
        par_stack = []
        for i, c in enumerate(s):
            if c == "(":
                par_stack.append("(")
            if c == "[":
                par_stack.append("[")
            if c == "{":
                par_stack.append("{")

            if c == ")":
                if len(par_stack) < 1:
                    return False
                if par_stack[-1] != "(":
                    return False
                par_stack.pop()

            if c == "}":
                if len(par_stack) < 1:
                    return False
                if par_stack[-1] != "{":
                    return False
                par_stack.pop()

            if c == "]":
                if len(par_stack) < 1:
                    return False
                if par_stack[-1] != "[":
                    return False
                par_stack.pop()

        return len(par_stack) == 0

    def main(self):
        print(self.isValid("()[]{}"))


if __name__ == "__main__":
    Solution().main()
