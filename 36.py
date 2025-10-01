class Block:
    def __init__(self, data):
        self.data = data
        self.next = None

b1, b2, b3 = Block(1), Block(2), Block(3)
b1.next, b2.next = b2, b3

ptr = b1
print("File blocks:", end=" ")
while ptr:
    print(ptr.data, end=" ")
    ptr = ptr.next
