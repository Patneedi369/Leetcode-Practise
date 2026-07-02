# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        prev = dummy
        curr = head
        delvalue = None
        while curr and curr.next:
            if curr.next.val == curr.val or curr.val == delvalue:
                delvalue = curr.val
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        if curr and curr.val == delvalue:
            prev.next = None
        return dummy.next