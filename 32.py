def lru(pages, frames):
    frame = []
    faults = 0
    for i, p in enumerate(pages):
        if p not in frame:
            if len(frame) < frames:
                frame.append(p)
            else:
                # replace least recently used
                lru_index = min(frame, key=lambda x: pages[:i][::-1].index(x))
                frame[frame.index(lru_index)] = p
            faults += 1
    return faults

pages = list(map(int, input("Enter page reference string: ").split()))
frames = int(input("Enter number of frames: "))
print("Page Faults =", lru(pages, frames))
