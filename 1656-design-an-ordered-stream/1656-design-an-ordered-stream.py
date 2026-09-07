class OrderedStream:

    def __init__(self, n: int):
        # Create an array of size n + 1 (1-indexed) initialized with None
        self.stream = [None] * (n + 1)
        # Pointer to track the current expected index
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        # Store the value at index idKey
        self.stream[idKey] = value
        
        chunk = []
        # Collect contiguous elements starting from self.ptr
        while self.ptr < len(self.stream) and self.stream[self.ptr] is not None:
            chunk.append(self.stream[self.ptr])
            self.ptr += 1
            
        return chunk