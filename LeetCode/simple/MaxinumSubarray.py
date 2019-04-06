# IP of code : https://leetcode-cn.com/problems/maximum-subarray/
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]

        # for i in range(1, len(nums)):
        #     if nums[i-1] > 0:
        #         nums[i] += nums[i-1]
        #     if res < nums[i]:
        #         res = nums[i]

        # sum = 0
        # for num in nums:
        #     if sum > 0:
        #         sum += num
        #     else:
        #         sum = num
        #     res = res if res > sum else sum

        n = nums[0]
        for i in range(1, len(nums)):
            if n > 0:
                n += nums[i]
            else:
                n = nums[i]
            # update data of res
            res = res if n < res else n

        return res

