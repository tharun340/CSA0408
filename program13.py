def first_fit(blocks, processes):
    allocation = [-1]*len(processes)
    b = blocks.copy()

    for i, p in enumerate(processes):
        for j, block in enumerate(b):
            if block >= p:
                allocation[i] = j
                b[j] -= p
                break
    print("\nFirst Fit Allocation:")
    print("Process\tSize\tBlock")
    for i, a in enumerate(allocation):
        print(f"P{i+1}\t{processes[i]}\t{a if a!=-1 else 'Not Allocated'}")

def best_fit(blocks, processes):
    allocation = [-1]*len(processes)
    b = blocks.copy()

    for i, p in enumerate(processes):
        best_idx = -1
        for j, block in enumerate(b):
            if block >= p:
                if best_idx == -1 or block < b[best_idx]:
                    best_idx = j
        if best_idx != -1:
            allocation[i] = best_idx
            b[best_idx] -= p

    print("\nBest Fit Allocation:")
    print("Process\tSize\tBlock")
    for i, a in enumerate(allocation):
        print(f"P{i+1}\t{processes[i]}\t{a if a!=-1 else 'Not Allocated'}")

def worst_fit(blocks, processes):
    allocation = [-1]*len(processes)
    b = blocks.copy()

    for i, p in enumerate(processes):
        worst_idx = -1
        for j, block in enumerate(b):
            if block >= p:
                if worst_idx == -1 or block > b[worst_idx]:
                    worst_idx = j
        if worst_idx != -1:
            allocation[i] = worst_idx
            b[worst_idx] -= p

    print("\nWorst Fit Allocation:")
    print("Process\tSize\tBlock")
    for i, a in enumerate(allocation):
        print(f"P{i+1}\t{processes[i]}\t{a if a!=-1 else 'Not Allocated'}")

# Example usage
blocks = [100, 500, 200, 300, 600]
processes = [212, 417, 112, 426]

first_fit(blocks, processes)
best_fit(blocks, processes)
worst_fit(blocks, processes)
