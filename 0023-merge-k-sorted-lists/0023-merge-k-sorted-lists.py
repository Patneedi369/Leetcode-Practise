class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        for i, head_node in enumerate(lists):
            if head_node:
                heapq.heappush(min_heap, (head_node.val, i, head_node))

        dummy = ListNode(0)
        current = dummy

        while min_heap:
            val, i, node = heapq.heappop(min_heap)

            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
        
        return dummy.next