def scan(requests, head, size, direction):
    requests.sort()
    seek, pos = 0, 0
    while pos < len(requests) and requests[pos] < head:
        pos += 1
    if direction == "right":
        for r in requests[pos:]:
            seek += abs(r - head); head = r
        seek += abs(size - 1 - head); head = size - 1
        for r in reversed(requests[:pos]):
            seek += abs(r - head); head = r
    else:
        for r in reversed(requests[:pos]):
            seek += abs(r - head); head = r
        seek += head; head = 0
        for r in requests[pos:]:
            seek += abs(r - head); head = r
    return seek

req = list(map(int, input("Enter requests: ").split()))
head = int(input("Enter initial head: "))
size = int(input("Enter disk size: "))
direction = input("Enter direction (left/right): ")
print("Total Seek Time =", scan(req, head, size, direction))
