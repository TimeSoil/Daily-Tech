# IP of code : https://leetcode-cn.com/problems/valid-parentheses/submissions/
class Solution:
    def isValid(self, s: str) -> bool:

        sL = len(s)
        if sL == 0:
            return True
        elif sL % 2 == 1:
            return False

        stack = []
        mapping = {}
        mapping[')'] = '('
        mapping[']'] = '['
        mapping['}'] = '{'

        for ch in s:
            if ch in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[ch] != top_element:
                    return False
            else:
                stack.append(ch)
        return not stack
