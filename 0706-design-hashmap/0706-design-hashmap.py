class Node:

    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:

    def __init__(self):
        # A prime number size helps distribute keys evenly
        self.size = 1000
        self.buckets = [Node(-1, -1) for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        curr = self.buckets[index]

        while curr.next:
            if curr.next.key == key:
                curr.next.value = value  # Update existing key
                return
            curr = curr.next

        # Insert new key-value pair at the end
        curr.next = Node(key, value)

    def get(self, key: int) -> int:
        index = self._hash(key)
        curr = self.buckets[index].next

        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next

        return -1

    def remove(self, key: int) -> None:
        index = self._hash(key)
        curr = self.buckets[index]

        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next  # Unlink the node
                return
            curr = curr.next