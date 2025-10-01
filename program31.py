def fifo(pages, frames):
    frame = []
    faults = 0
    for p in pages:
        if p not in frame:
            if len(frame) < frames:
                frame.append(p)
            else:
                frame.pop(0)
                frame.append(p)
            faults += 1
    return faults

pages = list(map(int, input("Enter page reference string: ").split()))
frames = int(input("Enter number of frames: "))
print("Page Faults =", fifo(pages, frames))
