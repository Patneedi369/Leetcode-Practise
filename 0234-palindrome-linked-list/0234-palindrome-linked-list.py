# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head: Optional[ListNode]) -> bool:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
            
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # 1. Base cases: Empty list or single node is ALWAYS a palindrome
        if not head or not head.next:
            return True

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        if fast:
            # odd number of nodes
            second_half = self.reverse(slow.next)
        else:
            # even number of nodes
            second_half = self.reverse(slow)
        slow.next = None

        p1 = head
        p2 = second_half
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next

        return True