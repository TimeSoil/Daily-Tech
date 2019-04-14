# 假如你有一块面包，你要将这块面包均匀的分成正方块，且分出的正方块尽可能大。
# https://zh.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
import random
from typing import List


def maxinumCommonSoil(long: int, wide: int):
    if long < wide:
        return -1
    if wide == 0:
        return long
    else:
        q = long // wide
        remainder = long - wide * q
        return maxinumCommonSoil(wide, remainder)

# 算法图解代码
def quicksort(data: List[int]):
    if len(data) < 2:
        return data

    else:
        pivot = data[0]
        less = [i for i in data if i <= pivot]
        greater = [i for i in data if i > pivot]

        return quicksort(less) + pivot + quicksort(greater)

if __name__ == '__main__':
    # GCD = maxinumCommonSoil(1681, 640)
    # print(GCD)

    data = [1,2,3,4,5,6,1,2,8,9,2]
    quicksort(data)
    # for i in data[]:
    #     print(i)