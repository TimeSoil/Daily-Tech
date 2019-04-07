# IP of code : https://leetcode-cn.com/problems/merge-two-sorted-lists/submissions/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        if l1 == None and l2 == None:
            return None
        elif l1 == None:
            return l2
        elif l2 == None:
            return l1

        if l2.val <= l1.val:
            root = l2
        else:
            root = l1

        p1, p2 = l1, l2
        while p2 != None:
            if p2.val <= p1.val:
                while p2.next != None and p2.next.val <= p1.val:
                    p2 = p2.next
                l2 = p2.next
                p2.next = p1
            else:
                while p1.next != None and p1.next.val < p2.val:
                    p1 = p1.next
                l2 = p2.next
                p2.next = p1.next
                p1.next = p2
            p2 = l2

        return root

    def mergeTwoListsExtraListNode(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        cur = head
        while l2 and l1:
            if l2.val >= l1.val:
                cur.next = l1
                cur = cur.next
                l1 = l1.next
            else:
                cur.next = l2
                cur = cur.next
                l2 = l2.next

        if not l1:
            cur.next = l2
        else:
            cur.next = l1

        return head.next

