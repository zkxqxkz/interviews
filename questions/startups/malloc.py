"""
Implement malloc. Define two functions - alloc and free. 
alloc take in byte size and allocates size bytes for usage
free takes in the starting ptr address and relinquishes the space taken in its allocation

Talk about tradeoffs in the implementation and write tests to verify 
"""


class Malloc:
    def __init__(self, size: int): ...

    def alloc(self, size: int): ...

    def free(self, ptr: int): ...


# Solution


class Malloc:
    def __init__(
        self,
        size: int,
    ):
        self.size = size
        self.allocated = {}  # key = start idx, value = end of the addr

    def alloc(self, size) -> int:
        # return the starting int, -1 if not alloced
        if size > self.size:
            return -1

        # initial allocation,
        if len(self.allocated) == 0:
            self.allocated[0] = size - 1
            return 0

        # iterate to find the gap
        candidate_start_addr = 0
        for start_addr, end_addr in sorted(self.allocated.items()):
            if start_addr - candidate_start_addr >= size:
                self.allocated[candidate_start_addr] = size + candidate_start_addr - 1
                return candidate_start_addr
            candidate_start_addr = end_addr + 1

        # find the memory at the end
        if self.size - candidate_start_addr >= size:
            self.allocated[candidate_start_addr] = candidate_start_addr + size - 1
            return candidate_start_addr
        return -1

    def free(self, ptr: int):
        breakpoint()
        if ptr in self.allocated:
            del self.allocated[ptr]

    def display(self):
        print((self.allocated))


memory = Malloc(16)

ptr = memory.alloc(4)
memory.display()

ptr2 = memory.alloc(8)
memory.display()

p3 = memory.alloc(4)
memory.display()

# should not work
p4 = memory.alloc(1)
memory.display()

# free pointer at 4
memory.free(ptr2)
memory.display()

ptr5 = memory.alloc(3)
memory.display()

ptr7 = memory.alloc(3)
memory.display()

ptr8 = memory.alloc(2)
memory.display()

memory.free(ptr5)
memory.free(ptr7)
memory.display()

memory.alloc(6)
memory.display()
