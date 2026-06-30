class Solution:
    
    def reverse(self, head):
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        slow = head
        fast = head.next

        # find the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse the second half
        second = self.reverse(slow.next)
        slow.next = None  # Cut the list in half
        
        # 3. Merge the two halves
        first = head
        while second:
            p1, p2 = first.next, second.next
            first.next = second
            second.next = p1
            first, second = p1, p2
        
    