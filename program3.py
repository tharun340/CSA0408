n = int(input("Enter number of processes: "))
burst = [int(input(f"Burst time for P{i}: ")) for i in range(n)]

time = 0
for i in range(n):
    print(f"P{i} start={time} end={time+burst[i]}")
    time += burst[i]
