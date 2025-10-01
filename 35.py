def indexed_allocation(index_blocks):
    print("File allocated at blocks:", index_blocks)

blocks = list(map(int, input("Enter index blocks: ").split()))
indexed_allocation(blocks)

