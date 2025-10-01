def fcfs(requests, head):
    seek = 0
    for r in requests:
        seek += abs(r - head)
        head = r
    return seek

req = list(map(int, input("Enter requests: ").split()))
head = int(input("Enter initial head: "))
print("Total Seek Time =", fcfs(req, head))
