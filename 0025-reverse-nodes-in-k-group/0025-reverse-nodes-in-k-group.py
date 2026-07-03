class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 1. Check if there are at least k nodes left in the list
        curr = head
        for _ in range(k):
            if not curr:
                return head  # Less than k nodes left, leave as they are
            curr = curr.next
            
        # 2. Reverse the first k nodes standardly
        prev = None
        curr = head
        for _ in range(k):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        # 3. Head is now the TAIL of the reversed group. 
        # Connect it to the result of reversing the remaining list.
        head.next = self.reverseKGroup(curr, k)
        
        # 4. 'prev' is now the new HEAD of this reversed group
        return prev
