# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev = dummy
        curr = head
        count = 0
        while curr and curr.next:
            if count%2==0:
                first = curr
                second = curr.next
                
                prev.next = second
                first.next = second.next
                second.next = first
            else:
                prev = curr
                curr = curr.next
            count += 1
        
        return dummy.next