# IP of code : https://leetcode-cn.com/problems/reverse-integer/
class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        # s, x = (1, x) if x > 0 else (-1, 0-x)
        print(s, x)
        while (x != 0):
            t = x % 10
            x //= 10

            if rev > ((1 << 31) // 10):
                return 0
            elif rev == ((1 << 31) // 10) and t > 7:
                return 0
            rev = rev * 10 + t
        return s * rev

if __name__ == '__main__':
    s = Solution()
    res = s.reverse(-123)
    print(res)
