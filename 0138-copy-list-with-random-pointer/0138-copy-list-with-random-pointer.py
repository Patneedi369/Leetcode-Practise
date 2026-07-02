"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapping = {}
        curr = head
        while curr:
            new_node = Node(curr.val)
            mapping[curr] = new_node
            curr = curr.next

        curr = head
        while curr:
            new_node = mapping[curr]
            # Use .get() or an if-statement to handle None gracefully
            new_node.next = mapping.get(curr.next)
            new_node.random = mapping.get(curr.random)
            curr = curr.next
        
        return mapping.get(head)