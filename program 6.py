# Preemptive Priority Scheduling - Simple Python Code

def priority_preemptive(processes):
    n = len(processes)
    time, completed = 0, 0
    bt = [p[1] for p in processes]   # burst time
    wt, tat = [0]*n, [0]*n

    while completed < n:
        # pick process with highest priority (lowest value)
        idx = -1
        pr = 9999
        for i in range(n):
            if processes[i][0] <= time and bt[i] > 0 and processes[i][2] < pr:
                pr = processes[i][2]
                idx = i
        if idx == -1:
            time += 1
            continue

        bt[idx] -= 1
        if bt[idx] == 0:
            completed += 1
            finish = time + 1
            tat[idx] = finish - processes[idx][0]
            wt[idx] = tat[idx] - processes[idx][1]
        time += 1

    print("P\tAT\tBT\tPR\tWT\tTAT")
    for i, p in enumerate(processes):
        print(f"P{i+1}\t{p[0]}\t{p[1]}\t{p[2]}\t{wt[i]}\t{tat[i]}")
    print("\nAvg WT:", sum(wt)/n, " Avg TAT:", sum(tat)/n)


# (Arrival, Burst, Priority)
processes = [(0,5,2),(1,3,1),(2,8,4),(3,6,2)]
priority_preemptive(processes)
