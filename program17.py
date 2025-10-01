def bankers_algorithm():
    n = int(input("Enter number of processes: "))
    m = int(input("Enter number of resources: "))

    print("Enter Allocation Matrix:")
    allocation = [list(map(int, input().split())) for _ in range(n)]

    print("Enter Maximum Matrix:")
    maximum = [list(map(int, input().split())) for _ in range(n)]

    available = list(map(int, input("Enter Available Resources: ").split()))

    # Calculate Need matrix
    need = [[maximum[i][j] - allocation[i][j] for j in range(m)] for i in range(n)]

    finish = [False]*n
    safe_sequence = []

    while len(safe_sequence) < n:
        found = False
        for i in range(n):
            if not finish[i] and all(need[i][j] <= available[j] for j in range(m)):
                for j in range(m):
                    available[j] += allocation[i][j]
                safe_sequence.append(f"P{i}")
                finish[i] = True
                found = True
        if not found:
            print("System is NOT in a safe state!")
            return

    print("System is in a SAFE state.")
    print("Safe Sequence:", ' -> '.join(safe_sequence))


# Run the algorithm
bankers_algorithm()
