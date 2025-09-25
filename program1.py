import os

pid = os.fork()

if pid == 0:
    # Child
    print(f"Child: PID={os.getpid()} PPID={os.getppid()}")
else:
    # Parent
    print(f"Parent: PID={os.getpid()} Child PID={pid}")
