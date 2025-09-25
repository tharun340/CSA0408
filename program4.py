n = int(input("Processes: "))
quant = int(input("Quantum: "))
burst = [int(input(f"Burst time P{i}: ")) for i in range(n)]
rem = burst[:]
t = 0

while any(r > 0 for r in rem):
    for i in range(n):
        if rem[i] > 0:
            run = min(quant, rem[i])
            rem[i] -= run
            t += run
            if rem[i] == 0:
                print(f"P{i} finished at {t}")
