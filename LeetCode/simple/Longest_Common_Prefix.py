# IP of code : https://leetcode-cn.com/problems/longest-common-prefix/submissions/
# tutorial of implementing trie : https://leetcode.com/articles/implement-trie-prefix-tree/
from typing import List

class TrieNode:
    def __init__(self):
        self._R = 26
        self.links = [None] * self._R
        self.End = False
        self.size = 0

    def containsKey(self, ch) -> bool:
        return self.links[ord(ch) - ord('a')] != None

    def get(self, ch):
        return self.links[ord(ch) - ord('a')]

    def put(self, ch, Node):
        self.links[ord(ch) - ord('a')] = Node
        self.size += 1

    def setEnd(self):
        self.isEnd = True

    def isEnd(self) -> bool:
        return self.End

    def getLinks(self) -> int:
        return self.size


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for i in range(len(word)):
            currentChar = word[i]
            if not node.containsKey(currentChar):
                node.put(currentChar, TrieNode())
            node = node.get(currentChar)
        node.setEnd()

    def searchLongestPrefix(self, word):
        node = self.root
        prefix = ''
        for i in range(len(word)):

            # res_L = node.containsKey(currentChar)
            # res_M = node.getLinks() == 1
            # res_R = not node.isEnd()
            currentChar = word[i]
            # if (res_L and res_M )and res_R:
            if (node.containsKey(currentChar) and (node.getLinks() == 1)) and (not node.isEnd()):
                prefix += currentChar
                node = node.get(currentChar)
            else:
                return prefix
        return prefix


class Solution:

    def longestCommonPrefix_trie(self, strs: List[str]) -> str:

        if strs == [] or strs == None:
            return ''
        if len(strs) == 1:
            return strs[0]

        min = strs[0]
        for str in strs:
            if len(min) > len(str):
                min = str

        t = Trie()
        for s in strs:
            t.insert(s)
        return t.searchLongestPrefix(min)

    def longestCommonPrefix_exhaustive(self, strs: List[str]) -> str:
        if strs == []:
            return ''
        res = ''
        s = ''
        s = strs[0]
        for str in strs:
            if len(s) > len(str):
                s = str
        for i in range(len(s)):
            tag = 0

            for j in range(len(strs)-1):
                # return strs[j][i], strs[j+1][i]
                if strs[j][i] == strs[j+1][i]:
                    tag += 1
                else:
                    tag = -1

            if tag == -1:
                break

            if tag+1 == len(strs):
                res += s[i]
        return res

if __name__ == '__main__':
    strs = ["aaa","aa","aaa"]
    solution = Solution()
    prefix_1 = solution.longestCommonPrefix_trie(strs)
    prefix_2 = solution.longestCommonPrefix_exhaustive(strs)
    print(prefix_1, prefix_2)
