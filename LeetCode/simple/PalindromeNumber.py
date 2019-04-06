# IP of code : https://leetcode-cn.com/problems/palindrome-number/submissions/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x < 0:
        #     return False
        # else:
        #     y = str(x)[::-1]
        #     if y == str(x):
        #         return True
        #     else: 
        #         return False

        if x < 0:
            return False
        if x // 10 == 0:
            return True

        res = 0
        pop = 0
        y = x

        while y != 0:
            pop = y % 10
            y //= 10

            res = res * 10 + pop

        return True if res == x else False
